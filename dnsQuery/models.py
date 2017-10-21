from django.db import models
from datetime import datetime

# Create your models here.

class Query(models.Model):
	"""docstring for Query"""
	request = models.CharField(max_length=200)
	response = models.CharField(max_length=200)

	created = models.DateTimeField('created date', default=datetime.now, blank=True)

	def __str__(self):
		# return '{0} - {1}'.format(self.request, self.response)
		return '{0}'.format(self.request)
		