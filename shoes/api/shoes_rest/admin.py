from django.contrib import admin
from .models import BinVO, Shoe

@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    pass

@admin.register(BinVO)
class BinVOAdmin(admin.ModelAdmin):
    pass

# Register your models here.
