from django.contrib import admin

# Register your models here.
from .models import SsqModel


class SsqModelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('what?', {'fields': ['qiCi']}),
        ('Date information', {'fields': ['kaiJiangRiQi'], 'classes': ['collapse']}),
    ]
    list_display = ('qiCi', 'kaiJiangRiQi', 'was_kaijiangriqi_recently')
    list_filter = ['kaiJiangRiQi']
    search_fields = ['qiCi']


admin.site.register(SsqModel, SsqModelAdmin)
