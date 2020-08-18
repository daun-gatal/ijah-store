import requests
import pandas as pd

data = pd.read_excel('source.xlsx', sheet_name='Laporan Nilai Barang', header=7)


def report_products():
    for i in range(len(data)):
        requests.post(
            'http://127.0.0.1:8000/api/v1/report_products/',
            {
                'sku': data['SKU'][i],
                'nama_item': data['Nama Item'][i],
                'jumlah': data['Jumlah'][i],
                'rata_harga_beli': data['Rata-Rata Harga Beli'][i],
                'total': data['Total'][i],
            }
        )

