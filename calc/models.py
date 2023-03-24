from django.contrib.auth.models import User
from django.db import models


class TypeVariable(models.Model):
    TYPE_VAR = (
        ('VARIABLE', 'Variable'),
        ('EXPRESSION', 'Expression'),
        ('STRING', 'String'),
        ('PROGRAM', 'Program'),
    )
    type_var = models.CharField('Type of Variable', max_length=10, choices=TYPE_VAR)
    description = models.TextField('Description', max_length=80)

    def __str__(self):
        return self.type_var


class Variable(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, default='MarcioSmall'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name_var = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    type_var = models.ForeignKey(TypeVariable, on_delete=models.SET_NULL, null=True, blank=True,
        default='Variable',
    )
    value_var = models.FloatField()
    exp_var = models.TextField()
    string_var = models.CharField(max_length=80)
    money = models.BooleanField(default=False)
    save_value_with_result = models.BooleanField(default=True)
    expression_recursive = models.BooleanField(default=True)
    expression_is_html = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)



