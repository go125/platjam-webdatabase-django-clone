from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from stocks.models import Stock
from stocks.forms import StockForm, StockInForm, StockOutForm

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
    stock=get_object_or_404(Stock, pk=stock_id)
    if request.method=='POST':
        form = StockInForm(request.POST)
        if form.is_valid():
            in_num = form.cleaned_data["in_num"]
            stock_num_before = stock.stock_num
            stock_num_after = stock_num_before + in_num
            stock.stock_num = stock_num_after
            stock.save()
            return redirect(stock_detail, stock_id=stock_id)
    else:
        form=StockInForm()
    return render(request, "stocks/stock_in.html",{'form':form, 'stock':stock})

@login_required
def stock_out(request, stock_id):
    stock=get_object_or_404(Stock, pk=stock_id)
    stock_num_before = stock.stock_num
    if request.method=='POST':
        form = StockOutForm(request.POST)
        if form.is_valid():
            out_num = form.cleaned_data["out_num"]
            stock_num_after = stock_num_before - out_num
            if stock_num_after >= 0:
                stock.stock_num = stock_num_after
                stock.save()
                return redirect(stock_detail, stock_id=stock_id)
            else:
                e="在庫数を超す数の出庫はできません"
                return render(request, "stocks/stock_out.html",{'form':form, "stock":stock, "error":e})

    else:
        form=StockOutForm()
    return render(request, "stocks/stock_out.html",{'form':form, "stock":stock})
