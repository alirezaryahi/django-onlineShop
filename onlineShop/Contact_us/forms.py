from django import forms


class Contact_form(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'عنوان ...', 'class': 'input1'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل ...', 'class': 'input1'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن پیام ...', 'class': 'input1'}))
