from django.test import TestCase

from .models import Category, Menu


class CategoryModelTestCase(TestCase):
    def test_category_model(self):
        category = Category.objects.create(name='Test Category', names='Test Categories')
        self.assertEqual(str(category), 'Test Categories')


class MenuModelTestCase(TestCase):
    def test_menu_model(self):
        category = Category.objects.create(name='Test Category', names='Test Categories')
        menu = Menu.objects.create(name='Test Menu', category=category, path='/test/')
        self.assertEqual(str(menu), 'Test Menu')
