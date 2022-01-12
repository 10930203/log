from django.db import models

# Create your models here.

class person(models.Model):
    TITLE_OPTIONS = [
    (0, '待處理'),
    (1, '處理中'),
    (2, '已結案'),
    (3, '已結案'),
    ]


    borrower = models.CharField('借用人', max_length=30)

    title = models.IntegerField(
              '身分', 
              default=0, 
              choices=TITLE_OPTIONS
           )

    