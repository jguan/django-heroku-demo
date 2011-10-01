from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Student(models.Model):
    teacher = models.ForeignKey(Teacher)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

