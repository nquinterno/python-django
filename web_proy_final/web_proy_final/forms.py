from django import forms

class cursoFormulario(forms.Form):
    numero_curso = forms.IntegerField()
    tipo_curso = forms.CharField()