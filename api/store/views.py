from rest_framework import viewsets
from .serializers import JumlahBarangSerializer, BarangMasukSerializer, \
    BarangKeluarSerializer, LaporanNilaiBarangSerializer, LaporanPenjualanSerializer
from .models import JumlahBarang, BarangMasuk, BarangKeluar, \
    LaporanNilaiBarang, LaporanPenjualan
from rest_framework.renderers import JSONRenderer
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer


# Create your views here.

class JumlahBarangViewSet(viewsets.ModelViewSet):
    queryset = JumlahBarang.objects.all().order_by('sku')
    serializer_class = JumlahBarangSerializer
    renderer_classes = (JSONRenderer, )
    filterset_fields = ('sku',)


class BarangMasukViewSet(viewsets.ModelViewSet):
    queryset = BarangMasuk.objects.all().order_by('sku')
    serializer_class = BarangMasukSerializer
    renderer_classes = (JSONRenderer, )
    filterset_fields = ('sku', 'nomer_kwitansi',)


class BarangKeluarViewSet(viewsets.ModelViewSet):
    queryset = BarangKeluar.objects.all().order_by('sku')
    serializer_class = BarangKeluarSerializer
    renderer_classes = (JSONRenderer,)
    filterset_fields = ('sku',)


class LaporanNilaiBarangViewset(viewsets.ModelViewSet):
    queryset = LaporanNilaiBarang.objects.all().order_by('sku')
    serializer_class = LaporanNilaiBarangSerializer
    renderer_classes = (JSONRenderer, )
    filterset_fields = ('sku',)


class LaporanPenjualanViewset(viewsets.ModelViewSet):
    queryset = LaporanPenjualan.objects.all().order_by('sku')
    serializer_class = LaporanPenjualanSerializer
    renderer_classes = (JSONRenderer, )
    filterset_fields = ('sku',)


class DownloadLaporanNilaiBarangViewset(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    queryset = LaporanNilaiBarang.objects.all().order_by('sku')
    serializer_class = LaporanNilaiBarangSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'report_products.xlsx'


class DownloadLaporanPenjualanViewset(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    queryset = LaporanPenjualan.objects.all().order_by('sku')
    serializer_class = LaporanPenjualanSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'report_sales.xlsx'
