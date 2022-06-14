from django import forms
from django.core.exceptions import ValidationError

class ItemForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        item_id = forms.IntegerField()
        item_id.widget.attrs.update({'class': 'hi-input'})
        self.fields.update(dict(item_id=item_id))

    def clean_item_id(self):
        # return self.cleaned_data['item_id']
        item_id = self.cleaned_data['item_id']
        if item_id >= 1 and item_id <= 100:
            return item_id
        else:
            raise ValidationError(f'Неверное значение {item_id}, требуется ввести число от 1 до 100')
