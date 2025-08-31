from django.db import models
from django.utils.translation import gettext as _



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





class Muscle(models.Model):
    name = models.CharField("نام عضله", max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField("دسته بندی", max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField("ابزار", max_length=100, unique=True)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField("جنسیت", max_length=100, unique=True)
    
    def __str__(self):
        return self.name



class Workout(models.Model):
    title = models.CharField(_("نام تمرین"), max_length=250)
    discription = models.TextField(_("توضیحات"), null=True, blank=True)
    stage1 = models.TextField(_("مرحله 1"), null=True, blank=True)
    stage2 = models.TextField(_("مرحله 2"), null=True, blank=True)
    stage3 = models.TextField(_("مرحله 3"), null=True, blank=True)
    stage4 = models.TextField(_("مرحله 4"), null=True, blank=True)
    stage5 = models.TextField(_("مرحله 5"), null=True, blank=True)
    stage6 = models.TextField(_("مرحله 6"), null=True, blank=True)
    stage7 = models.TextField(_("مرحله 7"), null=True, blank=True)
    stage8 = models.TextField(_("مرحله 8"), null=True, blank=True)
    stage9 = models.TextField(_("مرحله 9"), null=True, blank=True)
    stage10 = models.TextField(_("مرحله 10"), null=True, blank=True)
    video = models.FileField(_("ویدئو تمرین"), upload_to='training videos/', null=True, blank=True)

    muscles = models.ManyToManyField(Muscle, verbose_name=_("عضلات هدف"))
    categories = models.ManyToManyField(Category, verbose_name=_("دسته بندی تمرین"))
    tools = models.ManyToManyField(Tool, verbose_name=_("ابزارها"))
    genders = models.ManyToManyField(Gender, verbose_name=_("جنسیت"))

    def __str__(self):
        return self.title



