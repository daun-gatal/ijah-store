import requests
import pandas as pd

data = pd.read_excel('source.xlsx', sheet_name='Catatan Barang Masuk')


def product_in():
    for i in range(len(data)):
        requests.post(
            'http://127.0.0.1:8000/api/v1/product_in/',
            {
                'waktu_field': data['Waktu'][i],
                'sku': data['SKU'][i],
                'nama_barang': data['Nama Barang'][i],
                'jumlah_pemesanan': data['Jumlah Pemesanan'][i],
                'jumlah_diterima': data['Jumlah Diterima'][i],
                'harga_beli_field': data['Harga Beli'][i],
                'total': data['Total'][i],
                'nomer_kwitansi': data['Nomer Kwitansi'][i],
                'catatan': data['Catatan'][i]
            }
        )

