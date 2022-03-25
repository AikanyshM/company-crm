from dataclasses import fields
from django import forms
from .models import Position, Employee, Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {'birthdate': forms.widgets.DateInput(attrs={'type': 'date'})}