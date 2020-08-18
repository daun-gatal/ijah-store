import requests
import pandas as pd

data = pd.read_excel('source.xlsx', sheet_name='Catatan Jumlah Barang')


def product():
    for i in range(len(data)):
        requests.post(
            'http://127.0.0.1:8000/api/v1/products/',
            {
                'sku': data['SKU'][i],
                'nama_item': data['Nama Item'][i],
                'jumlah_sekarang': data['Jumlah Sekarang'][i]
            }
        )

