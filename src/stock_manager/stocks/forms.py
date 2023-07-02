from django import forms

from stocks.models import Stock


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('name', 'amount', 'stock_type', 'remarks')

class StockInForm(forms.Form):
    in_num=forms.IntegerField(label='入庫数')

class StockOutForm(forms.Form):
    out_num=forms.IntegerField(label='出庫数')
