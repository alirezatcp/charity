from django.db import models
from django.db.models import Q

from accounts.models import User

class Benefactor(models.Model):
    EXPERIENCE_CHOICES = (
        (0, 'Beginner'),
        (1, 'Medium'),
        (2, 'Expert'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=EXPERIENCE_CHOICES, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default = 0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        queryset = Task.objects.filter(charity__user=user)
        return queryset

    def related_tasks_to_benefactor(self, user):
        queryset = Task.objects.filter(assigned_benefactor__user=user)
        return queryset

    def all_related_tasks_to_user(self, user):
        queryset = Task.objects.filter(Q(state='Pending') | Q(assigned_benefactor__user=user) | Q(charity__user=user))
        return queryset


class Task(models.Model):
    STATE_CHOICES = (
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
    )

    GENDER_LIMIT_CHOISES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(max_length=1, choices=GENDER_LIMIT_CHOISES, blank=True, null=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='P')
    title = models.CharField(max_length=100)

    objects = TaskManager()
