from django.db import models

# Create your models here.
class Expenses(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"

    class Meta:
        verbose_name_plural = "Expenses"
