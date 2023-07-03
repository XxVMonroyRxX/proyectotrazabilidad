from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.core.validators import FileExtensionValidator


# Create your models here.
class Sesiones(models.Model):
    estado = models.CharField(max_length=200)
    fecha_conexion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Sesion {self.id}  - {self.estado}  - {self.fecha_conexion}"
    class Meta:
        db_table = "sesiones"

class UsuarioPersonalizado(AbstractUser):
    LEVEL_CHOICES = (
        ('administrador', 'Usuario Administrador'),
        ('auditor', 'Usuario Auditor'),
        ('almacen', 'Usuario Almacen'),

    )
    username = None
    nombre = models.CharField(max_length=30)
    correo = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    sesion = models.ForeignKey(Sesiones,on_delete=models.DO_NOTHING,verbose_name="sesion de usuario",default=None, blank=True, null=True,related_name="usuario")
    tipo_usuario = models.CharField(max_length=30, choices=LEVEL_CHOICES, default='regular')
    groups = models.ManyToManyField(
    'auth.Group',
    related_name='bitacora_usuario_personalizado_groups',
    )

    user_permissions = models.ManyToManyField(
    'auth.Permission',
    related_name='bitacora_usuario_personalizado_user_permissions',
    )
    REQUIRED_FIELDS = [nombre,correo,password]
    USERNAME_FIELD = 'correo'

    def __str__(self):
        return f"Usuarios {self.id}  - {self.nombre} - {self.correo}"
    class Meta:
        db_table = "usuarios"
    def verificar_contrasena(self,rcontrasena):
        if rcontrasena==self.password:
            return True
        else:
            return False
class Campus(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        db_table = "campus"
    def __str__(self):
        return 'Campus: ' + self.nombre
class Departamentos(models.Model):
    nombre = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus,on_delete=models.CASCADE,verbose_name="campus del departamento",related_name="departamento")
    def __str__(self):
        return f"Departamento {self.id}  - {self.nombre}"
    class Meta:
        db_table = "departamentos"
class CatMatPeligroso(models.Model):
    nombre = models.CharField(max_length=200)
    cretib = models.CharField(max_length=200)
    descripcion = models.TextField()
    ficha_seguridad =models.FileField(upload_to='fichas_seguridad/',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    imagen = models.ImageField(null=True,blank=True,upload_to='imagenes/')
    def __str__(self):
        return f"CatMatPeligroso {self.id}  - {self.nombre} - {self.cretib}"
    class Meta:
        db_table = "cat_mat_peligroso"

class USubProducto(models.Model):
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    def __str__(self):
        return f"Producto {self.id}  - {self.nombre}"
    class Meta:
        db_table = "u_sub_producto"
class UProducto(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_caducidad = models.DateTimeField()
    cat_material_peligro = models.ForeignKey(CatMatPeligroso,on_delete=models.CASCADE,related_name="mat_uproducto")
    u_sub_producto = models.ForeignKey(USubProducto,on_delete=models.CASCADE,related_name="uproducto")
    def __str__(self):
        return f"Producto {self.id}  - {self.nombre}"
    class Meta:
        db_table = "u_producto"
class Seguimientos(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_recibo = models.DateTimeField()
    nombre_empleado_origen = models.CharField(max_length=200)
    nombre_empleado_destino = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    producto = models.ForeignKey(UProducto,on_delete=models.CASCADE,verbose_name="producto del seguimiento",related_name="seguimiento")
    departamento_inicial = models.ForeignKey(Departamentos,on_delete=models.CASCADE,verbose_name="departamento inicial del seguimiento",related_name='seg_inicial',)
    departamento_final = models.ForeignKey(Departamentos,on_delete=models.CASCADE,verbose_name="departamento final del seguimiento",related_name='seg_final')
    def __str__(self):
        return f"Seguimiento {self.id}  - {self.nombre}"
    class Meta:
        db_table = "seguimientos"


class AuditoriasE(models.Model):
    departamento = models.ForeignKey(Departamentos,on_delete=models.CASCADE,related_name="auditoriae_depto")
    seguimiento = models.ForeignKey(Seguimientos,on_delete=models.CASCADE,related_name="auditoriae_depto")
    producto = models.ForeignKey(UProducto,on_delete=models.CASCADE,related_name="auditoriae_producto")
    fecha = models.DateTimeField()
    def __str__(self):
        return f"Auditoria {self.id} de {self.producto} realizada el {self.fecha_auditoria}"
    class Meta:
        db_table = "auditorias_e"
class AuditoriasS(models.Model):
    producto = models.ForeignKey(UProducto,on_delete=models.CASCADE,related_name="auditorias_producto")
    departamento = models.ForeignKey(Departamentos,on_delete=models.CASCADE,related_name="auditorias_depto")
    fecha_auditoria = models.DateTimeField()
    estatus = models.CharField(max_length=200)
    etiquetado = models.CharField(max_length=200)
    vida_util = models.IntegerField()
    def __str__(self):
        return f"Auditoria {self.id} de {self.producto} realizada el {self.fecha_auditoria}"
    class Meta:
        db_table = "auditorias_s"
class RegAlmacen(models.Model):
    lote = models.CharField(max_length=200)
    factura = models.IntegerField()
    proveedor = models.CharField(max_length=200)
    fecha_llegada = models.DateTimeField()
    producto = models.ForeignKey(UProducto,on_delete=models.CASCADE,verbose_name="producto del almacen",related_name="regalmacen_producto")
    def __str__(self):
        return f"RegAlmacen {self.id}  - {self.producto}"
    class Meta:
        db_table = "reg_almacen"
