from django import forms


class FilterForm(forms.Form):
    curved = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"type": "checkbox", "class": "curved"}),
    )
    smart = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"type": "checkbox", "class": "smart"}),
    )

    country = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={"type": "checkbox", "class": "countryFilter"}
        ),
    )
