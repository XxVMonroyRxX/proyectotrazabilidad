from django.contrib.auth.models import Permission
import datetime
import logging
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import UsuarioPersonalizado


logger = logging.getLogger(__name__)
def crear_permisos():
    content_type = ContentType.objects.get_for_model(UsuarioPersonalizado)
    logger.warning('Se ejecuta la funcion crear_permisos a las  '+str(datetime.datetime.now())+' horas!')
    try:
        logger.warning('Se trata de crear el permiso administrador en permissions.py a las  '+str(datetime.datetime.now())+' horas!')
        Permission.objects.get_or_create(codename='administrador', name='administrador',
        content_type=content_type,)
    except:
        logger.warning('Ocurrio un error al crear el permiso administrador en permissions.py a las  '+str(datetime.datetime.now())+' horas!')
    try:
        logger.warning('Se trata de crear el permiso auditor en permissions.py a las  '+str(datetime.datetime.now())+' horas!')
        Permission.objects.get_or_create(codename='auditor', name='auditor',
        content_type=content_type,)
    except:
        logger.warning('Ocurrio un error al crear el permiso administrador en permissions.py a las  '+str(datetime.datetime.now())+' horas!')
    try:
        logger.warning('Se trata de crear el permiso almacen en permissions.py a las  '+str(datetime.datetime.now())+' horas!')
        Permission.objects.get_or_create(codename='almacen', name='almacen',
        content_type=content_type,)
    except:
        logger.warning('Ocurrio un error al crear el permiso administrador en permissions.py a las  '+str(datetime.datetime.now())+' horas!')

