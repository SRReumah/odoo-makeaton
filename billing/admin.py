from django.contrib import admin
from .models import TaxRule, DiscountRule


@admin.register(TaxRule)
class TaxRuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
    search_fields = ('name',)


@admin.register(DiscountRule)
class DiscountRuleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'discount_type',
        'value',
        'applies_to',
        'usage_limit',
        'times_used',
    )
    search_fields = ('name',)
    list_filter = ('discount_type', 'applies_to')
