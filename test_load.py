import unittest
import pandas as pd
import os
from utils.load import load_to_csv

class TestLoad(unittest.TestCase):
    def setUp(self):
        self.dummy_df = pd.DataFrame({
            'title': ['Test Product'],
            'price': [100000.0],
            'rating': [4.5],
            'color': [1],
            'size': ['M'],
            'gender': ['Unisex'],
            'timestamp': [pd.Timestamp.now()]
        })
        self.output_path = "test_output.csv"

    def test_load_to_csv_success(self):
        result = load_to_csv(self.dummy_df, self.output_path)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.output_path))

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
