from unittest import skip
from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.models import User
from shop.models import Category,Product
from django.test import Client
from shop.views import all_products

# @skip("demonstrating skipping")
# class testSkip(TestCase):
#     def test_skip_exmaple(self):
#         pass
class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()

    def test_url_allowed_hosts(self):

        response = self.c.get('/')
        self.assertEqual(response.status_code,200)

    def test_product_detail_url(self):
        response = self.c.get(reverse('shop:product_detail',args=['telefon']))

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        print(html)
        self.assertIn("<title>Home</title>",html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code,200)
