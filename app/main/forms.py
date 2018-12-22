from django import forms
from . import models
import bootstrap_datepicker_plus as datetimepicker


class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = (
            'title',
            'place',
            'theme',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            )
        widgets = {
            'start_date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                attrs={'readonly': 'true'},
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            ).start_of('期間'),
            'start_time': datetimepicker.TimePickerInput(
                format='%H:%M',
                attrs={'readonly': 'true'},
                options={
                    'locale': 'ja',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            ),
            'end_date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                attrs={'readonly': 'true'},
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            ),
            'end_time': datetimepicker.TimePickerInput(
                format='%H:%M',
                attrs={'readonly': 'true'},
                options={
                    'locale': 'ja',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            ).end_of('期間'),
        }

# ―――――――――――――――――――
class ShincyokuForm(forms.ModelForm):
    class Meta:
        model = models.Shincyoku
        fields = (
            'snck',
            'progress',
            )
