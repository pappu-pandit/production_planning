from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import inputtest,date,alignment,mrp_store,trending_form
from django.http import JsonResponse
from django.db.models import Sum,Count,Q,Max
from django.db import connection
from .models import  item_master,production_planning,opening_balance,production_damage,production_completed,production_order,item_master_copy,item_master_main,closing_balance,\
    material_requisition,mrp_linewise_store,mrp_linewise_sponge,mrp_linewise_bms,mrp_store_opening,mrp_store_closing,mrp_sponge_opening,mrp_sponge_closing,mrp_bms_closing,mrp_bms_opening
from .resources import production_order_resource
from django.contrib import messages
from tablib import Dataset
#import pandas as pd
import math
import time
from datetime import datetime,timedelta,date as fdate
from asgiref.sync import sync_to_async
import pytz
#IST = pytz.timezone('Asia/Kolkata')
#print(datetime.now(IST))

today = fdate.today()
tomorrow = fdate.today() + timedelta(days=1)
yesterday = fdate.today() - timedelta(days=1)


def opening_store(request):

    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        fm = date(initial={'date':today})
        openinglist = []
        # data = item_master_copy.objects.all()
        data = material_requisition.objects.filter(mr_parameter='coupli_or_board_size')
        for i in data:
            coupli_board = i.mr_entity_name
            id=i.id
            opening1 = mrp_store_opening.objects.filter(date=today, coupli_board=coupli_board).aggregate(Sum('quantity'))

            opening1 = opening1['quantity__sum']

            if opening1 == None:
                opening1 = 0

            dit = {'id':id,'coupli_board': coupli_board,'opening_balance': opening1}

            ditcopy = dit.copy()
            openinglist.append(ditcopy)

        if request.method == 'POST':
            qset = request.POST
            # rint(qset)
            keytolist = qset.keys()
            keylist = list(keytolist)
            # print("list:",keylist)
            newlist = deletekeylist(keylist)
            # print(newlist)
            # print("key:",v[3])

            datee = request.POST['date']
            for i in newlist:
                data1 = request.POST[i]

                if data1:

                    p = material_requisition.objects.filter(id=int(i))
                    coupli_board = p[0].mr_entity_name
                    mrp_store_opening.objects.create(coupli_board=coupli_board, quantity=data1, date=datee)
                else:
                    pass
            messages.info(request, 'Opening Balance inserted')
            return HttpResponseRedirect('opening_store', {'form': fm, 'data': openinglist,'date':today})
        else:
            return render(request, 'opening_store.html', {'form': fm, 'data': openinglist,'date':today})
    else:
        return HttpResponseRedirect('login')


def micro_mrp(request):
    return render(request,'test.html')

def material_requisition_store(request):
    today = fdate.today()
    tomorrow = fdate.today() + timedelta(days=1)
    yesterday = fdate.today() - timedelta(days=1)
    mrp_s=mrp_store()

    #itemcode = item_master_copy.objects.filter(date=today,status='YES').values('itemcode','itemname')

    dict_list=[]
    line_dict={}
    l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = l9 = 0
    #listt=[]
    if request.is_ajax() and request.method == "POST" or request.method=="POST":
        v1 = request.POST['item_name']
        v2 = request.POST['value']
        v3 = request.POST['iid']
        v4 = request.POST['itemname']

        print(v4)

        mrp_linewise_store.objects.create(coupli_board=v1,itemname=v4,station_no=v3,quantity=v2,date=today)
        return HttpResponseRedirect('store')

    lfd = item_master_copy.objects.filter(date=today)
    #print(lfd)
    coupli_list=material_requisition.objects.filter(mr_parameter='coupli_or_board_size')
    for list_coupli_board in coupli_list:

        #print("board:::",list_coupli_board.mr_entity_name)
        tt = item_master_copy.objects.filter(date=today, coupli_or_board_size=list_coupli_board.mr_entity_name)
        #print("query:", tt)
        if tt:
            t = t1=t2=t3=t4=t5=t6=t7=t8=t9=0
            line=0
            line_list = set()
            for i in tt:
                micro = 0
                b=''
                plan = production_planning.objects.filter(date=today, itemcode=i.itemcode).aggregate(Sum('quantity'))
                sett={y for y in line_list if y==i.station_no}
                if sett==set():
                    pass
                else:
                    a=iter(sett)
                    b=next(a)
                    if b:
                        print('b=',b)
                if b ==i.station_no:
                    pass
                else:
                    if plan['quantity__sum']:
                        mrp=mrp_linewise_store.objects.filter (date=today,station_no=i.station_no,coupli_board=list_coupli_board.mr_entity_name).aggregate(Sum('quantity'))
                        micro = mrp['quantity__sum']

                        if micro == None:
                            micro = 0
                        line_list.add(i.station_no)
                #print(line_list)

                #print("M==", micro,i.station_no,list_coupli_board.mr_entity_name)

                planning=plan['quantity__sum']

                if planning==None:
                    planning=0
                line=line + micro
                total_ladi = math.ceil(planning / i.pics_per_ladi)
                #print(total_ladi)
                total_quantity=math.ceil((total_ladi * i.pics_per_ladi) / int(i.pics_per_coupli))
                t = t + total_quantity

                if i.station_no=='Line1':
                    t1=t1 + total_quantity - micro
                elif i.station_no=="Line2":
                    t2=t2 + total_quantity -micro
                elif i.station_no == "Line3":
                    t3 = t3 + total_quantity -micro
                elif i.station_no == "Line4":
                    t4 = t4 + total_quantity -micro
                elif i.station_no == "Line5":
                    t5 = t5 + total_quantity -micro
                elif i.station_no == "Line6":
                    t6 = t6 + total_quantity -micro
                elif i.station_no == "Line7":
                    t7 = t7 + total_quantity -micro
                elif i.station_no == "Line8":
                    t8 = t8 + total_quantity -micro
                elif i.station_no == "Line9":
                    t9 = t9 + total_quantity -micro
                else:
                    pass


            l1 = l1 + t1
            l2 = l2 + t2
            l3 = l3 + t3
            l4 = l4 + t4
            l5 = l5 + t5
            l6 = l6 + t6
            l7 = l7 + t7
            l8 = l8 + t8
            l9 = l9 + t9

            store_open=mrp_store_opening.objects.filter(coupli_board=list_coupli_board.mr_entity_name).aggregate(Sum('quantity'))
            store_open1=store_open['quantity__sum']
            if store_open1==None:
                store_open1=0
            close_bal=store_open1 - t
            if close_bal<0:
                close_bal=0

            dit={'coupli_board_size':list_coupli_board.mr_entity_name,'store_open':store_open1,'quantity':t,"given":line,"station1":t1,"station2":t2,"station3":t3,"station4":t4,
                     "station5":t5,"station6":t6,"station7":t7,"station8":t8,"station9":t9,'close_bal':close_bal}
            #print(dit)

            ditcopy=dit.copy()
            dict_list.append(ditcopy)
        else:
            store_open = mrp_store_opening.objects.filter(coupli_board=list_coupli_board.mr_entity_name).aggregate(Sum('quantity'))
            store_open1 = store_open['quantity__sum']
            if store_open1 == None:
                store_open1 = 0
            close_bal =0


            dit = {'coupli_board_size': list_coupli_board.mr_entity_name,'store_open':store_open1, 'quantity': 0,"given":0,"station1":0,"station2":0,"station3":0,"station4":0,
                     "station5":0,"station6":0,"station7":0,"station8":0,"station9":0,'close_bal':close_bal}

            ditcopy = dit.copy()
            dict_list.append(ditcopy)


    #print(dict_list)

    line_dict={"line1":l1,"line2":l2,"line3":l3,"line4":l4,"line5":l5,"line6":l6,"line7":l7,"line8":l8,"line9":l9}
    return render(request,'store.html',{'data':dict_list,'date':today,'form':mrp_s,'line_dict':line_dict,'lfd':lfd})



def opening_sponge(request):

    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        fm = date(initial={'date':today})
        openinglist = []
        # data = item_master_copy.objects.all()
        list_sponge_type = material_requisition.objects.filter(mr_parameter='sponge_type')
        list_sponge_shape = material_requisition.objects.filter(mr_parameter='sponge_shape')

        for sponge_type_item in list_sponge_type:
            type=sponge_type_item.mr_entity_name
            t_id=sponge_type_item.id

            for sponge_shape_item in list_sponge_shape:
                shape = sponge_shape_item.mr_entity_name
                s_id=sponge_shape_item.id

                id=str(t_id) + '#' + str(s_id)
                #print(id)
                opening1 = mrp_sponge_opening.objects.filter(date=today, sponge_type=type , sponge_shape=shape).aggregate(Sum('quantity'))

                opening1 = opening1['quantity__sum']

                if opening1 == None:
                    opening1 = 0
                if type =='yellow_pink_orange' or type == 'yellow_vanilla_veg' or type == 'dark_veg(33%)_vanilla_veg(66%)':
                    pass
                else:
                    dit = {'id':id,'sponge_type': type,'sponge_shape':shape,'opening_balance': opening1}

                    ditcopy = dit.copy()
                    openinglist.append(ditcopy)

        if request.method == 'POST':
            qset = request.POST
            # rint(qset)
            keytolist = qset.keys()
            keylist = list(keytolist)
            # print("list:",keylist)
            newlist = deletekeylist(keylist)
            # print(newlist)
            # print("key:",v[3])

            datee = request.POST['date']
            for i in newlist:
                data1 = request.POST[i]
                if data1:
                    data2=i.split('#')
                    t_id=data2[0]
                    s_id=data2[1]
                    t = material_requisition.objects.filter(id=int(t_id))
                    s = material_requisition.objects.filter(id=int(s_id))
                    sp_type = t[0].mr_entity_name
                    sp_shape= s[0].mr_entity_name

                    #print(coupli_board,sp_shape)
                    mrp_sponge_opening.objects.create(sponge_type=sp_type,sponge_shape=sp_shape, quantity=data1, date=datee)
                else:
                    pass
            messages.info(request, 'Opening Balance inserted')
            return HttpResponseRedirect('opening_sponge', {'form': fm, 'data': openinglist,'date':today})
        else:
            return render(request, 'opening_sponge.html', {'form': fm, 'data': openinglist,'date':today})
    else:
        return HttpResponseRedirect('login')


def material_requisition_sponge(request):
    today = fdate.today()


    dict_list=[]
    list_dict={}
    l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = l9 = 0
    lfd = item_master_copy.objects.filter(date=today)
    if request.is_ajax() and request.method == "POST" or request.method=="POST":
        sp_type = request.POST['sp_type']
        sp_shape = request.POST['sp_shape']
        itemname=request.POST['item']
        qty = request.POST['value']
        station = request.POST['iid']


        mrp_linewise_sponge.objects.create(sponge_type=sp_type,sponge_shape=sp_shape,itemname=itemname,quantity=qty,station_no=station,date=today)
        return HttpResponseRedirect('sponge')


    sp_type_list=material_requisition.objects.filter(mr_parameter='sponge_type')
    sp_shape_list = material_requisition.objects.filter(mr_parameter='sponge_shape')
    index = 0
    for sp_type_item in sp_type_list:
        print("main::",sp_type_item.mr_entity_name)
        for sp_shape_item in sp_shape_list:

            tt = item_master_copy.objects.filter(date=today, sponge_type=sp_type_item.mr_entity_name,sponge_shape=sp_shape_item.mr_entity_name)

            t = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = 0
            line = 0
            line_list = set()
            stn_no=''
            for i in tt:
                micro = 0
                b = ''
                plan = production_planning.objects.filter(date=today, itemcode=i.itemcode).aggregate(Sum('quantity'))
                sett = {y for y in line_list if y == i.station_no}
                if sett == set():
                    pass
                else:
                    a = iter(sett)
                    b = next(a)
                    if b:
                        print('b=', b)
                if b == i.station_no:
                    pass
                else:
                    if plan['quantity__sum']:
                        mrp = mrp_linewise_sponge.objects.filter(date=today, station_no=i.station_no,sponge_type=sp_type_item.mr_entity_name,sponge_shape=sp_shape_item.mr_entity_name).aggregate(Sum('quantity'))
                        micro = mrp['quantity__sum']

                        if micro == None:
                            micro = 0
                        line_list.add(i.station_no)
                planning=plan['quantity__sum']
                if planning==None:
                    planning=0
                line = line + micro
                total_ladi = math.ceil(planning / i.pics_per_ladi)
                t = t + total_ladi
                #print("line=",line)


                if i.station_no=='Line1':
                    t1=t1 + total_ladi - micro

                elif i.station_no=="Line2":
                    t2=t2 + total_ladi -micro
                elif i.station_no == "Line3":
                    t3 = t3 + total_ladi -micro
                elif i.station_no == "Line4":
                    t4 = t4 + total_ladi -micro
                elif i.station_no == "Line5":
                    t5 = t5 + total_ladi -micro
                elif i.station_no == "Line6":
                    t6 = t6 + total_ladi -micro
                elif i.station_no == "Line7":
                    t7 = t7 + total_ladi -micro
                elif i.station_no == "Line8":
                    t8 = t8 + total_ladi -micro
                elif i.station_no == "Line9":
                    t9 = t9 + total_ladi -micro
                else:
                    pass

                stn_no = i.station_no
            l1 = l1 + t1
            l2 = l2 + t2
            l3 = l3 + t3
            l4 = l4 + t4
            l5 = l5 + t5
            l6 = l6 + t6
            l7 = l7 + t7
            l8 = l8 + t8
            l9 = l9 + t9

            sponge_open = mrp_sponge_opening.objects.filter(sponge_type=sp_type_item.mr_entity_name,sponge_shape=sp_shape_item.mr_entity_name,date=today).aggregate(
                Sum('quantity'))
            sponge_open1 = sponge_open['quantity__sum']
            if sponge_open1 == None:
                sponge_open1 = 0
            close_bal = sponge_open1 - t
            if close_bal < 0:
                close_bal = 0

            #print(t1)

            dit={"id":index,"sponge_type":sp_type_item.mr_entity_name,"sponge_shape":sp_shape_item.mr_entity_name,"sponge_open1":sponge_open1,"quantity":t,"given":line,"station1":t1,"station2":t2,"station3":t3,"station4":t4,
                     "station5":t5,"station6":t6,"station7":t7,"station8":t8,"station9":t9,"stn":stn_no,"close_bal":close_bal}
            ditcopy=dit.copy()
            dict_list.append(ditcopy)
            index=index+1

            if sp_type_item.mr_entity_name=='dark_veg(33%)_vanilla_veg(66%)' or sp_type_item.mr_entity_name=='yellow_vanilla_veg' :
                break
    #print(dict_list)
    def spongeadd(dit):
        data1 = [i for i in dict_list if i['sponge_type'] =='dark_veg(33%)_vanilla_veg(66%)' or  i['sponge_type'] == 'yellow_vanilla_veg' or i['sponge_type'] == 'yellow_pink_orange' ]

        dark_veg_ladhi=0
        vanilla_veg_ladhi=0
        yellow_ladhi=0
        pink_ladhi=0
        orange_ladhi=0
        yellow_one_kg_round=0
        pink_one_kg_round=0
        orange_one_kg_round=0
        #print(data1)
        for data in data1:

            #line = data['stn']
            #line = line[len(line) - 1]
            # print(line)

            #stn = 'station' + str(line)
            #print(stn)

            if data['sponge_type']=="dark_veg(33%)_vanilla_veg(66%)":
                dark_veg_ladhi = math.ceil(data['quantity'] * 1/3)
                vanilla_veg_ladhi = math.ceil(data['quantity'] * 2/3)

            if data['sponge_type'] == "yellow_vanilla_veg":
                yellow_ladhi = math.ceil(data['quantity'] * 1 /60)
                vanilla_veg_ladhi = math.ceil(data['quantity'] * 1 /125)

            if data['sponge_type'] == "yellow_pink_orange" and data['sponge_shape'] == "one_kg_round":

                yellow_one_kg_round = math.ceil(data['quantity'] * 1 / 3)
                pink_one_kg_round = math.ceil(data['quantity'] * 1 / 3)
                orange_one_kg_round = math.ceil(data['quantity'] * 1 / 3)

            if data['sponge_type'] == "yellow_pink_orange" and data['sponge_shape'] == "ladhi":
                yellow_ladhi = math.ceil(data['quantity'] * 1 / 3)
                pink_ladhi = math.ceil(data['quantity'] * 1 / 3)
                orange_ladhi = math.ceil(data['quantity'] * 1 / 3)




            if dit['sponge_type']=='dark_veg' and dit['sponge_shape']=='ladhi':
                dit['quantity']=dit['quantity'] + dark_veg_ladhi
                dark_veg_ladhi = 0
                #print(dit)
            elif dit['sponge_type']=='vanilla_veg' and dit['sponge_shape']=='ladhi':
                #print(stn, dit)
                dit['quantity']=dit['quantity'] + vanilla_veg_ladhi

                #dit[stn]=dit[stn] + vanilla_veg_ladhi
                #print("vanilla===",vanilla_veg_ladhi)
                vanilla_veg_ladhi = 0
            elif dit['sponge_type'] == 'yellow' and dit['sponge_shape'] == 'ladhi':
                dit['quantity'] = dit['quantity'] + yellow_ladhi
                #dit[stn] = dit[stn] + yellow_ladhi
                yellow_ladhi = 0

            elif dit['sponge_type'] == 'pink' and dit['sponge_shape'] == 'ladhi':
                dit['quantity'] = dit['quantity'] + pink_ladhi
                pink_ladhi = 0

            elif dit['sponge_type'] == 'orange' and dit['sponge_shape'] == 'ladhi':
                dit['quantity'] = dit['quantity'] + orange_ladhi
                orange_ladhi = 0


            elif dit['sponge_type'] == 'yellow' and dit['sponge_shape'] == 'one_kg_round':
                dit['quantity'] = dit['quantity'] + yellow_one_kg_round
                yellow_one_kg_round=0

            elif dit['sponge_type'] == 'pink' and dit['sponge_shape'] == 'one_kg_round':
                dit['quantity'] = dit['quantity'] + pink_one_kg_round
                pink_one_kg_round=0

            elif dit['sponge_type'] == 'orange' and dit['sponge_shape'] == 'one_kg_round':
                dit['quantity'] = dit['quantity'] + orange_one_kg_round
                orange_one_kg_round=0

            else:
                pass


        return dit
    dict_list=list(map(spongeadd,dict_list))

    #[dict_list.remove(sponge_item) for sponge_item in dict_list if sponge_item['sponge_type']=='dark(33%)_vanilla(66%)' or sponge_item['sponge_type']=='yellow_vanilla' or sponge_item['sponge_type']=='yellow_pink_orange']
    [[dict_list.remove(sponge_item) for sponge_item in dict_list if sponge_item['sponge_type']=='dark_veg(33%)_vanilla_veg(66%)' or sponge_item['sponge_type']=='yellow_vanilla_veg' or sponge_item['sponge_type']=='yellow_pink_orange'  ]for i in range(len(dict_list))]

    #print(dict_list)
    print(l1)
    line_dict = {"line1": l1, "line2": l2, "line3": l3, "line4": l4, "line5": l5, "line6": l6, "line7": l7, "line8": l8,
                 "line9": l9}
    return render(request, 'sponge.html', {'data': dict_list,'line_dict':line_dict,'lfd':lfd, 'date': today})



def opening_bms(request):

    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        fm = date(initial={'date':today})
        openinglist = []
        # data = item_master_copy.objects.all()
        data = material_requisition.objects.filter(mr_parameter='layer_finish_decor')
        for i in data:
            lyf = i.mr_entity_name
            id=i.id
            opening1 = mrp_bms_opening.objects.filter(date=today, lyf=lyf).aggregate(Sum('quantity'))

            opening1 = opening1['quantity__sum']

            if opening1 == None:
                opening1 = 0

            dit = {'id':id,'lyf': lyf,'opening_balance': opening1}

            ditcopy = dit.copy()
            openinglist.append(ditcopy)

        if request.method == 'POST':
            qset = request.POST
            # rint(qset)
            keytolist = qset.keys()
            keylist = list(keytolist)
            # print("list:",keylist)
            newlist = deletekeylist(keylist)
            # print(newlist)
            # print("key:",v[3])

            datee = request.POST['date']
            for i in newlist:
                data1 = request.POST[i]

                if data1:

                    p = material_requisition.objects.filter(id=int(i))
                    lyf = p[0].mr_entity_name
                    mrp_bms_opening.objects.create(lyf=lyf, quantity=data1, date=datee)
                else:
                    pass
            messages.info(request, 'Opening Balance inserted')
            return HttpResponseRedirect('opening_bms', {'form': fm, 'data': openinglist,'date':today})
        else:
            return render(request, 'opening_bms.html', {'form': fm, 'data': openinglist,'date':today})
    else:
        return HttpResponseRedirect('login')



def material_requisition_bms(request):
    today = fdate.today()
    tomorrow = fdate.today() + timedelta(days=1)
    yesterday = fdate.today() - timedelta(days=1)

    lfd_data=material_requisition.objects.filter(mr_parameter='layer_finish_decor')
    item_master_data=item_master_copy.objects.filter(date=today)
    dict_list=[]
    line_dict={}
    l1=l2=l3=l4=l5=l6=l7=l8=l9=0
    if request.is_ajax() and request.method == "POST" or request.method == "POST":
        lyf = request.POST['lyf']
        qty = request.POST['value']
        station = request.POST['iid']
        mrp_linewise_bms.objects.create(lyf=lyf, quantity=qty, station_no=station,date=today)
        return HttpResponseRedirect('bms')

    for ldf_item in lfd_data:
        k=0

        t1 = 0
        t2 = 0
        t3 = 0
        t4 = 0
        t5 = 0
        t6 = 0
        t7 = 0
        t8 = 0
        t9 = 0
        line = 0
        line_list = set()
        for item_master_item in item_master_data:
            micro = 0
            b = ''
            plan=production_planning.objects.filter(date=today,itemcode=item_master_item.itemcode).aggregate(Sum('quantity'))
            sett = {y for y in line_list if y == item_master_item.station_no}
            if sett == set():
                pass
            else:
                a = iter(sett)
                b = next(a)
                if b:
                    print('b=', b)
            if b == item_master_item.station_no:
                pass
            else:
                if plan['quantity__sum']:
                    mrp = mrp_linewise_bms.objects.filter(date=today, station_no=item_master_item.station_no,lyf=ldf_item.mr_entity_name).aggregate(Sum('quantity'))
                    micro = mrp['quantity__sum']

                    if micro == None:
                        micro = 0
                    line_list.add(item_master_item.station_no)

            qty=plan['quantity__sum']
            if qty==None:
                qty=0
            line = line + micro
            total_ladi = math.ceil(qty / item_master_item.pics_per_ladi)

            s = 0
            t =0
            for i in range(1,7):
                if i==1:
                    if ldf_item.mr_entity_name==item_master_item.l1:
                        s= s+ item_master_item.l1_qty
                if i==2:
                    if ldf_item.mr_entity_name == item_master_item.l2:
                        s = s + item_master_item.l2_qty
                if i==3:
                    if ldf_item.mr_entity_name == item_master_item.l3:
                        s = s + item_master_item.l3_qty
                if i==4:
                    if ldf_item.mr_entity_name == item_master_item.l4:
                        s = s + item_master_item.l4_qty
                if i==5:
                    if ldf_item.mr_entity_name == item_master_item.l5:
                        s = s + item_master_item.l5_qty
                if i==6:
                    if ldf_item.mr_entity_name == item_master_item.l6:
                        s = s + item_master_item.l6_qty


            for i in range(1, 7):
                if i==1:
                    if ldf_item.mr_entity_name == item_master_item.f1:
                        s = s + item_master_item.f1_qty
                if i==2:
                    if ldf_item.mr_entity_name == item_master_item.f2:
                        s = s + item_master_item.f2_qty
                if i==3:
                    if ldf_item.mr_entity_name == item_master_item.f3:
                        s = s + item_master_item.f3_qty
                if i==4:
                    if ldf_item.mr_entity_name == item_master_item.f4:
                        s = s + item_master_item.f4_qty
                if i==5:
                    if ldf_item.mr_entity_name == item_master_item.f5:
                        s = s + item_master_item.f5_qty
                if i==6:
                    if ldf_item.mr_entity_name == item_master_item.f6:
                        s = s + item_master_item.f6_qty

            for i in range(1, 7):
                if i==1:
                    if ldf_item.mr_entity_name == item_master_item.d1:
                        s = s + item_master_item.d1_qty
                if i==2:
                    if ldf_item.mr_entity_name == item_master_item.d2:
                        s = s + item_master_item.d2_qty
                if i==3:
                    if ldf_item.mr_entity_name == item_master_item.d3:
                        s = s + item_master_item.d3_qty
                if i==4:
                    if ldf_item.mr_entity_name == item_master_item.d4:
                        s = s + item_master_item.d4_qty
                if i==5:
                    if ldf_item.mr_entity_name == item_master_item.d5:
                        s = s + item_master_item.d5_qty
                if i==6:
                    if ldf_item.mr_entity_name == item_master_item.d6:
                        s = s + item_master_item.d6_qty

            #print(s)
            t=s*total_ladi
            print("qtyyy::",total_ladi)
            if item_master_item.station_no == 'Line1':
                t1 = t1 + t - micro
            elif item_master_item.station_no == "Line2":
                t2 = t2 + t - micro
            elif item_master_item.station_no == "Line3":
                t3 = t3 + t - micro
            elif item_master_item.station_no == "Line4":
                t4 = t4 + t - micro
            elif item_master_item.station_no == "Line5":
                t5 = t5 + t - micro
            elif item_master_item.station_no == "Line6":
                t6 = t6 + t - micro
            elif item_master_item.station_no == "Line7":
                t7 = t7 + t - micro
            elif item_master_item.station_no == "Line8":
                t8 = t8 + t - micro
            elif item_master_item.station_no == "Line9":
                t9 = t9 + t - micro
            else:
                pass
            k=k+t
            #print("row:",k)
            #print("total row",t,item_master_item.itemcode,ldf_item.mr_entity_name)
        l1 = l1 + t1
        l2 = l2 + t2
        l3 = l3 + t3
        l4 = l4 + t4
        l5 = l5 + t5
        l6 = l6 + t6
        l7 = l7 + t7
        l8 = l8 + t8
        l9 = l9 + t9

        bms_open = mrp_bms_opening.objects.filter(lyf=ldf_item.mr_entity_name).aggregate(Sum('quantity'))
        bms_open1 = bms_open['quantity__sum']
        if bms_open1 == None:
            bms_open1 = 0
        close_bal = bms_open1 - k
        if close_bal < 0:
            close_bal = 0
        dit = {'lfd_items': ldf_item.mr_entity_name, "bms_opening":bms_open1, 'quantity': k,"given":line,"station1":t1,"station2":t2,"station3":t3,"station4":t4,
                     "station5":t5,"station6":t6,"station7":t7,"station8":t8,"station9":t9,"bms_closing":close_bal}
        ditcopy = dit.copy()
        dict_list.append(ditcopy)
        #print(ldf_item.mr_entity_name,s)
        print(dit)
    line_dict = {"total": "Total", "line1": l1, "line2": l2, "line3": l3, "line4": l4, "line5": l5, "line6": l6,
                 "line7": l7, "line8": l8,
                 "line9": l9}
    return render(request, 'bms.html', {'data': dict_list,'line_dict':line_dict, 'date': today})





def loginfm(request):
    fm = AuthenticationForm()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                paswd = fm.cleaned_data['password']

                user = authenticate(username=uname, password=paswd)
                if user is not None:
                    login(request, user)
                    print("inside login")
                    print(user)
                    return HttpResponseRedirect('planning')
        else:
            return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('planning')


def logoutfm(request):
    print(" Pre logout:",request.user)
    logout(request)
    print(" POST logout:", request.user)
    return HttpResponseRedirect('login')

def job_card(request,station):
    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        #fm=date()
        line1=[]
        print("today::::",today)
        itemcode=item_master_copy.objects.filter(Q(date=today),Q(station_no=station)).values('itemcode','itemname').distinct()
        print(itemcode)
        for code in itemcode:

            #itemname=code.itemname
            print(code['itemcode'])

            plann=production_planning.objects.filter(itemcode=code['itemcode'], date=today).aggregate(Sum('quantity'))
            #ladi=item_master_copy.objects.filter(Q(date=today) & Q(itemcode=code.itemcode) & Q(station_no='line1'))
            ladi=item_master_copy.objects.filter(Q(date=today) & Q(itemcode=code['itemcode']) & Q(station_no=station))


            #print("ladi",ladi[0])
            planning=plann['quantity__sum']
            pics_per_ladi=ladi[0].pics_per_ladi
            if planning==None:
                planning=0
            #print(planning)
            #print(pics_per_ladi)

            total_ladis=math.ceil(planning/pics_per_ladi)

            dit={'itemcode':code['itemcode'],'itemname':code['itemname'],'planning':planning,'pics_per_ladi':pics_per_ladi,'total_ladis':total_ladis}


            ditcopy=dit.copy()
            line1.append(ditcopy)
        return render(request,'job_card.html',{'dit':line1,'date':today,'station':station})
    else:
        return HttpResponseRedirect('login')



def changes(request):
    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        fm = date()
        align = alignment()
        itemcode=item_master.objects.values('itemcode')
        itemcode2=item_master_main.objects.values('itemcode')
        tt=item_master_main.objects.all()
        #print(pd.DataFrame(tt))
        #print("itemcode1:::=",itemcode1)
        #print("itemcode:::=",itemcode2)

        if request.is_ajax() and  request.method=='POST':

            print("ajax:",request.POST)

            itemcode=request.POST['userdata']
            #print(itemcode)
            if itemcode=='copy':

                item_master_data = item_master.objects.filter(status='yes').order_by('item_master_align_id')
                for data in item_master_data:
                    #item_master_copy.objects.create(itemcode=data.itemcode, itemname=data.itemname, status=data.status,station_no=data.station_no,item_master_align_id=data.item_master_align_id,pics_per_ladi=data.pics_per_ladi, date=tomorrow)
                    item_master_copy.objects.create(itemcode=data.itemcode, itemname=data.itemname,
                                               status=data.status, station_no=data.station_no, pics_per_ladi=data.pics_per_ladi,
                                               coupli_or_board_size=data.coupli_or_board_size,
                                               pics_per_coupli=data.pics_per_coupli, sponge_type=data.sponge_type,
                                               sponge_shape=data.sponge_shape,
                                               l1=data.l1, l1_qty=data.l1_qty, l2=data.l2, l2_qty=data.l2_qty,
                                               l3=data.l3, l3_qty=data.l3_qty, l4=data.l4, l4_qty=data.l4_qty,
                                               l5=data.l5, l5_qty=data.l5_qty, l6=data.l6, l6_qty=data.l6_qty,
                                               f1=data.f1, f1_qty=data.f1_qty, f2=data.f2,
                                               f2_qty=data.f2_qty, f3=data.f3, f3_qty=data.f3_qty,
                                               f4=data.f4, f4_qty=data.f4_qty,
                                               f5=data.f5, f5_qty=data.f5_qty, f6=data.f6,
                                               f6_qty=data.f6_qty, d1=data.d1, d1_qty=data.d1_qty,
                                               d2=data.d2, d2_qty=data.d2_qty,
                                               d3=data.d3, d3_qty=data.d3_qty, d4=data.d4,
                                               d4_qty=data.d4_qty, d5=data.d5, d5_qty=data.d5_qty,
                                               d6=data.d6, d6_qty=data.d6_qty,
                                               item_master_align_id=data.id,date=today)

                messages.info(request, 'status changed')
                return render(request, 'item.html', {'form': fm, 'alignment': align, 'itemcode2':itemcode,'itemcode':itemcode2})

            else:
                itemname=item_master_main.objects.filter(itemcode=itemcode)

                data=itemname[0].itemname
                return HttpResponse(data)


        if request.method=='POST':

            #print("POST:",request.POST)
            find=request.POST['find']
            replace=request.POST['replace']
            itemcode = request.POST['itemcode']
            status = request.POST['status']
            station = request.POST['station']


            if find and replace:
                data=item_master.objects.get(item_master_align_id=replace)
                item_master.objects.filter(item_master_align_id=find).update(item_master_align_id=replace)
                item_master.objects.filter(id=data.id).update(item_master_align_id=find)

            if itemcode and status:
                item_master.objects.filter(itemcode=itemcode).update(status=status)
            if itemcode and station:
                item_master.objects.filter(itemcode=itemcode).update(station_no=station)
        else:
            pass

        return render(request,'item.html',{'form':fm,'alignment':align,'itemcode2':itemcode,'itemcode':itemcode2})
    else:
        return HttpResponseRedirect('login')

def add_item_in_master(request):
    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        fm = date()
        align = alignment()
        request.session.modified=True
        itemcode2 = item_master_main.objects.values('itemcode')
        coupli_board_size=material_requisition.objects.filter(mr_parameter='coupli_or_board_size')
        sponge_type=material_requisition.objects.filter(mr_parameter='sponge_type')
        sponge_shape = material_requisition.objects.filter(mr_parameter='sponge_shape')
        lfd = material_requisition.objects.filter(mr_parameter='layer_finish_decor')
        if request.is_ajax() and request.method == 'POST':

            #print("ajax:", request.POST)

            itemcode = request.POST['userdata']
            # print(itemcode)
            if itemcode:
                itemname = item_master_main.objects.filter(itemcode=itemcode)

                data = itemname[0].itemname
                return HttpResponse(data)
            else:
                pass


        if request.method == 'POST':

            print("POST:",request.POST)

            itemcode = request.POST['itemcode']
            status = request.POST['status']
            station = request.POST['station']
            pics_per_ladi=request.POST['pics_per_ladi']
            coupli_or_board_size = request.POST['coupli_or_board_size']
            pics_per_coupli = request.POST['pics_per_coupli']
            sponge_type = request.POST['sponge_type']
            sponge_shape = request.POST['sponge_shape']

            l1=request.POST['l1']

            l2 = request.POST['l2']
            l3 = request.POST['l3']
            l4 = request.POST['l4']
            l5 = request.POST['l5']
            l6 = request.POST['l6']
            #print("layesrs:",l3)
            l1_qty = request.POST['l1_qty']
            l2_qty = request.POST['l2_qty']
            l3_qty = request.POST['l3_qty']
            l4_qty = request.POST['l4_qty']
            l5_qty = request.POST['l5_qty']
            l6_qty = request.POST['l6_qty']

            f1 = request.POST['f1']
            f2 = request.POST['f2']
            f3 = request.POST['f3']
            f4 = request.POST['f4']
            f5 = request.POST['f5']
            f6 = request.POST['f6']

            f1_qty = request.POST['f1_qty']
            f2_qty = request.POST['f2_qty']
            f3_qty = request.POST['f3_qty']
            f4_qty = request.POST['f4_qty']
            f5_qty = request.POST['f5_qty']
            f6_qty = request.POST['f6_qty']

            d1 = request.POST['d1']
            d2 = request.POST['d2']
            d3 = request.POST['d3']
            d4 = request.POST['d4']
            d5 = request.POST['d5']
            d6 = request.POST['d6']

            d1_qty = request.POST['d1_qty']
            d2_qty = request.POST['d2_qty']
            d3_qty = request.POST['d3_qty']
            d4_qty = request.POST['d4_qty']
            d5_qty = request.POST['d5_qty']
            d6_qty = request.POST['d6_qty']

            if l1 == '' and l1_qty=='':
                l1=0
                l1_qty=0
            if l2=='' and l2_qty=='':
                l2=0
                l2_qty=0
            if l3=='' and l3_qty=='':
                l3=0
                l3_qty=0
            if l4 == '' and l4_qty=='':
                l4=0
                l4_qty = 0
            if l5 == '' and l5_qty == '':
                l5=0
                l5_qty = 0
            if l6 == '' and l6_qty == '':
                l6=0
                l6_qty = 0

            if f1 == '' and f1_qty=='':
                f1=0
                f1_qty = 0
            if f2 == '' and f2_qty == '':
                f2=0
                f2_qty = 0
            if f3 == '' and f3_qty == '':
                f3=0
                f3_qty = 0
            if f4 == '' and f4_qty=='':
                f4=0
                f4_qty = 0
            if f5 == '' and f5_qty == '':
                f5=0
                f5_qty = 0
            if f6 == '' and f6_qty == '':
                f6=0
                f6_qty = 0

            if d1 == '' and d1_qty=='':
                d1=0
                d1_qty = 0
            if d2 == '' and d2_qty == '':
                d2=0
                d2_qty = 0
            if d3 == '' and d3_qty == '':
                d3=0
                d3_qty = 0
            if d4 == '' and d4_qty=='':
                d4=0
                d4_qty = 0
            if d5 == '' and d5_qty == '':
                d5=0
                d5_qty = 0
            if d6 == '' and d6_qty == '':
                d6=0
                d6_qty = 0


            if itemcode and status and station and pics_per_ladi:
                itemcode=item_master_main.objects.filter(itemcode=itemcode)
                id=item_master.objects.aggregate(Max('item_master_align_id'))
                if id['item_master_align_id__max'] == None:
                    id = 1
                else:
                    id =id['item_master_align_id__max'] +1

                item_master.objects.create(itemcode=itemcode[0].itemcode,itemname=itemcode[0].itemname,status=status,station_no=station,pics_per_ladi=pics_per_ladi,
                coupli_or_board_size=coupli_or_board_size,pics_per_coupli=pics_per_coupli,sponge_type=sponge_type,sponge_shape=sponge_shape,
                l1=l1,l1_qty=l1_qty,l2=l2,l2_qty=l2_qty,l3=l3,l3_qty=l3_qty,l4=l4,l4_qty=l4_qty,l5=l5,l5_qty=l5_qty,l6=l6,l6_qty=l6_qty,
                f1=f1, f1_qty=f1_qty,f2=f2, f2_qty=f2_qty,f3=f3, f3_qty=f3_qty,f4=f4, f4_qty=f4_qty,
                f5=f5, f5_qty=f5_qty,f6=f6, f6_qty=f6_qty, d1=d1, d1_qty=d1_qty, d2=d2, d2_qty=d2_qty,
                d3=d3, d3_qty=d3_qty, d4=d4, d4_qty=d4_qty, d5=d5, d5_qty=d5_qty, d6=d6, d6_qty=d6_qty,
                item_master_align_id=id)

        else:
            pass
        return render(request, 'add_item_in_master.html', {'form': fm, 'alignment': align, 'itemcode': itemcode2,'coupli':coupli_board_size,'sponge_type':sponge_type,'sponge_shape':sponge_shape,'lfd':lfd})
    else:
        return HttpResponseRedirect('login')

def upload(request):
    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)

        fm=date()
        itmcode=item_master.objects.values_list('itemcode')
        if request.method=='POST':
            order_data=production_order_resource()
            dataset=Dataset()
            file=request.FILES['myfile']
            orderdate=request.POST['date']
            print(file.name)
            if not file.name.endswith('xlsx'):
                messages.info(request,'Worng format ')
                return render(request,'upload.html')
            elif file.name=='sumo.xlsx':
                print('ggg')
                imported_data = dataset.load(file.read(), format='xlsx')
                i = 1
                for data in imported_data:

                    #v=item_master_main.objects.create(itemcode=data[0],itemname=data[1])

                    for code in itmcode:

                        if data[0]==code[0]:

                            #value = production_order(itemcode=data[0], itemname=data[1], quantity=data[3], date=today,datetime=today)
                            production_order.objects.update_or_create(itemcode=data[0], date=today,defaults={'itemcode': data[0],'itemname': data[1],'quantity':data[3],'date': orderdate,'datetime':today})
                            #value.save()
                            break

                            #i+=1
                        else:
                            pass


                messages.info(request, 'Successfully uploaded into database')
            else:
                messages.info(request, 'Wrong file selection')

            return HttpResponseRedirect('summary')


        return render(request,'upload.html',{'form':fm})
    else:
        return HttpResponseRedirect('login')


def deletekeylist(keylist):
    keylist.remove('csrfmiddlewaretoken')
    keylist.remove('date')
    keylist.remove('example_length')
    return keylist

def production_summary(request):

    if request.user.is_authenticated:

        fm = date()
        all_qty_table = []


        if request.method=='POST':
            select_date=request.POST['date']
            datee = select_date[8:10]
            pre = int(datee) - 1
            yr = select_date[0:8]
            pre_day = yr + str(pre)
            today=select_date
            yesterday=pre_day
            today=datetime.fromisoformat(today)
            #print("today:",type(today))

        else:
            today = fdate.today()
            yesterday = fdate.today() - timedelta(days=1)
            #print("today:", type(today))

        itemcode=item_master_copy.objects.filter(date=today).values('itemcode','itemname','item_master_align_id').order_by('item_master_align_id')
        #planning=production_planning.objects.values('itemcode').annotate(Sum('quantity',distinct=False))
        #open=opening_balance.objects.values('itemcode').annotate(openvar=Sum('quantity',distinct=False))
        #data = item_master_copy.objects.filter(date=today).order_by('item_master_align_id')

        for code in itemcode:

            itemcode = code['itemcode']
            itemname = code['itemname']
            id=code['item_master_align_id']

            planning = production_planning.objects.filter(itemcode=itemcode, date=today).aggregate(Sum('quantity'))
            opening_bal = opening_balance.objects.filter(itemcode=itemcode, date=today).aggregate(Sum('quantity'))
            p_completed = production_completed.objects.filter(itemcode=itemcode, date=today).aggregate(Sum('quantity'))
            p_damage = production_damage.objects.filter(itemcode=itemcode, date=today).aggregate(Sum('quantity'))
            #closing=closing_balance.objects.filter(date=today,itemcode=itemcode).aggregate(Sum('quantity'))
            p_order = production_order.objects.filter(itemcode=itemcode, date=today).aggregate(Sum('quantity'))

            #print(p_order)

            p_order = p_order['quantity__sum']
            plan = planning['quantity__sum']
            p_damage = p_damage['quantity__sum']
            #closing = closing['quantity__sum']
            opening_bal = opening_bal['quantity__sum']
            p_completed = p_completed['quantity__sum']

            if plan == None:
                plan = 0
            if p_order == None:
                p_order = 0

            if opening_bal == None:
                opening_bal = 0

            if p_completed == None:
                p_completed = 0
            #if closing == None:
                #closing = 0

            if p_damage == None:
                p_damage = 0

            t_production = opening_bal + p_completed
            var = t_production - p_damage - p_order

            if var < 0:
                variation = -(var)
                closing=0
            else:
                variation = 0
                closing=var


            dit = {'id':id,'itemcode': itemcode, 'itemname': itemname, 'plan_qty': plan, 'op_qty': opening_bal,
                   'p_completed_qty': p_completed, 't_production': t_production, 'p_damage': p_damage, 'p_order': p_order,
                   'variation': variation, 'closing_balance': closing}

            ditcopy = dit.copy()
            all_qty_table.append(ditcopy)
            cur_date = fdate.today()
            print("current date==",cur_date)
            if cur_date==today:
                closing_balance.objects.update_or_create(itemcode=itemcode, date=today,defaults={'itemcode': itemcode, 'itemname': itemname,'quantity': closing, 'date': today})

        return render(request, 'summary.html',{'itemcode': itemcode, 'dit': all_qty_table, 'form': fm, 'date': today, 'station': 'line1'})

    else:
        return HttpResponseRedirect('login')


def planning_submit(request):

    if request.user.is_authenticated:

        planlist = []
        today = fdate.today()

        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        fm = date(initial={'date': today})
        data = item_master_copy.objects.filter(date=today).order_by('item_master_align_id')
        #order=production_order.objects.filter(date=today)

        for i in data:

            itemcode=i.itemcode
            itemname=i.itemname
            item_master_align_id=i.item_master_align_id

            order=production_order.objects.filter(date=today,itemcode=itemcode)
            opening=opening_balance.objects.filter(date=today,itemcode=itemcode).aggregate(Sum('quantity'))
            planning=production_planning.objects.filter(date=today,itemcode=itemcode).aggregate(Sum('quantity'))
            closing=closing_balance.objects.filter(date=today,itemcode=itemcode).aggregate(Sum('quantity'))
            pro_comp=production_completed.objects.filter(date=today,itemcode=itemcode).aggregate(Sum('quantity'))
            pro_damage=production_damage.objects.filter(date=today,itemcode=itemcode).aggregate(Sum('quantity'))



            opening=opening['quantity__sum']
            closing = closing['quantity__sum']

            planning = planning['quantity__sum']
            pro_comp = pro_comp['quantity__sum']
            pro_damage = pro_damage['quantity__sum']
            if order:
                order=order[0].quantity
            else:
                order=0
            if opening==None:
                opening=0
            if planning==None:
                planning=0
            if closing == None:
                closing = 0
            if pro_comp == None:
                pro_comp = 0
            if pro_damage == None:
                pro_damage = 0
            t_production= opening + pro_comp
            var = t_production - pro_damage - order

            if var < 0:
                variation = -(var)
            else:
                variation = 0


            #closing_balance.objects.update_or_create(itemcode=itemcode, date=today,defaults={'itemcode': itemcode, 'itemname': itemname,'quantity': closing_bal, 'date': today})

            dit = {'itemcode': itemcode, 'itemname': itemname, 'item_master_align_id':item_master_align_id,'planning':planning,'production_done':pro_comp,'total_production':t_production,'pro_damage':pro_damage,'opening':opening,'variation':variation,'closing_balance':closing,'order':order}

            ditcopy = dit.copy()
            planlist.append(ditcopy)
            
            

        opening_balance_date = opening_balance.objects.last()
        if opening_balance_date == None:
            todayyy = today
            #print(todayyy)
        else:
            todayyy = opening_balance_date.date
            #print(todayyy)

        if todayyy == today:
            pass
        else:
            openbal = closing_balance.objects.filter(date=yesterday).order_by('id')
            for i in openbal:
                opening_balance.objects.create(itemcode=i.itemcode, itemname=i.itemname, quantity=i.quantity,date=today)

        item_master_date = item_master_copy.objects.last()
        if item_master_date == None:
            todayy = today
            print(todayy)
        else:
            todayy = item_master_date.date
            print(todayy)

        if todayy == today or todayy==tomorrow:

            if request.method=='POST':
                qset=request.POST
                #print(qset)
                keytolist=qset.keys()
                keylist=list(keytolist)
                #print("list:",keylist)
                newlist=deletekeylist(keylist)
                #print(newlist)
                #print("key:",v[3])
                datee = request.POST['date']
                print("list:",newlist)
                for i in newlist:
                    data1=request.POST[i]

                    if data1:

                        p=item_master_copy.objects.filter(item_master_align_id=int(i),date=today,)

                        itemname=p[0].itemname
                        itemcode=p[0].itemcode

                        production_planning.objects.create(itemcode=itemcode,itemname=itemname,quantity=data1,date=datee)
                    else:
                        pass

                messages.info(request, 'Planning SuccessFully inserted')
                return HttpResponseRedirect('planning', {'form': fm, 'data': planlist,'date':today})

            else:
                return  render(request,'palnning.html',{'form':fm,'data':planlist,'date':today})

        else:
            print("yesterdY:",yesterday)
            yes_data = item_master_copy.objects.filter(date=yesterday)
            print(yes_data)
            for data in yes_data:
                print("deepak")
                item_master_copy.objects.create(itemcode=data.itemcode, itemname=data.itemname,status=data.status, station_no=data.station_no,pics_per_ladi=data.pics_per_ladi,
                                                coupli_or_board_size=data.coupli_or_board_size,pics_per_coupli=data.pics_per_coupli, sponge_type=data.sponge_type,
                                                sponge_shape=data.sponge_shape,l1=data.l1, l1_qty=data.l1_qty, l2=data.l2,
                                                l2_qty=data.l2_qty,l3=data.l3, l3_qty=data.l3_qty, l4=data.l4,
                                                l4_qty=data.l4_qty,l5=data.l5, l5_qty=data.l5_qty, l6=data.l6,
                                                l6_qty=data.l6_qty,f1=data.f1, f1_qty=data.f1_qty,
                                                f2=data.f2,f2_qty=data.f2_qty, f3=data.f3, f3_qty=data.f3_qty,
                                                f4=data.f4, f4_qty=data.f4_qty,f5=data.f5, f5_qty=data.f5_qty,
                                                f6=data.f6,f6_qty=data.f6_qty, d1=data.d1, d1_qty=data.d1_qty,
                                                d2=data.d2, d2_qty=data.d2_qty,d3=data.d3, d3_qty=data.d3_qty,
                                                d4=data.d4,d4_qty=data.d4_qty, d5=data.d5, d5_qty=data.d5_qty,
                                                d6=data.d6, d6_qty=data.d6_qty,item_master_align_id=data.item_master_align_id, date=today)
            return render(request, 'palnning.html', {'form': fm, 'data': planlist,'date':today})
    else:
        return HttpResponseRedirect('login')


def opening_bal_submit(request):

    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        fm = date(initial={'date':today})
        openinglist = []
        # data = item_master_copy.objects.all()
        data = item_master_copy.objects.filter(date=today).order_by('item_master_align_id')

        for i in data:

            itemcode = i.itemcode
            itemname = i.itemname
            item_master_align_id = i.item_master_align_id

            opening1 = opening_balance.objects.filter(date=today, itemcode=itemcode).aggregate(Sum('quantity'))

            opening1 = opening1['quantity__sum']

            if opening1 == None:
                opening1 = 0

            dit = {'itemcode': itemcode, 'itemname': itemname, 'item_master_align_id': item_master_align_id,
                   'opening_balance': opening1}

            ditcopy = dit.copy()
            openinglist.append(ditcopy)

        if request.method == 'POST':
            qset = request.POST
            # rint(qset)
            keytolist = qset.keys()
            keylist = list(keytolist)
            # print("list:",keylist)
            newlist = deletekeylist(keylist)
            # print(newlist)
            # print("key:",v[3])

            datee = request.POST['date']
            for i in newlist:
                data1 = request.POST[i]

                if data1:
                    if data1.startswith('-'):
                        messages.info(request, 'Substraction not allowed !!!')
                        return HttpResponseRedirect('opening', {'form': fm, 'data': openinglist, 'date': today})
                    else:
                        p = item_master_copy.objects.filter(item_master_align_id=int(i),date=today)
                        itemname = p[0].itemname
                        itemcode = p[0].itemcode
                        opening_balance.objects.create(itemcode=itemcode, itemname=itemname, quantity=data1, date=datee)
                else:
                    pass
            messages.info(request, 'Opening Balance inserted')
            return HttpResponseRedirect('opening', {'form': fm, 'data': openinglist,'date':today})
        else:
            return render(request, 'opening_balance.html', {'form': fm, 'data': openinglist,'date':today})
    else:
        return HttpResponseRedirect('login')


def damage_submit(request):

    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        fm=date(initial={'date':today})
        damagelist = []

        data = item_master_copy.objects.filter(date=today).order_by('item_master_align_id')

        for i in data:

            itemcode = i.itemcode
            itemname = i.itemname
            item_master_align_id = i.item_master_align_id

            pro_damage = production_damage.objects.filter(date=today, itemcode=itemcode).aggregate(Sum('quantity'))

            pro_damage = pro_damage['quantity__sum']


            if pro_damage == None:
                pro_damage = 0


            dit = {'itemcode': itemcode, 'itemname': itemname, 'item_master_align_id': item_master_align_id,
                   'production_damage': pro_damage}

            ditcopy = dit.copy()
            damagelist.append(ditcopy)



        # data = item_master_copy.objects.all()
        #data = item_master_copy.objects.filter(date=today).order_by('item_master_align_id')

        if request.method == 'POST':
            qset = request.POST
            # rint(qset)
            keytolist = qset.keys()
            keylist = list(keytolist)
            # print("list:",keylist)
            newlist = deletekeylist(keylist)
            # print(newlist)
            # print("key:",v[3])

            datee = request.POST['date']
            for i in newlist:
                data1 = request.POST[i]
                if data1:
                    p = item_master_copy.objects.filter(item_master_align_id=int(i),date=today)
                    itemname = p[0].itemname
                    itemcode = p[0].itemcode
                    s = production_damage(itemcode=itemcode, itemname=itemname, quantity=data1, date=datee)
                    s.save()
                else:
                    pass

            messages.info(request, 'Damage inserted')
            return HttpResponseRedirect('damage', {'form': fm, 'data': damagelist,'date':today})
        else:
            return render(request, 'production_damage.html', {'form': fm, 'data': damagelist,'date':today})


    else:
        return HttpResponseRedirect('login')

def production_submit(request):


    if request.user.is_authenticated:
        today = fdate.today()
        tomorrow = fdate.today() + timedelta(days=1)
        yesterday = fdate.today() - timedelta(days=1)
        fm = date(initial={'date':today})
        productionlist = []


        #data = item_master_copy.objects.all()
        data = item_master_copy.objects.filter(date=today).order_by('item_master_align_id')

        for i in data:

            itemcode = i.itemcode
            itemname = i.itemname
            item_master_align_id = i.item_master_align_id

            production1 = production_completed.objects.filter(date=today, itemcode=itemcode).aggregate(Sum('quantity'))

            production1 = production1['quantity__sum']

            print("prod:::",production1)

            if production1 == None:
                production1 = 0

            dit = {'itemcode': itemcode, 'itemname': itemname, 'item_master_align_id': item_master_align_id,'production': production1}

            ditcopy = dit.copy()
            productionlist.append(ditcopy)




        if request.method == 'POST':
            qset = request.POST
            # rint(qset)
            keytolist = qset.keys()
            keylist = list(keytolist)
            # print("list:",keylist)
            newlist = deletekeylist(keylist)
            # print(newlist)
            # print("key:",v[3])

            datee = request.POST['date']
            for i in newlist:
                data1 = request.POST[i]
                if data1:
                    p = item_master_copy.objects.filter(item_master_align_id=int(i),date=today)
                    itemname = p[0].itemname
                    itemcode = p[0].itemcode

                    production_completed.objects.create(itemcode=itemcode, itemname=itemname, quantity=data1,
                                                        date=datee)

                else:
                    pass
            messages.info(request, 'submited')
            #return render(request, 'production_completrd.html', {'form': fm, 'data': productionlist})
            return HttpResponseRedirect('produced', {'form': fm, 'data': productionlist,'date':today})
        else:
            return render(request, 'production_completrd.html', {'form': fm, 'data': productionlist,'date':today})

    else:
        return HttpResponseRedirect('login')
