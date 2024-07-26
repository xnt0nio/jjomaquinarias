from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'tipo',
            'imagen',
            'vigente',
            'marca',
            'modelo',
            'motor',
            'potencia',
            'traccion',
            'alimentacion',
            'neumaticos',
            'caracteristica',
            'equipamiento'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'vigente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'motor': forms.TextInput(attrs={'class': 'form-control'}),
            'potencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'traccion': forms.TextInput(attrs={'class': 'form-control'}),
            'alimentacion': forms.TextInput(attrs={'class': 'form-control'}),
            'neumaticos': forms.TextInput(attrs={'class': 'form-control'}),
            'caracteristica': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'equipamiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }



class MensajeForm(forms.ModelForm):
    class Meta:
        model = mensaje
        fields = ['nombre', 'email', 'telefono', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            'asunto': forms.TextInput(attrs={'placeholder': 'Asunto', 'class': 'asunto-field'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Mensaje'}),
        }
