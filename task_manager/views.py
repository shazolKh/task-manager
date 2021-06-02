from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponseRedirect
from .models import *
from datetime import datetime
from django.contrib import messages


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


@login_required(login_url='login')
def SingleTask(request, pk):
    data = Task.objects.get(id=pk)

    commen = Comment.objects.filter(task_id=pk)
    page = request.GET.get('page', 1)
    paginator = Paginator(commen, 4)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        status = request.POST.get('status')
        additional_info = request.POST.get('additional')
        updated_at = datetime.now()
        updated_by = request.user

        Task.objects.filter(id=pk).update(status=status, additional_info=additional_info, updated_by=updated_by,
                                          updated_at=updated_at)

        messages.success(request, 'Information updated successfully.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'data': data,
        'comments': comments,
    }
    return render(request, 'task_manager/singleTask.html', context)


@login_required(login_url='login')
def DeleteTask(request, pk):
    Task.objects.get(id=pk).delete()
    messages.error(request, 'Task Deleted!!!')
    return redirect('dashboard')


@login_required(login_url='login')
def AddComment(request, pk):
    Comment.objects.create(
        task_id=pk,
        user_id=request.user.pk,
        details=request.POST.get('comment')
    )
    messages.success(request, 'Your Comment Added to this task')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def Additional(request, pk):
    print(pk)
    return JsonResponse({'data': pk})
