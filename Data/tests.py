from django.test import TestCase
# Data/tests.py
from django.test import TestCase
from shop.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.product = Product.objects.create(
            name="Test Product",
            price=19.99,
            description="A test product for unit testing."
        )

    def test_product_name(self):
        # Test that the product name is correct
        self.assertEqual(self.product.name, "Test Product")

    def test_product_price(self):
        # Test that the product price is correct
        self.assertEqual(self.product.price, 19.99)

    def test_product_description(self):
        # Test that the product description is correct
        self.assertEqual(self.product.description, "A test product for unit testing.")


