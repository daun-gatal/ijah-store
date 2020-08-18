from rest_framework import serializers
from .models import JumlahBarang, BarangKeluar, BarangMasuk, \
    LaporanNilaiBarang, LaporanPenjualan


class JumlahBarangSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JumlahBarang
        fields = (
            'sku',
            'nama_item',
            'jumlah_sekarang',
        )


class BarangMasukSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BarangMasuk
        fields = (
            'id',
            'waktu_field',
            'sku',
            'nama_barang',
            'jumlah_pemesanan',
            'jumlah_diterima',
            'harga_beli_field',
            'total',
            'nomer_kwitansi',
            'catatan',
        )


class BarangKeluarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BarangKeluar
        fields = (
            'id',
            'waktu_field',
            'sku',
            'nama_barang',
            'jumlah_keluar',
            'harga_jual',
            'total',
            'catatan',
        )


class LaporanNilaiBarangSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LaporanNilaiBarang
        fields = (
            'id',
            'sku',
            'nama_item',
            'jumlah',
            'rata_harga_beli',
            'total',
        )


class LaporanPenjualanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LaporanPenjualan
        fields = (
            'id_pesanan',
            'waktu_field',
            'sku',
            'nama_barang',
            'jumlah',
            'harga_jual',
            'total',
            'harga_beli',
            'laba',
        )
