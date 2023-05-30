import datetime

from django.db import models

# Create your models here.


class Technology(models.Model):
    technology_text = models.CharField(max_length=200)
    begining_date = models.DateTimeField("date published")
    def __str__(self):
        return self.technology_text
    def was_published_resently(self):
        return self.begining_date >= timezone.now() - datetime.timedelta(days=1)

class Progress(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=200)
    progress = models.IntegerField(default=0)
    def __str__(self):
        return self.note_text