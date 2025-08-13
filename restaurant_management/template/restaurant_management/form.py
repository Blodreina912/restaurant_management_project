from django import froms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['comment']
        widgets={
            'comment': forms.Textarea(attrs={'rows': 4,'placeholder': 'Enter your feedback here....'}),
        }
        class ContactForm(forms.ModelForm):
            class Meta:
                model= ContactFormfields=['name','email']
                widgets= {
                    'name': form.TextInput(attrs={'placeholder': 'Your Name'}),
                    'email': forms.EmailInput(attrs={'placeholder': 'Your Email Address'}),
                }