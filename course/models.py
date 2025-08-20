from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

class Course(models.Model):


    course_name = models.CharField(("نام دوره"),max_length=30, null=True, blank=True)
    short_discription = models.CharField(("توضیحات کوتاه "),max_length=100,null=True, blank=True)
    long_discription = RichTextField((" توضیحات بلند"),max_length=15000,null=True, blank=True)
    start_at = models.DateField(("تاریخ شروع "),null=True, blank=True)
    duration = models.PositiveIntegerField(("مدت زمان دوره "),help_text="مدت زمان دوره به ساعت",null=True, blank=True)
    course_price = models.PositiveIntegerField(("قیمت "),help_text="قیمت دوره به تومان",null=True, blank=True)
    course_image1 = models.ImageField(("عکس اول"),upload_to='image/',null=True, blank=True)
    course_image2 = models.ImageField(("عکس دوم"),upload_to='image/',null=True, blank=True)
    course_image3 = models.ImageField(("عکس سوم"),upload_to='image/',null=True, blank=True)
    course_lable = models.ImageField((" لیبل دوره"),upload_to='image/',null=True, blank=True)
    

    def __str__(self):
        return self.course_name