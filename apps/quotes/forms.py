from django import forms

class StockAdd(forms.Form):
    ticker = forms.CharField(label='Stock Name', max_length=10)
