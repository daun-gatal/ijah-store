import pandas as pd

data = pd.read_excel('source.xlsx', sheet_name='Laporan Nilai Barang', header=7)

for i in range(len(data)):
    print({
                'sku': data['SKU'][i],
                'nama_item': data['Nama Item'][i],
                'jumlah': data['Jumlah'][i],
                'rata_harga_beli': data['Rata-Rata Harga Beli'][i],
                'total': data['Total'][i],
            })