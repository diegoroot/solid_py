from django import forms
from .models import User


class ApiCreateUserForm(forms.ModelForm):
    code = forms.CharField(required=True)
    name = forms.CharField(required=True)
    state = forms.CharField(required=True)

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if User.objects.filter(code=code).exists():
            raise forms.ValidationError(
                u'El código de usuario ' + str(code) + u' ya existe, por favor ingrese un código diferente')

        return code

    class Meta:
        model = User
        fields = ('code', 'name', 'state')
