import requests
import pandas as pd

data = pd.read_excel('source.xlsx', sheet_name='Catatan Barang Keluar')


def product_out():
    for i in range(len(data)):
        requests.post(
            'http://127.0.0.1:8000/api/v1/product_out/',
            {
                'waktu_field': data['Waktu'][i],
                'sku': data['SKU'][i],
                'nama_barang': data['Nama Barang'][i],
                'jumlah_keluar': data['Jumlah Keluar'][i],
                'harga_jual': data['Harga Jual'][i],
                'total': data['Total'][i],
                'catatan': data['Catatan'][i]
            }
        )

