import requests
import pandas as pd

data = pd.read_excel('source.xlsx', sheet_name='Laporan Penjualan', header=9)


def report_sales():
    for i in range(len(data)):
        requests.post(
            'http://127.0.0.1:8000/api/v1/report_sales/',
            {
                'id_pesanan': data['ID Pesanan'][i],
                'waktu_field': data['Waktu'][i],
                'sku': data['SKU'][i],
                'nama_barang': data['Nama Barang'][i],
                'jumlah': data['Jumlah'][i],
                'harga_jual': data['Harga Jual'][i],
                'total': data['Total'][i],
                'harga_beli': data['Harga Beli'][i],
                'laba': data['Laba'][i],
            }
        )
