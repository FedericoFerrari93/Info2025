from django.shortcuts import render, redirect # Importamos redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactoForm

def contacto(request):
    """
    Vista para mostrar y procesar el formulario de contacto.
    """
    if request.method == 'POST':
        # 1. Crear instancia del formulario con los datos POST
        form = ContactoForm(request.POST)
        
        # 2. Validar los datos
        if form.is_valid():
            # Obtener datos limpios
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            
            # 3. Construir el contenido del correo
            contenido_email = f"Mensaje de {nombre} ({email}):\n\n{mensaje}"
            
            # 4. Enviar el correo
            try:
                send_mail(
                    subject=asunto,
                    message=contenido_email,
                    from_email=settings.DEFAULT_FROM_EMAIL, # O email si quieres usar el del usuario
                    recipient_list=['tu_correo_destino@ejemplo.com'], # ¡CAMBIA ESTO!
                    fail_silently=False,
                )
                # Opcional: Agregar un mensaje de éxito con messages framework
                # from django.contrib import messages
                # messages.success(request, "Tu mensaje ha sido enviado con éxito.")
                
                # Redirigir a una página de éxito (o a la misma página)
                return redirect('apps.contacto:contacto_gracias') 
            
            except Exception as e:
                # Opcional: Manejar errores de envío
                # messages.error(request, f"Ocurrió un error al enviar el mensaje: {e}")
                pass
    
    else:
        # Si es GET, crear un formulario vacío
        form = ContactoForm()
        
    # Renderizar el template con el formulario
    return render(request, 'contacto/contacto_form.html', {'form': form})

def contacto_gracias(request):
    """
    Vista simple para mostrar un mensaje de agradecimiento.
    """
    return render(request, 'contacto/contacto_gracias.html')
