from django.db import models


class TaxRule(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"
class DiscountRule(models.Model):

    DISCOUNT_TYPES = [
        ('fixed', 'Fixed'),
        ('percentage', 'Percentage'),
    ]

    APPLIES_TO = [
        ('product', 'Product'),
        ('subscription', 'Subscription'),
    ]

    name = models.CharField(max_length=100)

    discount_type = models.CharField(
        max_length=20,
        choices=DISCOUNT_TYPES
    )

    value = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    minimum_purchase = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    minimum_quantity = models.PositiveIntegerField(default=1)

    start_date = models.DateField()
    end_date = models.DateField()

    usage_limit = models.PositiveIntegerField()
    times_used = models.PositiveIntegerField(default=0)

    applies_to = models.CharField(
        max_length=20,
        choices=APPLIES_TO
    )

    def __str__(self):
        return self.name
