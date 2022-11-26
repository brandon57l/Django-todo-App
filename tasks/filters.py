import django_filters 
from django_filters import CharFilter
from django import forms
from .models import *

class TaskFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', widget= forms.TextInput(attrs={'placeholder':'Search...'}))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created']