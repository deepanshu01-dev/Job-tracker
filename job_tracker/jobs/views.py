from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from .models import Job
from django.db.models import Count
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
@login_required
def add_jobs(request):
    if request.method == 'POST':
       title = request.POST.get('title')
       company = request.POST.get('company')
       location = request.POST.get('location')
       url = request.POST.get('url')
       salary = request.POST.get('salary')
       description = request.POST.get('description')

       Job.objects.create(user=request.user,title=title, company=company, location=location, url=url, salary=salary, description=description)

       return redirect('job_list')

@login_required
def job_list(request):
  jobs = Job.objects.filter(user=request.user)
  status_choices = Job.status_choices
  
  status_counts = Job.objects.filter(user=request.user).values('status').annotate(count=Count('status'))
  status_summary = {
     item['status']: item['count'] for item in status_counts
  }
  return render(request, 'jobs/job_list.html' ,{ 'jobs': jobs,
  'status_choices': status_choices,
  'status_summary': status_summary}
)

@login_required
@require_POST
def update_status(request, job_id):
    try:
        data = json.loads(request.body)
        new_status = data.get('status')
        # Remove user filter for debugging
        job = get_object_or_404(Job, id=job_id, user=request.user) 
        job.status = new_status
        job.save()
        return JsonResponse({'status': job.status})
    except Job.DoesNotExist:
        return JsonResponse({'error': 'Job not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    

def debug_view(request, job_id):
    return HttpResponse(f"Got job_id: {job_id}")

@login_required
def update_job(request, job_id):
      job = get_object_or_404(Job, id=job_id, user=request.user)
      if request.method == 'POST':
         job.title = request.POST.get('title')
         job.company = request.POST.get('company')
         job.location = request.POST.get('location')
         job.url = request.POST.get('url')
         job.salary = request.POST.get('salary')
         job.description = request.POST.get('description')
         job.save()
         return redirect('job_list')
      return render(request, 'jobs/update_job.html', {'job':job})

@login_required
def job_detail(request, job_id):
   job = get_object_or_404(Job, id=job_id, user=request.user)
   return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def delete_job(request, job_id):
    try:
        job = get_object_or_404(Job, id=job_id, user=request.user)
        job.delete()
        return redirect('job_list')
    except Job.DoesNotExist:
        return HttpResponse('Job not found', status=404)
    