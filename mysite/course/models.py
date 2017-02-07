from django.db import models
from django.conf import settings
import uuid


class Course(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	course_name = models.TextField(primary_key=True)
	course_desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s %s" % (str(self.pk), self.course_name)



