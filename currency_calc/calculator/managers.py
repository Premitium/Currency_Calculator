from django.db import models

class CurrencyManager(models.Manager):
    def delete_everything(self):
        return self.all().delete()
