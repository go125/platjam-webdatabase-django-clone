from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from stocks.views import top, stock_new, stock_edit, stock_detail, stock_in, stock_out

class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        request=HttpRequest()
        response=top(request)
        self.assertEqual(response.status_code, 200)

class TopPageTest(TestCase):
    def test_top_returns_200(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code, 200)

class CreateStockTest(TestCase):
    def test_should_resolve_stock_new(self):
        found = resolve("/stocks/new/")
        self.assertEqual(stock_new, found.func)

class StockDetailTest(TestCase):
    def test_should_resolve_stock_detail(self):
        found = resolve("/stocks/1/")
        self.assertEqual(stock_detail, found.func)

class EditStockTest(TestCase):
    def test_should_resolve_stock_edit(self):
        found = resolve("/stocks/1/edit/")
        self.assertEqual(stock_edit, found.func)

class StockInTest(TestCase):
    def test_should_resolve_stock_in(self):
        found = resolve("/stocks/1/in/")
        self.assertEqual(stock_in, found.func)

class StockOutTest(TestCase):
    def test_should_resolve_stock_out(self):
        found = resolve("/stocks/1/out/")
        self.assertEqual(stock_out, found.func)
