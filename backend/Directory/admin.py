from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'department', 'office', 'office_phone', 'mobile_phone', 'level', 'leader', 'created_at', 'updated_at')
    search_fields = ('name', 'position', 'department')  # 可搜索的字段
    list_filter = ('level', 'department')  # 可过滤的字段
