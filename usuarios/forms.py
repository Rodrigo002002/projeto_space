from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={ 'class':'form-control',
                    'placeholder':'Ex.: João Silva',
                }
        ),
    )
    senha=forms.CharField(
        label="Senha",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={ 'class':'form-control',
                    'placeholder':'Digite sua senha',
            }
        ),
    )