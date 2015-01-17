from django.contrib import admin
from workrecords.models import Work

class WorkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['title']}),
        ('详情',            {'fields': ['work_text', 'work_path']}),
        ('备注',            {'fields': ['remarks'], 'classes': ['collapse']}),
        ('提交日期',         {'fields': ['rec_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'work_path', 'rec_date')
    search_fields = ['title', 'work_text', 'remarks']  #设置从哪几项中搜索

admin.site.register(Work, WorkAdmin)

