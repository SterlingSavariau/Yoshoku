from django import forms

class CustomSignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, 
        label='First Name',
        widget=forms.TextInput(
            attrs={"placeholder": ("First name"), "autocomplete": "First name"}
        ),
    )

    last_name = forms.CharField(
        max_length=30, 
        label='Last Name',
        widget=forms.TextInput(
            attrs={"placeholder": ("Last name"), "autocomplete": "Last name"}
        ),
        )
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user