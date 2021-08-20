from django.contrib import admin
from main.models import Account, Category, Record

class AccountAdmin(admin.ModelAdmin):
    list_display = ['title','account_balance']

class RecordAdmin(admin.ModelAdmin):
    list_display = ['date','category','item','value','account','comment']
    list_filter = ['category','account']

admin.site.register(Account, AccountAdmin)
admin.site.register(Category)
admin.site.register(Record, RecordAdmin)
