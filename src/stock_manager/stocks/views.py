from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def top(request):
    return HttpResponse(b"Hello, World!")

def stock_new(request):
    return HttpResponse("新規材料種類の登録")

def stock_edit(request, stock_id):
    return HttpResponse("材料プロパティの編集")

def stock_detail(request, stock_id):
    return HttpResponse("材料プロパティの詳細閲覧")

def stock_in(request, stock_id):
    return HttpResponse("材料の入庫")

def stock_out(request, stock_id):
    return HttpResponse("材料の出庫")
