from django.contrib import admin
from .models import TaxRule, DiscountRule

admin.site.register(TaxRule)
admin.site.register(DiscountRule)
