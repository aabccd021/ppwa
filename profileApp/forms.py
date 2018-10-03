from django import forms


class JadwalForm(forms.Form):
    hari = forms.MultipleChoiceField(
        label='hari',
        choices=(
            ("senin", "cape"),
            ("monday", "lelah")),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                # 'class': 'form-control',
                'placeholder': "Masukkan kategori"
            }))

    tanggal = forms.DateField(
        label='tanggal',
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'form-control',
                'placeholder': 'Pilih tanggal'
            }))

    jam = forms.TimeField(
        label='Waktu',
        widget=forms.TimeInput(
            format='%I:%M',
            attrs={
                'class': 'form-control',
                'placeholder': 'Pilih waktu'
            }))

    nama = forms.CharField(
        label='Nama',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Masukkan nama"
            }))

    tempat = forms.CharField(
        label='tempat',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Masukkan tempat"
            }))

    kategori = forms.MultipleChoiceField(
        label='Kategori',
        choices=(
            ("kategoria", "catA"),
            ("kategorin", "catN")),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                # 'class': 'form-control',
                'placeholder': "Masukkan kategori"
            }))


class NameForm(forms.Form):
    name = forms.CharField(
        label='Nama',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Masukkan nama"
            }))

    date = forms.DateField(
        label='TTL',
        widget=forms.DateInput(
            format=('%d-%m-%Y'),
            attrs={
                'class': 'form-control',
                'placeholder': 'Pilih tanggal'
            }))

    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Masukkan email"
            }))

    username = forms.CharField(
        max_length=20,
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Masukkan username"
            }))

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Masukkan password"
            }
        )
    )

    password_confirm = forms.CharField(
        label='Konfirmasi Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Masukkan kembali password"
            }
        )
    )