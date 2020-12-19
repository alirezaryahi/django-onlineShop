from django import forms


class order_form(forms.Form):
    product_id = forms.CharField(
        widget=forms.HiddenInput()
    )
    product_title = forms.CharField(
        widget=forms.HiddenInput()
    )
