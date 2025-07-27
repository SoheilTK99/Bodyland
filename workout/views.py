from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Workout
from django.contrib.auth.decorators import login_required


@csrf_exempt
def get_workouts_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'unauthenticated'}, status=401)
    if request.method == 'POST':
        gender = request.POST.get('gender')
        goal = request.POST.get('goal')
        muscle = request.POST.get('muscle', '')
        equipment = request.POST.get('equipment', '')

        muscle_list = muscle.split(',') if muscle else []
        equipment_list = equipment.split(',') if equipment else []

        workouts = Workout.objects.filter(
            gender=gender,
            categorey=goal,
            muscle__in=muscle_list,
            tools__in=equipment_list
        )

        data = []
        for w in workouts:
            data.append({
                'title': w.title,
                'description': w.discription,
                'muscle': w.get_muscle_display(),
                'video_url': w.video.url if w.video else None
            })

        return JsonResponse({'results': data})

    return JsonResponse({'error': 'Invalid request'}, status=400)



def workout_list(request):
    workout_list = Workout.objects.all()
    context = {
        'workouts': workout_list,
        'is_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else ''
    }
    return render(request, "workout/workout.html", context)

