from django.db import models
from django.utils.translation import gettext as _

class Workout (models.Model):

    MUSCLE_TYPE = (
        ('shoulder' , 'شانه'),
        ('chest' , 'سینه'),
        ('back' , 'پشت'),
        ('hand' , 'دست'),
        ('armpit' , 'زیربغل'),       
        ('abdominal and side' , 'شکم و پهلو'),
        ('leg' , 'پا'),
        ('calf' , 'ساق پا'),

        
    )

    CATEGOREY_TYPE = (
        ('hypertrophy' , 'افزایش حجم'),
        ('weight loss' , 'کاهش وزن'),
        ('strength training' , 'افزایش قدرت'),
    )

    TOOLS_TYPE = (
        ('bodyweight' , 'وزن بدن'),
        ('dumbbells' , 'دمبل'),
        ('halter and plate' , 'هالتر و صفحه'),
        ('machine' , 'دستگاه'),
        ('cable' , 'سیمکش'),
        ('smith' , 'دستگاه اسمیت'),
        ('band' , 'کش ورزشی'),
        ('medicine ball' , 'توپ'),
        ('kettlebells' , 'دمبل روسی'),
    )


    GENDER_TYPE = (
        ('male' , 'مرد'),
        ('female' , 'زن'),
    )

    title = models.CharField((" نام تمرین "),max_length=250)
    discription = models.TextField(("توضیحات"))
    muscle = models.CharField((" عضله هدف "),max_length=20, choices=MUSCLE_TYPE, default='shoulder')
    categorey = models.CharField((" دسته بندی تمرین "),max_length=20, choices=CATEGOREY_TYPE, default='hypertrophy')
    tools = models.CharField(("ابزار ها"), choices=TOOLS_TYPE, default='bodyweight')
    gender = models.CharField((" جنسیت "),max_length=20, choices=GENDER_TYPE, default='male')
    video = models.FileField((" ویدئو تمرین "),upload_to='training videos/', null=True, blank=True)

    def __str__(self):
        return self.title

