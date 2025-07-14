from django import forms
from .models import Testimonial


class TestimonialModelForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = [
            'student_name',
            'content',

        ]
        widgets = {
            'student_name': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
