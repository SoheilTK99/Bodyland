from django.db import models
from django.utils.translation import gettext as _

class Course(models.Model):


    course_name = models.CharField(("نام دوره"),max_length=30, null=True, blank=True)
    short_discription = models.CharField(("توضیحات کوتاه "),max_length=100,null=True, blank=True)
    long_discription = models.TextField((" توضیحات بلند"),max_length=900,null=True, blank=True)
    start_at = models.DateField(("تاریخ شروع "),null=True, blank=True)
    duration = models.PositiveIntegerField(("مدت زمان دوره "),help_text="مدت زمان دوره به ساعت",null=True, blank=True)
    course_price = models.PositiveIntegerField(("قیمت "),help_text="قیمت دوره به تومان",null=True, blank=True)
    course_image = models.ImageField((" عکس"),upload_to='image/',null=True, blank=True)
    course_lable = models.ImageField((" لیبل دوره"),upload_to='image/',null=True, blank=True)
    

    def __str__(self):
        return self.course_name