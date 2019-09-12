from django.db import models

class IssueDetails(models.Model):
	title = models.CharField(max_length=100)
	issue = models.CharField(max_length=500)
	solution = models.CharField(max_length=500)

