from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
  status_choices = [
    ('Bookmarked', 'Bookmarked'),
    ('Applying', 'Applying'),
    ('Applied', 'Applied'),
    ('Interviewing', 'Interviewing'),
    ('Negotiating', 'Negotiating'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
  ]
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs', null=True, blank=True)
  title = models.CharField(max_length=200, null=False)
  company = models.CharField(max_length=200, null=False)
  location = models.CharField(max_length=200, null=False, default='Remote')
  url = models.URLField()
  description = models.TextField(null=True, blank=True, default='No description provided.')
  salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  status = models.CharField(max_length=20, choices=status_choices, default='Bookmarked')
  date_saved = models.DateField(default=timezone.now)

  def __str__(self):
    return f"{self.title} at {self.company}"
  
  

