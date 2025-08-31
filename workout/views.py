from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Workout, Muscle, Category, Tool, Gender 

# دکوراتور login_required را به view اصلی اضافه می‌کنیم که بهتر است
# @csrf_exempt
# def get_workouts_ajax(request): ...
# کد بالا خیلی امن نیست. بهتر است csrf را در فرانت‌اند مدیریت کنید.
# اما فعلاً برای سادگی آن را نگه می‌داریم.

@csrf_exempt
def get_workouts_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'unauthenticated'}, status=401)

    if request.method == 'POST':
        # 1. گرفتن لیست فیلترها با getlist (برای دریافت چند مقدار)
        gender_names = request.POST.getlist('gender')
        goal_names = request.POST.getlist('goal')
        muscle_names = request.POST.getlist('muscle')
        equipment_names = request.POST.getlist('equipment')

        # شروع کوئری با تمام تمرینات
        workouts = Workout.objects.all()

        # 2. اعمال فیلترها به صورت داینامیک و صحیح
        if gender_names:
            workouts = workouts.filter(genders__name__in=gender_names)
        if goal_names:
            workouts = workouts.filter(categories__name__in=goal_names)
        if muscle_names:
            workouts = workouts.filter(muscles__name__in=muscle_names)
        if equipment_names:
            workouts = workouts.filter(tools__name__in=equipment_names)

        # 3. استفاده از distinct برای جلوگیری از نتایج تکراری
        workouts = workouts.distinct()

        data = []
        for w in workouts:
            data.append({
                'title': w.title,
                'discription': w.discription,
                'stage1': w.stage1,
                'stage2': w.stage2,
                'stage3': w.stage3,
                'stage4': w.stage4,
                'stage5': w.stage5,
                'stage6': w.stage6,
                'stage7': w.stage7,
                'stage8': w.stage8,
                'stage9': w.stage9,
                'stage10': w.stage10,
                # 4. خواندن اطلاعات از مدل‌های مرتبط به صورت لیست
                'muscles': [muscle.name for muscle in w.muscles.all()],
                'categories': [category.name for category in w.categories.all()],
                'tools': [tool.name for tool in w.tools.all()],
                'genders': [gender.name for gender in w.genders.all()],
                'video_url': w.video.url if w.video else None
            })

        return JsonResponse({'results': data})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def workout_list(request):
    workout_list = Workout.objects.all()
    
    # ارسال لیست کامل گزینه‌ها به تمپلیت برای استفاده در فیلترها
    context = {
        'workouts': workout_list,
        'all_muscles': Muscle.objects.all(),
        'all_categories': Category.objects.all(),
        'all_tools': Tool.objects.all(),
        'all_genders': Gender.objects.all(),
        'is_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else ''
    }
    return render(request, "workout/workout.html", context)