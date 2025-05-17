import unittest
import pandas as pd
from utils.extract import extract_data
from utils.transform import transform_data

class TestTransform(unittest.TestCase):
    def test_transform_data_returns_dataframe(self):
        raw_df = extract_data()
        cleaned_df = transform_data(raw_df)
        self.assertIsInstance(cleaned_df, pd.DataFrame)

    def test_transform_data_valid_structure(self):
        raw_df = extract_data()
        cleaned_df = transform_data(raw_df)
        self.assertGreater(len(cleaned_df), 0, "Data hasil transformasi tidak boleh kosong")
        self.assertIn('price', cleaned_df.columns)
        self.assertTrue(cleaned_df['price'].dtype in [float, int])
