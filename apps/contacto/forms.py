from django import forms

class ContactoForm(forms.Form):
    # Campo para el nombre del remitente (máx. 100 caracteres)
    nombre = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Tu Nombre Completo'})
    )
    
    # Campo para el email del remitente (será la dirección de respuesta)
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'tu.correo@ejemplo.com'})
    )
    
    # Campo para el asunto del mensaje
    asunto = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Asunto del Mensaje'})
    )
    
    # Campo para el contenido del mensaje
    mensaje = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Escribe tu mensaje aquí...'})
    )