# admin.py

from django.contrib import admin
from .models import Workout, Muscle, Gender, Category, Tool

# فقط مدل‌ها را خیلی ساده ثبت کنید
admin.site.register(Workout)
admin.site.register(Muscle)
admin.site.register(Gender)
admin.site.register(Category)
admin.site.register(Tool)