from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    BUG_TYPES = [
        ("graphic", "Graphic"),
        ("text", "Text"),
        ("navigation", "Navigation")
    ]

    bugType = models.CharField(max_length = 12, choices=BUG_TYPES)
    assignedTo = models.CharField(max_length = 34)
   
    REPORT_STATUSES = [
        ("assigned", "Assigned"),
        ("acknowledged", "Acknowledged"),
        ("feedback", "Feedback"),
        ("resolved", "Resolved"),
        ("closed", "Closed")

    ]
    PRIORITIES = [
        ("S", "S"),
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    ]
    priorityLevel = models.CharField(max_length=1, choices=PRIORITIES, default="C")
    status = models.CharField(max_length=12, choices=REPORT_STATUSES, default="assigned")
    summaryTitle = models.CharField(max_length=52)
    bugDescription = models.TextField()
    attachments = models.FileField(upload_to="Media")

    def __str__(self):
        return self.summaryTitle
