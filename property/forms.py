from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    predictedprice = forms.IntegerField(widget=forms.HiddenInput,initial=1)
    class Meta:
        model = Property
        fields = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.predictedprice = self.cleaned_data["predictedprice"]
        if commit:
            instance.save()
        return instance