from django.contrib.auth.models import User
from django.db import models


class Variable(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name_var = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=80)
    value_var = models.FloatField()
    exp_var = models.TextField()
    string_var = models.CharField(max_length=80)
    money = models.BooleanField(default=False)
    save_value_with_result = models.BooleanField(default=True)
    exp_recursive = models.BooleanField(default=True)
    exp_is_html = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
