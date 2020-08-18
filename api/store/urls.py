from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'products', views.JumlahBarangViewSet, 'products')
router.register(r'product_in', views.BarangMasukViewSet, 'product_in')
router.register(r'product_out', views.BarangKeluarViewSet, 'product_out')
router.register(r'report_products', views.LaporanNilaiBarangViewset, 'report_products')
router.register(r'report_sales', views.LaporanPenjualanViewset, 'report_sales')
router.register(r'report_products/download/', views.DownloadLaporanNilaiBarangViewset, 'download_products')
router.register(r'report_sales/download/', views.DownloadLaporanPenjualanViewset, 'download_sales')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))]