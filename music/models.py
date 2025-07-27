from django.db import models
from django.utils.translation import gettext as _

class Music(models.Model):

    CATEGOREY_TYPE = (
        ('foreign' , 'خارجی'),
        ('old' , 'قدیمی'),
        ('remix' , 'ریمیکس'),
        ('rap' , 'رپ'),
        ('pop' , 'پاپ'),
    )

    music_name = models.CharField(("نام موسیقی"),max_length=250)
    artist_name = models.CharField(("نام خواننده"),max_length=250)
    label = models.ImageField(("پوستر موسیقی"),upload_to='image/', null=True, blank=True)
    music_file = models.FileField(("فایل موسیقی"),upload_to='audio/', null=True, blank=True)
    categorey = models.CharField(("دسته بندی"),max_length=20, choices=CATEGOREY_TYPE, default='foreign')

    def __str__(self):
        return self.music_name

