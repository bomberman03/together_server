from __future__ import unicode_literals

from django.db import models


class User(models.Model):

    student_id = models.CharField(max_length=20)
    department_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Project(models.Model):

    name = models.CharField(max_length=100)
    summary = models.TextField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name


class Task(models.Model):

    project = models.ForeignKey(Project, related_name="tasks")
    user = models.ForeignKey(User, related_name="tasks")
    name = models.CharField(max_length=100)
    summary = models.TextField(max_length=200)
    end_date = models.DateField()

    def __unicode__(self):
        return self.name


class Feed(models.Model):

    task = models.ForeignKey(Task, related_name="feeds")
    user = models.ForeignKey(User, related_name="feeds")
    summary = models.TextField(max_length=200)

    def __unicode__(self):
        return self.name
