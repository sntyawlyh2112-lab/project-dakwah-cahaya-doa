from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class FormDaftar(forms.ModelForm):
    nama_lengkap = forms.CharField(
        max_length=150,
        label="Nama Lengkap"
    )

    password = forms.CharField(
        label="Kata Sandi",
        widget=forms.PasswordInput,
        validators=[validate_password]
    )

    konfirmasi_password = forms.CharField(
        label="Konfirmasi Kata Sandi",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email"]
        labels = {
            "username": "Nama Pengguna",
            "email": "Alamat Email",
        }

    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Email sudah digunakan."
            )

        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        konfirmasi = cleaned_data.get("konfirmasi_password")

        if password and konfirmasi and password != konfirmasi:
            self.add_error(
                "konfirmasi_password",
                "Konfirmasi kata sandi tidak cocok."
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["nama_lengkap"]
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user
