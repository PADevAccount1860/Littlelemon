from django.test import TestCase
#from django.test import Client
#from django.test.utils import setup_test_environment
from django.urls import reverse
from restaurant.models import Menu
import json

#setup_test_environment()
#client = Client()

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='IceCream', price=80, inventory=100)
    
    def test_getall(self):
        response = self.client.get(reverse('menu'))
        content = json.loads(response.content)
        content = [{'title': d['title'], 'price': d['price'], 'inventory': d['inventory']} for d in content]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, [{'title': 'IceCream', 'price': '80.00', 'inventory': 100}])