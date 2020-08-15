from django.shortcuts import render, redirect
import requests
from .models import Stock
from .forms import StockAdd
# Create your views here.

API_KEY = 'GHO3SKBQEV878JXX'
BASE_URI = 'https://www.alphavantage.co/'

def quotes(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_data = requests.get('{}query?function=OVERVIEW&symbol={}&apikey={}'.format(BASE_URI, ticker, API_KEY))
        if not api_data.json() or api_data.json().get('Error Message'):
            return render(request, 'quotes/quotes.html', {'error': 'error'})
        return render(request, 'quotes/quotes.html', {'api': api_data.json()})
    else:
        return render(request, 'quotes/quotes.html', {'ticker': 'ticker'})

def show_all(request):
    data_list = []
    data = Stock.objects.all()
    for single in data:
        api_data = requests.get('{}query?function=OVERVIEW&symbol={}&apikey={}'.format(BASE_URI, single, API_KEY))
        api_data = api_data.json()
        api_data['id'] = single.id
        data_list.append(api_data)
    return render(request, 'quotes/show_all.html', {'data' : data_list})

def add_stock(request):
    forms_data = StockAdd(request.POST)
    print(forms_data.is_valid())
    if forms_data.is_valid():
        ticker = forms_data.cleaned_data['ticker']
        ticker_data = Stock(ticker=ticker)
        ticker_data.save()
    return redirect(show_all)

def delete_stock(request, stock_id):
    stock_obj = Stock.objects.filter(pk=stock_id)
    print(stock_obj)
    stock_obj.delete()
    return redirect(show_all)