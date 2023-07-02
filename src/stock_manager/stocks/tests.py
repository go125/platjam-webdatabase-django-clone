from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import resolve

from stocks.models import Stock
from stocks.views import top, stock_new, stock_edit, stock_detail, stock_in, stock_out

UserModel = get_user_model()

class TopPageTest(TestCase):
    def test_top_returns_200(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code, 200)

class TopPageRenderStocksTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.stock = Stock.objects.create(
            name="米粉",
            amount="25kg",
            stock_type = 1,
            stock_num = 5,
            managed_by = self.user,
            remarks = "国産",
        )

    def test_should_return_stock_name(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.stock.name)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)

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
