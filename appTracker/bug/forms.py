from django import forms
from .models import Bug

class CreateBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['bugType', 'assignedTo', 'priorityLevel', 'status', 'summaryTitle'
                    ,'bugDescription']
        widgets = {
            'bugType': forms.Select(attrs = {
                'class': 'form-control'
            }), 
            'assignedTo': forms.TextInput(attrs = {
                'class': 'form-control'
            }), 
            'priorityLevel': forms.Select(attrs = {
                'class': 'form-control'
            }), 
            'status': forms.Select(attrs = {
                'class': 'form-control'
            }), 
            'summaryTitle': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'bugDescription': forms.Textarea(attrs = {
                'class': 'form-control'
            })

        }
