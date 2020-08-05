from django import forms
from django.forms import DateInput

from webapp.models import Status, Task_type, STATUS_CHOICE, TYPE_CHOICE


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Заголовок', widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(max_length=3000, required=True, label='Описание', widget=forms.Textarea(attrs={'class': "form-control"}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус', empty_label=None,
                                    widget=forms.Select(attrs={'class': "form-control"}))
    type_task = forms.ModelChoiceField(queryset=Task_type.objects.all(), required=True, label='Тип', empty_label=None,
                                       widget=forms.Select(attrs={'class': "form-control"}))