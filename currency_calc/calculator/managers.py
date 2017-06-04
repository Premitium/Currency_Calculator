from django.db import models

class CurrencyManager(models.Manager):
    def delete_everything(self):
        return self.all().delete()

    def get_currency_sign_and_bgn_to_value(self, db_id):
        return self.all().filter(id=db_id).values_list('currency_sign','bgn_to_currency').first()

    def get_currency_signs(self):
        return self.all().values_list('currency_sign','currency_name')
