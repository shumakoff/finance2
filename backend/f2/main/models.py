from django.db import models
from djmoney.models.fields import MoneyField


class Account(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    currency = models.CharField(max_length=4)

    def account_balance(self):
        income = self.record_set.filter(value__gt=0).aggregate(models.Sum('value'))['value__sum'] or 0
        expences = self.record_set.filter(value__lt=0).aggregate(models.Sum('value'))['value__sum'] or 0
        return income + expences

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.balance_currency = self.currency
        super(Account, self).save(*args, **kwargs)


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'

class Record(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    value = MoneyField(max_digits=19, decimal_places=8, default_currency='RUB')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return u'%s %s %s %s' % (self.date, self.category, self.item, self.value)


