from django.shortcuts import render, redirect
from .models import Schedule, Lesson


def calendar(request):
    schedule: list = list(Schedule.objects.all().order_by('order'))
    context = {
        'lessons': schedule,
    }
    return render(request, 'calendar/calendar.html', context)


def edit_schedule(request):
    data = request.POST
    for key in data.keys():
        if key != 'csrfmiddlewaretoken':
            lesson = Lesson.objects.get(id=int(key))
            lesson.meet_link = data.get(key)
            lesson.save()
    return redirect('calendar')
