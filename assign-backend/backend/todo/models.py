from django.db import models
class Todo(models.Model):
    catname =  models.CharField(max_length=1000)
    objectname = models.CharField(max_length=1000)
    def _str_(self):
        return self.title