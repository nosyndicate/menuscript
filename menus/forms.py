import logging
from django import forms

from .models import Dish

logger = logging.getLogger('default')

class DishForm(forms.Form):

    def __init__(self, *args, **kwargs):
        dishes = kwargs.pop('dishes')
        super(DishForm, self).__init__(*args, **kwargs)

        for key in dishes:
            for dish_id in dishes[key]:
                dish = dishes[key][dish_id]
                self.fields[dish] = forms.BooleanField(required=False)
                self.fields[dish].widget.attrs.update({'id' : dish_id})
  