from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3, unique=True)

    # def __str__(self):
    #     return self.code  # Display the currency code

class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='base_currency')
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='target_currency')
    rate = models.FloatField()

    # def __str__(self):
    #     return f"{self.base_currency.code} to {self.target_currency.code} : {self.rate}"
