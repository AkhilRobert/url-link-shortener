import re
from django import forms
from .models import CoreModel


class CoreAdminForm(forms.ModelForm):
    def clean(self):
        original_url = self.cleaned_data.get("original_url")
        valid = re.match(
            "((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)", original_url)

        if not valid:
            raise forms.ValidationError("Invalid URL")


class ShrinkURLForm(forms.ModelForm):
    original_url = forms.CharField(label="", required=False)

    def clean_original_url(self):
        original_url = self.cleaned_data.get("original_url")
        valid = re.match(
            "((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)", original_url)

        if not valid:
            raise forms.ValidationError("Invalid URL")

        return original_url

    class Meta:
        model = CoreModel
        fields = ["original_url"]
