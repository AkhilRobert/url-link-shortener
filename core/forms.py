from django import forms
from django import forms
import re


class CoreAdminForm(forms.ModelForm):
    def clean(self):
        orginal_url = self.cleaned_data.get("original_url")
        valid = re.match(
            "((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)", orginal_url)

        if not valid:
            raise forms.ValidationError("Invalid Email")
