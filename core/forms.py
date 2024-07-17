from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'stock',
            'descripcion',
            'tipo',
            'imagen',
            'vigente',
            'marca',
            'modelo',
            'motor',
            'potencia',
            'traccion',
            'aire_acondicionado',
            'alimentacion',
            'neumaticos',
            'caracteristica_1_titulo',
            'caracteristica_1_descripcion',
            'caracteristica_2_titulo',
            'caracteristica_2_descripcion',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'vigente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'motor': forms.TextInput(attrs={'class': 'form-control'}),
            'potencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'traccion': forms.TextInput(attrs={'class': 'form-control'}),
            'aire_acondicionado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'alimentacion': forms.TextInput(attrs={'class': 'form-control'}),
            'neumaticos': forms.TextInput(attrs={'class': 'form-control'}),
            'caracteristica_1_titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'caracteristica_1_descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'caracteristica_2_titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'caracteristica_2_descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
