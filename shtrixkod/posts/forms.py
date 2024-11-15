from django import forms

from .models import Record


class DateInput(forms.DateInput):
    input_type = "date"


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = (
            "name",
            "marking",
            "amount",
            "weight",
            "volume",
            "add_date",
            "recipient",
            "comment"
        )

        widgets = {
            "name": forms.Textarea(attrs={'rows': 3}),
            "add_date": DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                    }
            ),
            "recipient": forms.Textarea(attrs={'rows': 3}),
            "comment": forms.Textarea(attrs={'rows': 3})
        }


class RecordFormIssueDate(forms.ModelForm):
    class Meta:
        model = Record
        fields = (
            "issue_date",
        )

        widgets = {
            "issue_date": DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                    }
            ),
        }
