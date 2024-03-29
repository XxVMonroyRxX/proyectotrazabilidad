# Generated by Django 3.2.19 on 2023-07-02 23:41

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'campus',
            },
        ),
        migrations.CreateModel(
            name='CatMatPeligroso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cretib', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('ficha_seguridad', models.FileField(blank=True, null=True, upload_to='fichas_seguridad/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
            options={
                'db_table': 'cat_mat_peligroso',
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento', to='bitacora.campus', verbose_name='campus del departamento')),
            ],
            options={
                'db_table': 'departamentos',
            },
        ),
        migrations.CreateModel(
            name='Sesiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=200)),
                ('fecha_conexion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'sesiones',
            },
        ),
        migrations.CreateModel(
            name='USubProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'u_sub_producto',
            },
        ),
        migrations.CreateModel(
            name='UsuarioPersonalizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nombre', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('tipo_usuario', models.CharField(choices=[('administrador', 'Usuario Administrador'), ('auditor', 'Usuario Auditor'), ('almacen', 'Usuario Almacen')], default='regular', max_length=30)),
                ('groups', models.ManyToManyField(related_name='bitacora_usuario_personalizado_groups', to='auth.Group')),
                ('sesion', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario', to='bitacora.sesiones', verbose_name='sesion de usuario')),
                ('user_permissions', models.ManyToManyField(related_name='bitacora_usuario_personalizado_user_permissions', to='auth.Permission')),
            ],
            options={
                'db_table': 'usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_caducidad', models.DateTimeField()),
                ('cat_material_peligro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mat_uproducto', to='bitacora.catmatpeligroso')),
                ('u_sub_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uproducto', to='bitacora.usubproducto')),
            ],
            options={
                'db_table': 'u_producto',
            },
        ),
        migrations.CreateModel(
            name='Seguimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_recibo', models.DateTimeField()),
                ('nombre_empleado_origen', models.CharField(max_length=200)),
                ('nombre_empleado_destino', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('departamento_final', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seg_final', to='bitacora.departamentos', verbose_name='departamento final del seguimiento')),
                ('departamento_inicial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seg_inicial', to='bitacora.departamentos', verbose_name='departamento inicial del seguimiento')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguimiento', to='bitacora.uproducto', verbose_name='producto del seguimiento')),
            ],
            options={
                'db_table': 'seguimientos',
            },
        ),
        migrations.CreateModel(
            name='RegAlmacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(max_length=200)),
                ('factura', models.IntegerField()),
                ('proveedor', models.CharField(max_length=200)),
                ('fecha_llegada', models.DateTimeField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regalmacen_producto', to='bitacora.uproducto', verbose_name='producto del almacen')),
            ],
            options={
                'db_table': 'reg_almacen',
            },
        ),
        migrations.CreateModel(
            name='AuditoriasS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_auditoria', models.DateTimeField()),
                ('estatus', models.CharField(max_length=200)),
                ('etiquetado', models.CharField(max_length=200)),
                ('vida_util', models.IntegerField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditorias_depto', to='bitacora.departamentos')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditorias_producto', to='bitacora.uproducto')),
            ],
            options={
                'db_table': 'auditorias_s',
            },
        ),
        migrations.CreateModel(
            name='AuditoriasE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditoriae_depto', to='bitacora.departamentos')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditoriae_producto', to='bitacora.uproducto')),
                ('seguimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditoriae_depto', to='bitacora.seguimientos')),
            ],
            options={
                'db_table': 'auditorias_e',
            },
        ),
    ]
