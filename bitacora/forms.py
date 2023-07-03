from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class XYZ_DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)

class CatMatPeligrosoForm(forms.ModelForm):
    class Meta:
        model = CatMatPeligroso
        fields = [
            "nombre",
            "cretib",
            "descripcion",
             "ficha_seguridad",
             "imagen"
        ]
        help_texts = {
              "nombre": _("Ingresa el nombre del Material peligroso"),
              "cretib": _("Ingresa el cretib del Material peligroso"),
              "descripcion": _("Ingresa la descripcion del Material peligroso"),
              "ficha_seguridad": _("Ingresa la ficha de seguridad del Material peligroso"),
              "imagen": _("Ingresa la imagen del Material peligroso"),
        }
        labels = {
              "nombre": _("Nombre"),
              "cretib": _("Cretib"),
              "descripcion": _("Descripcion"),
              "ficha_seguridad": _("Ficha de seguridad"),
              "imagen": _("Imagen"),
        }

class RegAlmacenForm(forms.ModelForm):
    class Meta:
        model = RegAlmacen
        fields = [
            "lote",
            "factura",
             "proveedor",
            "fecha_llegada",
            "producto"
        ]
        widgets = {
            'fecha_llegada': XYZ_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),}


        labels = {
              "lote": _("Lote"),
              "factura": _("Factura"),
              "proveedor": _("Proveedor"),
              "fecha_llegada": _("Fecha de llegada"),
              "producto": _("Producto"),
        }
        help_texts = {
            "lote": _("Ingresa el lote."),
              "factura": _("Ingresa la factura."),
              "proveedor": _("Ingresa el proveedor."),
              "fecha_llegada": _("Ingresa la fecha de llegada."),
              "producto": _("Ingresa el producto."),
        }

class SeguimientosForm(forms.ModelForm):
    class Meta:
        model = Seguimientos
        fields = [
            "nombre",
            "fecha_recibo",
                "nombre_empleado_origen",
            "nombre_empleado_destino",
                "estado",
            "producto",
                "departamento_inicial",
            "departamento_final"
        ]
        widgets = {
            'fecha_recibo': XYZ_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),

        }

        labels = {
              "nombre": _("Nombre"),
            "fecha_recibo": _("Fecha de recibo"),
            "nombre_empleado_origen": _("Nombre del empleado origen"),
            "nombre_empleado_destino": _("Nombre del empleado destino"),
            "estado": _("Estado"),
            "producto": _("Producto"),
             "departamento_inicial": _("Departamento Inicial"),
            "departamento_final": _("Departamento Final"),
        }
        help_texts = {
            "nombre": _("Ingresa el nombre del seguimiento."),
            "fecha_recibo": _("Ingresa la fecha de recibo del seguimiento."),
            "nombre_empleado_origen": _("Ingresa el nombre del empleado origen del seguimiento."),
            "nombre_empleado_destino": _("Ingresa el nombre del empleado destino del seguimiento."),
            "estado": _("Ingresa el estado del seguimiento."),
            "producto": _("Selecciona el producto del seguimiento."),
             "departamento_inicial": _("Selecciona el departamento inicial del seguimiento."),
            "departamento_final": _("Selecciona el departamento final del seguimiento."),
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['departamento_inicial'].queryset = Departamentos.objects.all()
            self.fields['departamento_final'].queryset = Departamentos.objects.all()
            self.fields['producto'].queryset = UProducto.objects.all()


class DepartamentosForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = [
            "nombre",
            "campus"
        ]
        labels = {
              "nombre": _("Nombre"),
            "campus": _("Campus"),
        }
        help_texts = {
              "nombre": _("Ingresa el nombre del departamento."),
              "campus": _("Selecciona el campus del departamento."),
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['campus'].queryset = Campus.objects.all()

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = [
            "nombre"
        ]
        labels = {
              "nombre": _("Nombre"),
        }
        help_texts = {
              "nombre": _("Ingresa tu el nombre del campus."),
        }

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = [
            "nombre",
           "correo",
            "password",
            "sesion",
           "tipo_usuario"
        ]
        labels = {
              "nombre": _("Nombre"),
            "correo": _("Correo"),
            "password": _("Contrasena"),
            "sesion": _("Sesion"),
                    "tipo_usuario": _("Tipo de usuario"),

        }
        help_texts = {
              "nombre": _("Ingresa el nombre del usuario."),
            "correo": _("Ingresa el correo del usuario."),
            "password": _("Ingresa la contrasena del usuario."),
            "sesion": _("Ingresa la sesion del usuario."),
                "tipo_usuario": _("Selecciona el tipo de usuario."),
        }

class SesionesForm(forms.ModelForm):
    class Meta:
        model = Sesiones
        fields = [
            "estado",]

        labels = {
              "estado": _("Estado"),
        }
        help_texts = {
              "estado": _("Ingresa el estado de la sesion."),
        }


class USubProductoForm(forms.ModelForm):
    class Meta:
        model = USubProducto
        fields = [
            "nombre",
            "cantidad",
              "descripcion"
        ]
        labels = {
              "nombre": _("Nombre"),
            "cantidad": _("Cantidad"),
             "descripcion": _("Descripcion"),

        }
        help_texts = {
              "nombre": _("Ingresa el nombre del subproducto."),
            "cantidad": _("Ingresa la cantidad del subproducto."),
             "descripcion": _("Ingresa la descripcion del subproducto."),

        }

class UProductoForm(forms.ModelForm):
    class Meta:
        model = UProducto
        fields = [
            "nombre",
            "fecha_caducidad",
                "cat_material_peligro",
            "u_sub_producto"
        ]
        widgets = {
            'fecha_caducidad': XYZ_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),

        }
        labels = {
              "nombre": _("Nombre"),
            "fecha_caducidad": _("Fecha de caducidad"),
            "cat_material_peligro": _("CatMatPeligroso"),
            "u_sub_producto": _("Suboroducto"),
        }
        help_texts = {
              "nombre": _("Ingresa el nombre del producto."),
            "fecha_caducidad": _("Ingresa la fecha de caducidad del producto."),
            "cat_material_peligro": _("Selecciona el CatMatPeligroso del producto."),
            "u_sub_producto": _("Selecciona el  Suboroducto del producto."),
        }

class AuditoriasEForm(forms.ModelForm):
    class Meta:
        model = AuditoriasE
        fields = [
            "departamento",
            "seguimiento",
             "producto",
            "fecha"
        ]
        labels = {
              "departamento": _("Departamento"),
            "seguimiento": _("Seguimiento"),
            "producto": _("Producto"),
            "fecha": _("Fecha"),
        }
        help_texts = {
              "departamento": _("Selecciona el departamento de la auditoria."),
            "seguimiento": _("Selecciona el seguimiento de la auditoria."),
            "producto": _("Selecciona el producto de la auditoria."),
            "fecha": _("Selecciona la fecha de la auditoria."),
        }

        widgets = {
            'fecha': XYZ_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),}
class AuditoriasSForm(forms.ModelForm):
    class Meta:
        model = AuditoriasS
        fields = [
            "producto",
            "departamento",
                    "fecha_auditoria",
            "estatus",
                    "etiquetado",
            "vida_util"
        ]
        labels = {
            "producto": _("Producto"),
             "departamento": _("Departamento"),
        "fecha_auditoria": _("Fecha de Auditoria"),
                "estatus": _("Estatus"),
                "etiquetado": _("Etiquetado"),
                "vida_util": _("Vida Util"),
            }
        help_texts = {
            "producto": _("Selecciona el producto de la auditoria"),
             "departamento": _("Selecciona el departamento de la auditoria"),
        "fecha_auditoria": _("Selecciona la fecha de la auditoria"),
                "estatus": _("Ingresa el estatus de la auditoria"),
                "etiquetado": _("Ingresa el etiquetado de la auditoria"),
                "vida_util": _("Ingresa la vida  util de la auditoria"),
        }

        widgets = {
            'fecha_auditoria': XYZ_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),}
class LoginForm(forms.ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = [
            "correo",
            "password",
        ]
        labels = {
              "correo": _("Correo"),
            "password": _("Contrasena"),
        }
        help_texts = {
              "correo": _("Ingresa tu correo."),
              "password": _("Ingresa tu contrasena."),
        }

class RegistroForm(forms.ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['nombre', 'correo', 'password','tipo_usuario' ]
        labels = {
            "password": _("Contrasena"),
             "tipo_usuario": _("Tipo de usuario"),

        }
        help_texts = {
            "nombre": _("Ingresa el nombre completo del usuario."),
              "correo": _("Ingresa el correo del usuario."),
              "password": _("Ingresa la contrasena del usuario."),
              "tipo_usuario": _("Selecciona el tipo de usuario."),
        }

class NuevoSeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimientos
        fields = [
               "departamento_inicial",
            "nombre_empleado_destino",
  "producto",


            "fecha_recibo",
                "nombre_empleado_origen",

                "estado",


            "departamento_final"
        ]
        widgets = {
            'fecha_recibo': XYZ_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),

        }

        labels = {
              "nombre": _("Nombre"),
            "fecha_recibo": _("Fecha de recibo"),
            "nombre_empleado_origen": _("Nombre del empleado origen"),
            "nombre_empleado_destino": _("Nombre del empleado destino"),
            "estado": _("Estado"),
            "producto": _("Producto"),
             "departamento_inicial": _("Departamento Inicial"),
            "departamento_final": _("Departamento Final"),
        }
        help_texts = {
            "nombre": _("Ingresa el nombre del seguimiento."),
            "fecha_recibo": _("Ingresa la fecha de recibo del seguimiento."),
            "nombre_empleado_origen": _("Ingresa el nombre del empleado origen del seguimiento."),
            "nombre_empleado_destino": _("Ingresa el nombre del empleado destino del seguimiento."),
            "estado": _("Ingresa el estado del seguimiento."),
            "producto": _("Selecciona el producto del seguimiento."),
             "departamento_inicial": _("Selecciona el departamento inicial del seguimiento."),
            "departamento_final": _("Selecciona el departamento final del seguimiento."),
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['departamento_inicial'].queryset = Departamentos.objects.all()
            self.fields['departamento_final'].queryset = Departamentos.objects.all()
            self.fields['producto'].queryset = UProducto.objects.all()






class NuevoRegAlmacenForm(forms.ModelForm):
    class Meta:
        model = RegAlmacen
        fields = [
             "factura",
            "lote",
             "proveedor",
            "fecha_llegada",

        ]
        widgets = {
            'fecha_llegada': XYZ_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),}


        labels = {
              "lote": _("Lote"),
              "factura": _("Factura"),
              "proveedor": _("Proveedor"),
              "fecha_llegada": _("Fecha de llegada"),
        }
        help_texts = {
            "lote": _("Ingresa el lote."),
              "factura": _("Ingresa la factura."),
              "proveedor": _("Ingresa el proveedor."),
              "fecha_llegada": _("Ingresa la fecha de llegada."),
        }
