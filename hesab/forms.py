from django import forms
from .models import hesabketab
class hesabketabform(forms.ModelForm):
    class Meta:
        model = hesabketab
        fields=['txtTitle','hesabketab_type','amount']
        labeles = {
            'txtTitle':'عنوان',
            'hesabketab_type':'نوع تراکنش',
            'amount':'مبلغ تراکنش'
        }
        widgets = {
            'hesabketab_type':forms.RadioSelect()
        }
