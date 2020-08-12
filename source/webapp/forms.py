from django import forms
from django.forms import DateInput
from django.core.exceptions import ValidationError
from webapp.models import Task, Status, Task_type
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


def at_least_10(string):
    if len(string) < 10:
        raise ValidationError('Value is too short!')


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


class TaskForm(forms.ModelForm):
    # summary = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    # status = forms.ModelChoiceField(widget=forms.RadioSelect)
    # type_task = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type_task']
        # widgets = {'summary': forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"})),
        #            'description': forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))}
                   # 'status': forms.ModelChoiceField(widget=forms.RadioSelect),
                   # 'type_task': forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple)}


    # summary = forms.CharField(max_length=200, required=True, label='Заголовок', widget=forms.TextInput(attrs={'class': "form-control"}))
    # description = forms.CharField(max_length=3000, required=True, label='Описание',
    #                               widget=forms.Textarea(attrs={'class': "form-control"}),
    #                               validators=[MinLengthValidator(5)])
    # status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус', empty_label=None,
    #                                 widget=forms.RadioSelect)
    # type_task = forms.ModelMultipleChoiceField(queryset=Task_type.objects.all(), required=True, label='Тип', widget=forms.CheckboxSelectMultiple)

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        summary = cleaned_data.get('summary')
        description = cleaned_data.get('description')
        if summary == description:
            errors.append(ValidationError('Text of the summary should not duplicate it"s description!'))
        if errors:
            raise ValidationError(errors)
        return cleaned_data
