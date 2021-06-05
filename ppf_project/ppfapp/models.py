from django.db import models


class mrp_linewise_store(models.Model):
    coupli_board=models.CharField(max_length=100)
    itemname=models.CharField(max_length=100)
    station_no=models.CharField(max_length=100)
    quantity=models.IntegerField()
    date=models.DateField()

class mrp_store_opening(models.Model):
    coupli_board=models.CharField(max_length=100)
    quantity=models.IntegerField()
    date=models.DateField()

class mrp_store_closing(models.Model):
    coupli_board=models.CharField(max_length=100)
    quantity=models.IntegerField()
    date=models.DateField()

class sponge_common(models.Model):
    sponge_type = models.CharField(max_length=100)
    sponge_shape = models.CharField(max_length=100)
    station_no = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract=True

class mrp_sponge_opening(sponge_common):
    station_no = None
class mrp_sponge_closing(sponge_common):
    station_no = None

class mrp_linewise_sponge(models.Model):
    sponge_type=models.CharField(max_length=100)
    sponge_shape=models.CharField(max_length=100)
    itemname=models.CharField(max_length=100)
    station_no=models.CharField(max_length=100)
    quantity=models.IntegerField()
    date=models.DateField()

class mrp_linewise_bms(models.Model):
    lyf=models.CharField(max_length=100)
    itemname = models.CharField(max_length=100)
    station_no=models.CharField(max_length=100)
    quantity=models.IntegerField()
    date=models.DateField()

class bms_common(models.Model):
    lyf = models.CharField(max_length=100)
    itemname = models.CharField(max_length=100)
    station_no=models.CharField(max_length=100)
    quantity = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract=True
class mrp_bms_opening(bms_common):
    station_no = None
    itemname=None
class mrp_bms_closing(bms_common):
    station_no = None
    itemname = None

class item_master_main(models.Model):
    itemcode = models.CharField(max_length=50, unique=False)
    itemname = models.CharField(max_length=100, unique=False)





class item_master(models.Model):
    itemcode = models.CharField(max_length=50, unique=False)
    itemname = models.CharField(max_length=100, unique=False)
    status = models.CharField(max_length=50, unique=False)
    station_no = models.CharField(max_length=50, unique=False)
    pics_per_ladi = models.IntegerField(max_length=50, unique=False)

    coupli_or_board_size = models.CharField(max_length=200, unique=False)
    pics_per_coupli = models.CharField(max_length=100, unique=False)
    sponge_type = models.CharField(max_length=100, unique=False)
    sponge_shape = models.CharField(max_length=100, unique=False)

    l1 = models.CharField(max_length=100, unique=False)
    l1_qty = models.FloatField(max_length=50, unique=False)

    l2 = models.CharField(max_length=100, unique=False)
    l2_qty = models.FloatField(max_length=50, unique=False)

    l3 = models.CharField(max_length=100, unique=False)
    l3_qty =models.FloatField(max_length=50, unique=False)

    l4 = models.CharField(max_length=100, unique=False)
    l4_qty = models.FloatField(max_length=50, unique=False)

    l5 = models.CharField(max_length=100, unique=False)
    l5_qty = models.FloatField(max_length=50, unique=False)
    l6 = models.CharField(max_length=100, unique=False)
    l6_qty = models.FloatField(max_length=50, unique=False)

    f1 = models.CharField(max_length=100, unique=False)
    f1_qty =models.FloatField(max_length=50, unique=False)
    f2 = models.CharField(max_length=100, unique=False)
    f2_qty = models.FloatField(max_length=50, unique=False)
    f3 = models.CharField(max_length=100, unique=False)
    f3_qty = models.FloatField(max_length=50, unique=False)
    f4 = models.CharField(max_length=100, unique=False)
    f4_qty =models.FloatField(max_length=50, unique=False)
    f5 = models.CharField(max_length=100, unique=False)
    f5_qty = models.FloatField(max_length=50, unique=False)
    f6 = models.CharField(max_length=100, unique=False)
    f6_qty = models.FloatField(max_length=50, unique=False)

    d1 = models.CharField(max_length=100, unique=False)
    d1_qty = models.FloatField(max_length=50, unique=False)
    d2 = models.CharField(max_length=100, unique=False)
    d2_qty = models.FloatField(max_length=50, unique=False)
    d3 = models.CharField(max_length=100, unique=False)
    d3_qty =models.FloatField(max_length=50, unique=False)
    d4 = models.CharField(max_length=100, unique=False)
    d4_qty = models.FloatField(max_length=50, unique=False)
    d5 = models.CharField(max_length=100, unique=False)
    d5_qty = models.FloatField(max_length=50, unique=False)
    d6 = models.CharField(max_length=100, unique=False)
    d6_qty = models.FloatField(max_length=50, unique=False)

    item_master_align_id = models.IntegerField(max_length=100, unique=False)


class item_master_copy(models.Model):
    itemcode = models.CharField(max_length=50, unique=False)
    itemname = models.CharField(max_length=100, unique=False)
    status = models.CharField(max_length=50, unique=False)
    station_no = models.CharField(max_length=50, unique=False)
    pics_per_ladi = models.IntegerField(max_length=50, unique=False)

    coupli_or_board_size = models.CharField(max_length=200, unique=False)
    pics_per_coupli = models.CharField(max_length=100, unique=False)
    sponge_type = models.CharField(max_length=100, unique=False)
    sponge_shape = models.CharField(max_length=100, unique=False)

    l1 = models.CharField(max_length=100, unique=False)
    l1_qty = models.FloatField(max_length=50, unique=False)

    l2 = models.CharField(max_length=100, unique=False)
    l2_qty = models.FloatField(max_length=50, unique=False)

    l3 = models.CharField(max_length=100, unique=False)
    l3_qty = models.FloatField(max_length=50, unique=False)

    l4 = models.CharField(max_length=100, unique=False)
    l4_qty = models.FloatField(max_length=50, unique=False)

    l5 = models.CharField(max_length=100, unique=False)
    l5_qty = models.FloatField(max_length=50, unique=False)
    l6 = models.CharField(max_length=100, unique=False)
    l6_qty = models.FloatField(max_length=50, unique=False)

    f1 = models.CharField(max_length=100, unique=False)
    f1_qty = models.FloatField(max_length=50, unique=False)
    f2 = models.CharField(max_length=100, unique=False)
    f2_qty = models.FloatField(max_length=50, unique=False)
    f3 = models.CharField(max_length=100, unique=False)
    f3_qty = models.FloatField(max_length=50, unique=False)
    f4 = models.CharField(max_length=100, unique=False)
    f4_qty = models.FloatField(max_length=50, unique=False)
    f5 = models.CharField(max_length=100, unique=False)
    f5_qty = models.FloatField(max_length=50, unique=False)
    f6 = models.CharField(max_length=100, unique=False)
    f6_qty = models.FloatField(max_length=50, unique=False)

    d1 = models.CharField(max_length=100, unique=False)
    d1_qty = models.FloatField(max_length=50, unique=False)
    d2 = models.CharField(max_length=100, unique=False)
    d2_qty = models.FloatField(max_length=50, unique=False)
    d3 = models.CharField(max_length=100, unique=False)
    d3_qty = models.FloatField(max_length=50, unique=False)
    d4 = models.CharField(max_length=100, unique=False)
    d4_qty = models.FloatField(max_length=50, unique=False)
    d5 = models.CharField(max_length=100, unique=False)
    d5_qty = models.FloatField(max_length=50, unique=False)
    d6 = models.CharField(max_length=100, unique=False)
    d6_qty = models.FloatField(max_length=50, unique=False)

    item_master_align_id = models.IntegerField(max_length=100, unique=False)


    date=models.DateField()



class material_requisition(models.Model):
    mr_parameter=models.CharField(max_length=50, unique=False)
    mr_entity_name=models.CharField(max_length=50, unique=False)




class production_planning(models.Model):
    itemcode = models.CharField(max_length=50, unique=False)
    itemname=models.CharField(max_length=100,unique=False)
    quantity = models.IntegerField(max_length=100,unique=False)
    date=models.DateField()

class opening_balance(models.Model):
    itemcode = models.CharField(max_length=50, unique=False)
    itemname=models.CharField(max_length=100,unique=False)
    quantity = models.IntegerField(max_length=100,unique=False)
    date=models.DateField()

class closing_balance(models.Model):
    itemcode = models.CharField(max_length=50, unique=False)
    itemname=models.CharField(max_length=100,unique=False)
    quantity = models.IntegerField(max_length=100,unique=False)
    date=models.DateField()

class production_damage(models.Model):
    itemcode = models.CharField(max_length=50, unique=False)
    itemname=models.CharField(max_length=100,unique=False)
    quantity = models.IntegerField(max_length=100,unique=False)
    date=models.DateField()

class production_completed(models.Model):
    itemcode = models.CharField(max_length=50, unique=False)
    itemname=models.CharField(max_length=100,unique=False)
    quantity = models.IntegerField(max_length=100,unique=False)
    date=models.DateField()

class production_order(models.Model):
    itemcode = models.CharField(max_length=50, unique=False)
    itemname = models.CharField(max_length=100, unique=False)
    quantity = models.IntegerField(max_length=100, unique=False)
    date = models.DateField()
    datetime=models.CharField(max_length=100,unique=False)

