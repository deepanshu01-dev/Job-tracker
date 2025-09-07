from . import views
from django.urls import path

urlpatterns = [
    path('add_jobs/', views.add_jobs, name='add_jobs' ),
    path('job_list/', views.job_list, name='job_list'),
    path('update_status/<int:job_id>/', views.update_status, name='update_status'),
    path('update_job/<int:job_id>/', views.update_job, name='update_job'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
]
