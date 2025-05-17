import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def extract_data():
    product_data = []

    for page in range(1, 51):  # Di Colab, batasi halaman untuk testing
        if page == 1:
          url = "https://fashion-studio.dicoding.dev"
        else:
          url = f"https://fashion-studio.dicoding.dev/page{page}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"[ERROR] Gagal mengambil halaman {page}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        product_cards = soup.find_all('div', class_='collection-card')

        if not product_cards:
            print(f"[INFO] Tidak ada produk pada halaman {page}.")
            break

        timestamp_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for product in product_cards:
            try:
                title = product.find('h3', class_='product-title').text.strip() if product.find('h3', class_='product-title') else 'N/A'
                price = product.find('span', class_='price').text.strip() if product.find('span', class_='price') else 'N/A'
                rating = product.find('p', style="font-size: 14px; color: #777;").text.strip().replace('Rating: ', '') if product.find('p', style="font-size: 14px; color: #777;") else 'N/A'
                color = product.find('p', string=lambda text: 'Color' in text if text else False).text.strip().replace('Color: ', '') if product.find('p', string=lambda text: 'Color' in text if text else False) else 'N/A'
                size = product.find('p', string=lambda text: 'Size' in text if text else False).text.strip().replace('Size: ', '') if product.find('p', string=lambda text: 'Size' in text if text else False) else 'N/A'
                gender = product.find('p', string=lambda text: 'Gender' in text if text else False).text.strip().replace('Gender: ', '') if product.find('p', string=lambda text: 'Gender' in text if text else False) else 'N/A'

                product_data.append({
                    'Title': title,
                    'Price': price,
                    'Rating': rating,
                    'Color': color,
                    'Size': size,
                    'Gender': gender,
                    'Timestamp': timestamp_now
                })
            except Exception as e:
                print(f"[WARNING] Gagal parsing produk di halaman {page}: {e}")
                continue

        time.sleep(1)

    return pd.DataFrame(product_data)

if __name__ == "__main__":
    df = extract_data()
    df.to_csv("extracted_product_data.csv", index=False)
    print(f"Total produk yang diambil: {len(df)}")
