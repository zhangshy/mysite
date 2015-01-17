from django.db import models
from django.utils import timezone

class Work(models.Model):
    now = timezone.now()
    title = models.CharField(max_length=100)
    work_text = models.CharField(max_length=200)
    rec_date = models.DateTimeField('date recorded', default=now)
    work_path = models.CharField(max_length=100)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.work_text
