#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        """Testing methods stealability"""
        prod = Product('Test Product', price=20, weight=10, flammability=1)
        self.assertEqual(prod.stealability(), "Very stealable!")

    def test_explode(self):
        """Testing methods explode"""
        prod = Product('Test Product', price=20, weight=10, flammability=1)
        self.assertEqual(prod.explode(), "...boom!")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """Test default lenth of generate_products()."""
        # prod = Product('Test Product')
        self.assertEqual(len(generate_products()), 30)
    # def test_legal_names(self):
    #     """Tests legal names. Not sure how to handle"""
    #     prod = Product('Test Product')
    #     self.assertEqual(prod.price, 10)


if __name__ == '__main__':
    unittest.main()
