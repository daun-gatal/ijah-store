# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BarangKeluar(models.Model):
    waktu_field = models.DateTimeField(db_column='Waktu ', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sku = models.TextField(db_column='SKU', blank=True, null=True)  # Field name made lowercase.
    nama_barang = models.TextField(db_column='Nama Barang', blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jumlah_keluar = models.BigIntegerField(db_column='Jumlah Keluar', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    harga_jual = models.FloatField(db_column='Harga Jual', blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    catatan = models.TextField(db_column='Catatan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True


class BarangMasuk(models.Model):
    waktu_field = models.DateTimeField(db_column='Waktu ', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sku = models.TextField(db_column='SKU', blank=True, null=True)  # Field name made lowercase.
    nama_barang = models.TextField(db_column='Nama Barang', blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jumlah_pemesanan = models.BigIntegerField(db_column='Jumlah Pemesanan', blank=True,
                                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jumlah_diterima = models.BigIntegerField(db_column='Jumlah Diterima', blank=True,
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    harga_beli_field = models.FloatField(db_column='Harga Beli ', blank=True,
                                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    nomer_kwitansi = models.TextField(db_column='Nomer Kwitansi', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catatan = models.TextField(db_column='Catatan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True


class JumlahBarang(models.Model):
    sku = models.TextField(db_column='SKU', blank=False, primary_key=True, unique=True)  # Field name made lowercase.
    nama_item = models.TextField(db_column='Nama Item', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jumlah_sekarang = models.BigIntegerField(db_column='Jumlah Sekarang', blank=True,
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True


class LaporanNilaiBarang(models.Model):
    sku = models.TextField(db_column='SKU', blank=True, null=True)  # Field name made lowercase.
    nama_item = models.TextField(db_column='Nama Item', blank=True, null=True)  # Field name made lowercase.
    jumlah = models.BigIntegerField(db_column='Jumlah', blank=True,
                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rata_harga_beli = models.FloatField(db_column='Rata-Rata Harga Beli', blank=True,
                                             null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True


class LaporanPenjualan(models.Model):
    id_pesanan = models.TextField(db_column='ID Pesanan', blank=True, primary_key=True,
                                  unique=True)  # Field name made lowercase.
    waktu_field = models.DateTimeField(db_column='Waktu ', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sku = models.TextField(db_column='SKU', blank=True, null=True)  # Field name made lowercase.
    nama_barang = models.TextField(db_column='Nama Barang', blank=True, null=True)  # Field name made lowercase.
    jumlah = models.BigIntegerField(db_column='Jumlah', blank=True, null=True)  # Field name made lowercase.
    harga_jual = models.FloatField(db_column='Harga Jual', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    harga_beli = models.FloatField(db_column='Harga Beli', blank=True, null=True)  # Field name made lowercase.
    laba = models.FloatField(db_column='Laba', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
