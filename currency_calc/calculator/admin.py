from django.core.management import call_command
from functools import update_wrapper
from django.contrib import admin
from .models import Currency
from django.shortcuts import render

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['currency_name','currency_sign','currency_to_bgn','bgn_to_currency']
    class Meta:
        model = Currency

    actions = ['execute_management_command']

    def execute_management_command(self, request, queryset):
        call_command('synccurrency')
        self.message_user(request, "Successfully synced the currency_db.")


# Register your models here.
admin.site.register(Currency, CurrencyAdmin)
