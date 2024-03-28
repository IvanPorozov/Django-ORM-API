from django import forms

from .models import Food


class AddNewElementForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
        widgets = {
            # 'type': forms.Textarea(attrs={'class': "form-select", "size": "3", 'aria-label': "Size 3 select example"}),
        }
