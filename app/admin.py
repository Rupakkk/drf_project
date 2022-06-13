from django.contrib import admin
from .models import Country,PetroleumProduct,Year,Detail
# Register your models here.
admin.site.register(Country)
admin.site.register(PetroleumProduct)
admin.site.register(Year)
admin.site.register(Detail)
