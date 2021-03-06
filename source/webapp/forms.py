from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Task, Status, Task_type, Project

INVALID_SIMVOLS= '~@#$%^-_(){}'''

# @deconstructible
# class MinLengthValidator(BaseValidator):
#     message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
#     code = 'too_short'
#
#     def compare(self, a, b):
#         return a < b
#
#     def clean(self, x):
#         return len(x)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type_task']
        widgets = {'summary': forms.TextInput(attrs={'class': "form-control"}),
                   'description': forms.Textarea(attrs={'class': "form-control"}),
                   'status': forms.RadioSelect,
                   'type_task': forms.CheckboxSelectMultiple}



    def clean_summary(self):
        errors = []
        summary = self.cleaned_data['summary']
        invalid_sim = 0
        for i in summary:
            if i in INVALID_SIMVOLS:
                invalid_sim += 1
        if invalid_sim > 0:
            errors.append(ValidationError(f'Вы использовали {invalid_sim} раз, недопустимые символы'))
        if len(summary) < 5:
            errors.append(ValidationError(f'Название задач не должны быть короче 5 символов'))
        if errors:
            raise ValidationError(errors)
        return summary


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти",
                             widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'finish_date']
        widgets = {'name': forms.TextInput(attrs={'class': "form-control"}),
                   'description': forms.Textarea(attrs={'class': "form-control"}),
                   'start_date': forms.SelectDateWidget,
                   'finish_date': forms.SelectDateWidget}

class TeamForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['team']
        widgets = {'team': forms.CheckboxSelectMultiple}