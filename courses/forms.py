from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control me-2',
        'type': 'search',
        'placeholder': 'Назва курсу',
        'aria-label': 'Назва курсу'
    }))
