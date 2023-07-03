from .models import UsuarioPersonalizado
from django.contrib.auth.models import User

class AutenticacionPorCorreo:
    """
    Custom authentication backend.

    Allows users to log in using their email address.
    """

    def authenticate(self, request, correo, password):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        try:
            user = UsuarioPersonalizado.objects.get(correo=correo)
            if user.verificar_contrasena(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return UsuarioPersonalizado.objects.get(id=user_id)
        except User.DoesNotExist:
            return None


