from db.db_conn import connect_db
import pandas as pd
from sqlalchemy.types import Integer, String

conn = connect_db()
data = pd.read_excel('source.xlsx', sheet_name='Catatan Jumlah Barang')
table_name = 'jumlah_barang'


def all_product():
    data.to_sql(
        table_name,
        conn,
        if_exists='replace',
        chunksize=500,
        index=False,
        dtype={
            'sku': String(1000),
            'nama_item': String(1000),
            'jumlah_sekarang': Integer
        }
    )
