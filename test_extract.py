import unittest
import pandas as pd
from utils.extract import extract_data

class TestExtract(unittest.TestCase):
    def test_extract_data_returns_dataframe(self):
        df = extract_data()
        self.assertIsInstance(df, pd.DataFrame)

    def test_extract_data_not_empty(self):
        df = extract_data()
        self.assertGreater(len(df), 0, "Data hasil ekstraksi tidak boleh kosong")
