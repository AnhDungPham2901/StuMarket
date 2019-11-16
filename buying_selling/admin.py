from django.contrib import admin

# Register your models here.
from .models import DangBan,DangMua
class PostAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['product_name', 'description']
  

admin.site.register(DangBan,PostAdmin)
admin.site.register(DangMua,PostAdmin)