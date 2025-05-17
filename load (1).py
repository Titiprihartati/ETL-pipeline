import pandas as pd

def load_to_csv(df, output_path="final_product_data.csv"):
    try:
        df.to_csv(output_path, index=False)
        print(f"Data berhasil disimpan di: {output_path}")
        return True
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")
        return False

if __name__ == "__main__":
    df = pd.read_csv("cleaned_product_data.csv")
    load_to_csv(df)

