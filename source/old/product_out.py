from db.db_conn import connect_db
import pandas as pd
from sqlalchemy.types import Integer, String, DateTime, Numeric

conn = connect_db()
data = pd.read_excel('source.xlsx', sheet_name='Catatan Barang Keluar')
table_name = 'barang_keluar'


def product_out():
    data.to_sql(
        table_name,
        conn,
        if_exists='replace',
        chunksize=500,
        index=True,
        index_label='Id',
        dtype={
            'waktu': DateTime(),
            'sku': String(1000),
            'nama_barang': String(1000),
            'jumlah_keluar': Integer,
            'harga_jual': Numeric(),
            'total': Numeric(),
            'catatan': String(1000)
        }
    )

