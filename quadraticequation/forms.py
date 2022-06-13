from django import forms
from django.core.exceptions import ValidationError

class EquationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(EquationForm, self).__init__(*args, **kwargs)

        def create_field(field_id):
            field = forms.FloatField()
            field.widget.attrs.update({'class': 'qe-input', 'id': field_id})
            return field

        self.fields.update(dict(
            a=create_field('a'),
            b=create_field('b'),
            c=create_field('c'),
        ))

    def clean_field(self, cleaned_data, field):
        data = cleaned_data[field]
        try:
            data = float(data)
            return data
        except:
            raise ValidationError(f'Неверное значение {field}, требуется ввести число')

    def clean_a(self):
        return self.clean_field(self.cleaned_data, 'a')

    def clean_b(self):
        return self.clean_field(self.cleaned_data, 'b')

    def clean_c(self):
        return self.clean_field(self.cleaned_data, 'c')