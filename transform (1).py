import pandas as pd

def transform_data(df_raw):
    df_raw.columns = df_raw.columns.str.strip().str.lower()
    cleaned_data = []

    for idx, record in df_raw.iterrows():
        try:
            # Validasi dan transformasi data
            title = str(record['title']).strip()
            price = float(str(record['price']).replace('$', '').replace(',', '').strip()) * 16000
            rating = float(str(record['rating']).split('/')[0].replace('⭐', '').strip())

            # PERBAIKAN: Tanda kurung yang benar untuk ekstraksi color
            color_str = str(record['color'])
            color = int(''.join(filter(str.isdigit, color_str))) if any(c.isdigit() for c in color_str) else 0

            size = str(record['size']).strip().upper()
            gender = str(record['gender']).strip().title()

            cleaned_data.append({
                'title': title,
                'price': price,
                'rating': rating,
                'color': color,
                'size': size,
                'gender': gender,
                'timestamp': pd.to_datetime(record['timestamp'])
            })
        except Exception as e:
            print(f"[WARNING] Error pada record {idx}: {str(e)}")
            continue

    return pd.DataFrame(cleaned_data).drop_duplicates().dropna()

if __name__ == "__main__":
    df_raw = pd.read_csv("extracted_product_data.csv")
    df_clean = transform_data(df_raw)
    df_clean.to_csv("cleaned_product_data.csv", index=False)
    print(f"Data berhasil ditransformasi: {len(df_clean)} record")
