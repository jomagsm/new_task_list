from django import forms
from django.forms import DateInput

from webapp.models import Status, Task_type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Заголовок', widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(max_length=3000, required=True, label='Описание', widget=forms.Textarea(attrs={'class': "form-control"}))
    status = forms.ChoiceField(choices=Status, required=True,  label='Статус', widget=forms.Select(attrs={'class': "form-control"}))
    type_task = forms.ChoiceField(choices=Task_type, required=True, label='Тип', widget=forms.Select(attrs={'class': "form-control"}))
    create_at = forms.DateField(required=False, label=' Дата выполнения', widget=DateInput(attrs={'class': "form-control", 'type': 'date'}))
