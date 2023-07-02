from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from stocks.models import Stock
from stocks.forms import StockForm
# Create your views here.
def top(request):
    stocks = Stock.objects.all()
    context = {"stocks":stocks}
    return render(request, "stocks/top.html", context)

@login_required
def stock_new(request):
    if request.method=='POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock=form.save(commit=False)
            stock.managed_by=request.user
            stock.save()
            return redirect(stock_detail, stock_id=stock.pk)
    else:
        form=StockForm()
    return render(request, "stocks/stock_new.html",{'form':form})

@login_required
def stock_edit(request, stock_id):
    stock=get_object_or_404(Stock, pk=stock_id)
    if stock.managed_by.id != request.user.id:
        return HttpResponseForbidden("この材料の詳細情報の編集は許可されていません。")
    if request.method=='POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect(stock_detail, stock_id=stock_id)
    else:
        form=StockForm(instance=stock)
    return render(request, "stocks/stock_edit.html",{'form':form})

def stock_detail(request, stock_id):
    stock=get_object_or_404(Stock, pk=stock_id)
    return render(request, "stocks/stock_detail.html", {"stock":stock})

@login_required
def stock_in(request, stock_id):
    # TODO 編集可能項目数を減らす
    stock=get_object_or_404(Stock, pk=stock_id)
    if request.method=='POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect(stock_detail, stock_id=stock_id)
    else:
        form=StockForm(instance=stock)
    return render(request, "stocks/stock_in.html",{'form':form})

@login_required
def stock_out(request, stock_id):
    # TODO 編集可能項目数を減らす
    stock=get_object_or_404(Stock, pk=stock_id)
    if request.method=='POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect(stock_detail, stock_id=stock_id)
    else:
        form=StockForm(instance=stock)
    return render(request, "stocks/stock_out.html",{'form':form})
