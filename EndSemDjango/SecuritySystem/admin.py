from django.contrib import admin
from .models import MEMBERSHIP
# Register your models here.

@admin.register(MEMBERSHIP)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','thumbnails','price','qty']