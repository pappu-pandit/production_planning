from django import forms


class DateInput(forms.DateInput):
    input_type='date'

class inputtest(forms.Form):
    first=forms.IntegerField()
    last=forms.IntegerField(widget=forms.TextInput(attrs={"onkeydown":"search(this)"}))

class date(forms.Form):
    date=forms.DateField(widget=DateInput())

class alignment(forms.Form):
    find=forms.IntegerField()
    replace=forms.IntegerField()
    itemcode=forms.CharField()
    status=forms.CharField()
    station_no=forms.CharField()
    duration=forms.CharField()
    pics_per_ladi=forms.IntegerField()
    layer_quantity=forms.IntegerField()
    finishing_quantity = forms.IntegerField()
    decoration_quantity = forms.IntegerField()

class mrp_store(forms.Form):

    line1 = forms.IntegerField()
    line2 = forms.IntegerField()
    line3 = forms.IntegerField()
    line4 = forms.IntegerField()
    line5 = forms.IntegerField()
    line6 = forms.IntegerField()
    line7 = forms.IntegerField()
    line8 = forms.IntegerField()
    line9 = forms.IntegerField()

class trending_form(forms.Form):

    interval = forms.CharField()
    date=forms.DateField(widget=DateInput())







