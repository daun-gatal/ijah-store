from django.contrib import admin
from .models import JumlahBarang, BarangMasuk, BarangKeluar

# Register your models here.
admin.site.register(JumlahBarang)
admin.site.register(BarangMasuk)
admin.site.register(BarangKeluar)