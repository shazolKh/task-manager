from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import *


# Create your views here.

@login_required(login_url='login')
def Dashboard(request):
    task_list = Task.objects.order_by('-id').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(task_list, 8)

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        'tasks': tasks,
    }
    return render(request, 'task_manager/dashboard.html', context)


def Additional(request, pk):
    print(pk)
    return JsonResponse({'data': pk})
