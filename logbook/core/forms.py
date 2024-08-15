from django import forms
from .models import MaintenanceLog

class MaintenanceLogForm(forms.ModelForm):
    class Meta:
        model = MaintenanceLog
        fields = '__all__'
        widgets = {
            'last_review_date': forms.SelectDateWidget(),
            'general_notes': forms.Textarea(attrs={'rows': 3}),
            'additional_notes': forms.Textarea(attrs={'rows': 3}),
            'pending_tasks': forms.Textarea(attrs={'rows': 3}),
        }
