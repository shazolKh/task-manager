from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from .models import *
from datetime import datetime
from django.contrib import messages
from django.db.models import Q


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
    try:
        approval = ApprovalRequest.objects.filter(task_id=pk).first()
    except:
        approval = 0

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

        Task.objects.filter(id=pk).update(
            status='pending',
            additional_info=additional_info,
            updated_by=updated_by,
            updated_at=updated_at
        )

        ApprovalRequest.objects.create(
            task_id=pk,
            user_id=request.user.pk,
            status=status,
        )

        messages.success(request, 'Request Submitted, Please wait for approval!!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'data': data,
        'comments': comments,
        'approval': approval,
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


@login_required(login_url='login')
def Approve(request, pk):
    status = ApprovalRequest.objects.values('status').filter(task_id=pk).first()
    stat = status.get('status')
    Task.objects.filter(id=pk).update(
        status=stat
    )
    ApprovalRequest.objects.filter(task_id=pk).delete()
    messages.success(request, 'Task Status Request has been Approved!!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def AddTask(request):
    if request.method == 'POST':
        Task.objects.create(
            task_name=request.POST.get('name'),
            status=request.POST.get('status'),
            additional_info=request.POST.get('additional')
        )
    return redirect('dashboard')


@login_required(login_url='login')
def Summary(request):
    tasks = Task.objects.order_by('-id').all()

    context = {
        'tasks': tasks,
    }
    return render(request, 'task_manager/summary.html', context)


@login_required(login_url='login')
def Search(request):
    query = request.GET['query']

    task_list = Task.objects.filter(Q(task_name__contains=query) | Q(status__contains=query) |
                                    Q(updated_by__username__contains=query) |
                                    Q(updated_by__first_name__contains=query))

    page = request.GET.get('page', 1)
    paginator = Paginator(task_list, 9)

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        'tasks': tasks,
    }

    return render(request, 'task_manager/search.html', context)


@login_required(login_url='login')
def MainDashboard(request):
    task_list = Task.objects.order_by('-id').all()
    # Total Tasks
    total_tasks = Task.objects.all().count()
    completed = Task.objects.filter(status='complete').count()

    percentage = (completed * 100) / total_tasks

    pending = ApprovalRequest.objects.all().count()

    page = request.GET.get('page', 1)
    paginator = Paginator(task_list, 9)

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        'tasks': tasks,
        'total_task': total_tasks,
        'complete': completed,
        'per': percentage,
        'pending': pending
    }
    return render(request, 'task_manager/mainDashboard.html', context)
