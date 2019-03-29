from django.db import models


class Book(models.Model):
    """本モデル"""

    class Meta:
        db_table = 'book'

    title = models.CharField(verbose_name='タイトル', max_length=20)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)

    def __str__(self):
        return self.title
