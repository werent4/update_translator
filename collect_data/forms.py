from django import forms

class TranslationForm(forms.Form):
    english_text = forms.CharField(widget=forms.Textarea, label='English')
    lithuanian_text = forms.CharField(widget=forms.Textarea, label='Lithuanian')
