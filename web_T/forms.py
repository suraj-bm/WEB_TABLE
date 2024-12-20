from django import forms
from .models import Timetable

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['day_of_week', 'start_time', 'end_time', 'course_code', 'course_name', 'room', 'instructor', 'is_break', 
                  'time_08_00_09_00', 'time_09_00_10_00', 'time_10_00_11_00', 'time_11_00_12_00', 'time_12_00_13_00', 
                  'time_13_00_14_00', 'time_14_00_15_00', 'time_15_00_16_00']  # include time slots if needed
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:
            if start_time >= end_time:
                raise forms.ValidationError("End time must be later than start time.")
        return cleaned_data
