from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from django.contrib import messages
from .models import *
from .forms import *
import datetime
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.core.files.storage import FileSystemStorage
from qrcode import *
import time
from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required,user_passes_test

logger = logging.getLogger(__name__)

def inicio(request):
    context ={}
    if request.method == 'GET':
            return render(request, "bitacora/inicio/Index.html", context)

def loguearse(request):
    context ={}
    if request.method == 'GET':
            return render(request, "bitacora/login/InicioSesion.html", context)

def registroalmacen(request):
    context ={}
    if request.method == 'GET':
            return render(request, "bitacora/registro/NuevoRegristro.html", context)
@login_required(login_url='login')
def almacen(request):
    context ={}
    if request.method == 'GET':
            return render(request, "bitacora/inicio/PrincipalAlmacen.html", context)


@login_required(login_url='login')
def acerca(request):
    context ={}
    if request.method == 'GET':
            return render(request, "bitacora/inicio/AcercaDe.html", context)


def admin(request):
    pass



@login_required(login_url='login')
def listar_auditorias_s(request):
    logger.warning('Se ejecuta la funcion listar_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["dataset"] = AuditoriasS.objects.all()
    context["titulo"] = "Auditorias_S"
    return render(request, "bitacora/auditorias_s/listar.html", context)
@login_required(login_url='login')
def visualizar_auditorias_s(request, id):
    logger.warning('Se ejecuta la funcion visualizar_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["data"] = AuditoriasS.objects.get(id = id)
    context["titulo"] = "Auditorias_S"
    context["accion"] = "Visualizar"
    return render(request, "bitacora/auditorias_s/detalle.html", context)
@login_required(login_url='login')
def crear_auditorias_s(request):
    logger.warning('Se ejecuta la funcion crear_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_S"
    context["accion"] = "Creacion"
    form = AuditoriasSForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/auditorias_s/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'La auditoria ha sido creada de manera exitosa.')
                logger.warning('Se crea una auditoria a las  '+str(datetime.datetime.now())+' horas!')
                return redirect('listar_auditorias_s')
            else:
                messages.error(request, 'Porfavor corrige los errores:')
                logger.warning('Error de validacion')
                return render(request, "bitacora/auditorias_s/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def eliminar_auditorias_s(request, id):
    logger.warning('Se ejecuta la funcion eliminar_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_S"
    obj = get_object_or_404(AuditoriasS, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Auditoria {id} eliminada de manera exitosa.')
        messages.success(request, f'Auditoria {id} eliminada de manera exitosa.')
        return HttpResponseRedirect("listar_auditorias_s")
    return render(request, "bitacora/auditorias_s/listar.html", context)
@login_required(login_url='login')
def actualizar_auditorias_s(request, id):
    logger.warning('Se ejecuta la funcion actualizar_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_S"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(AuditoriasS, id = id)
    form = AuditoriasSForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "bitacora/auditorias_s/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'La auditoria {id} ha sido actualizada de manera exitosa.')
                messages.success(request, f'La auditoria {id} ha sido actualizada de manera exitosa.')
                return HttpResponseRedirect('listar_auditorias_s')
            else:
                logger.warning('Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/auditorias_s/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def listar_auditorias_e(request):
    logger.warning('Se ejecuta la funcion listar_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    context["dataset"] = AuditoriasE.objects.all()
    return render(request, "bitacora/auditorias_e/listar.html", context)
@login_required(login_url='login')
def visualizar_auditorias_e(request, id):
    logger.warning('Se ejecuta la funcion visualizar_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    context["accion"] = "Visualizacion"
    context["data"] = AuditoriasE.objects.get(id = id)
    return render(request, "bitacora/auditorias_e/detalle.html", context)
@login_required(login_url='login')
def crear_auditorias_e(request):
    logger.warning('Se ejecuta la funcion crear_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    context["accion"] = "Creacion"
    form = AuditoriasEForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/auditorias_e/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('La auditoria ha sido creada de manera exitosa.')
                messages.success(request, 'La auditoria ha sido creada de manera exitosa.')
                return redirect('listar_auditorias_e')
            else:
                logger.warning('Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/auditorias_e/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

@login_required(login_url='login')
def eliminar_auditorias_e(request, id):
    logger.warning('Se ejecuta la funcion eliminar_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    obj = get_object_or_404(AuditoriasE, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Auditoria {id} eliminada de manera exitosa.')
        messages.success(request, f'Auditoria {id} eliminada de manera exitosa.')
        return HttpResponseRedirect("listar_auditorias_e")
    return render(request, "bitacora/auditorias_e/listar.html", context)
@login_required(login_url='login')
def actualizar_auditorias_e(request, id):
    logger.warning('Se ejecuta la funcion actualizar_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(AuditoriasE, id = id)
    form = AuditoriasEForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "bitacora/auditorias_e/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'La auditoria {id} ha sido actualizada de manera exitosa.')
                messages.success(request, f'La auditoria {id} ha sido actualizada de manera exitosa.')
                return HttpResponseRedirect('listar_auditorias_e')
            else:
                logger.warning('Porfavor corrige los errores:')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/auditorias_e/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

@login_required(login_url='login')
def listar_u_producto(request):
    logger.warning('Se ejecuta la funcion listar_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    context["dataset"] = UProducto.objects.all()
    return render(request, "bitacora/u_producto/listar.html", context)
@login_required(login_url='login')
def visualizar_u_producto(request, id):
    logger.warning('Se ejecuta la funcion visualizar_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    context["accion"] = "Visualizacion"
    obj = get_object_or_404(UProducto, id = id)
    context["data"] = UProducto.objects.get(id = id)
    context["form"] = UProductoForm(request.POST or None,instance=obj)
    return render(request, "bitacora/u_producto/detalle.html", context)
@login_required(login_url='login')
def crear_u_producto(request):
    logger.warning('Se ejecuta la funcion crear_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    context["accion"] = "Creacion"
    form = UProductoForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/u_producto/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('La auditoria ha sido creada de manera exitosa.')
                messages.success(request, 'La auditoria ha sido creada de manera exitosa.')
                return redirect('listar_u_producto')
            else:
                logger.warning('Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/u_producto/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

@login_required(login_url='login')
def eliminar_u_producto(request, id):
    logger.warning('Se ejecuta la funcion eliminar_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    obj = get_object_or_404(UProducto, id = id)
    try:
        obj.delete()
        messages.success(request, f'Producto {id} eliminada de manera exitosa.')
        logger.warning(f'U Producto {id} eliminado de manera exitosa.')
        messages.success(request, f'U Producto {id} eliminado de manera exitosa.')
        return redirect("listar_u_producto")
    except:
        logger.warning(f'No se pudo eliminar.')
        messages.success(request, f'El U_Produto {id} no se pudo eliminarse..')
    return render(request, "bitacora/u_producto/listar.html", context)

@login_required(login_url='login')
def actualizar_u_producto(request, id):
    logger.warning('Se ejecuta la funcion actualizar_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(UProducto, id = id)
    form = UProductoForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["obj"] = obj
        context["form"] = form
        return render(request, "bitacora/u_producto/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'El producto {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'El producto {id} ha sido actualizado de manera exitosa.')
                return redirect("listar_u_producto")
            else:
                logger.warning(f'Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/u_producto/detalle.html", {'context':context,'form':form})
        except:
            logger.warning(f'Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def listar_u_sub_producto(request):
    logger.warning('Se ejecuta la funcion listar_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    context["dataset"] = USubProducto.objects.all()
    return render(request, "bitacora/u_sub_producto/listar.html", context)
@login_required(login_url='login')
def visualizar_u_sub_producto(request, id):
    logger.warning('Se ejecuta la funcion visualizar_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    context["accion"] = "Visualizacion"
    obj = get_object_or_404(USubProducto, id = id)
    context["data"] = USubProducto.objects.get(id = id)
    context["form"] = USubProductoForm(request.POST or None,instance=obj)
    return render(request, "bitacora/u_sub_producto/detalle.html", context)
@login_required(login_url='login')
def crear_u_sub_producto(request):
    logger.warning('Se ejecuta la funcion crear_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    context["accion"] = "Creacion"
    form = USubProductoForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/u_sub_producto/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('Subproducto ha sido creado de manera exitosa.')
                messages.success(request, 'Subproducto ha sido creado de manera exitosa.')
                return redirect('listar_u_sub_producto')
            else:
                logger.warning('Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/u_sub_productos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')



@login_required(login_url='login')
def eliminar_u_sub_producto(request, id):
    logger.warning('Se ejecuta la funcion eliminar_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    obj = get_object_or_404(USubProducto, id = id)
    try:
        obj.delete()
        logger.warning(f'Sub Producto {id} eliminado de manera exitosa.')
        messages.success(request, f'Sub Producto {id} eliminado de manera exitosa.')
        return redirect("listar_u_sub_producto")
    except:
        logger.warning(f'No se pudo eliminar.')
        messages.success(request, f'El U_Sub_Produto {id} no se pudo eliminarse..')
    return render(request, "bitacora/u_sub_producto/listar.html", context)

@login_required(login_url='login')
def actualizar_u_sub_producto(request, id):
    logger.warning('Se ejecuta la funcion actualizar_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(USubProducto, id = id)
    form = USubProductoForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["obj"] = obj
        context["form"] = form
        return render(request, "bitacora/u_sub_producto/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'El subproducto {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'El subproducto {id} ha sido actualizado de manera exitosa.')
                return redirect("listar_u_sub_producto")
            else:
                logger.warning(f'Se ha generado un error de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/u_sub_producto/detalle.html", {'context':context,'form':form})
        except:
            logger.warning(f'Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')






















@login_required(login_url='login')
def listar_cat_mat_peligroso(request):
    logger.warning('Se ejecuta la funcion listar_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligrosos"
    context["dataset"] = CatMatPeligroso.objects.all()
    return render(request, "bitacora/cat_mat_peligroso/listar.html", context)
@login_required(login_url='login')
def visualizar_cat_mat_peligroso(request, id):
    logger.warning('Se ejecuta la funcion visualizar_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligrosos"
    context["accion"] = "Visualizacion"
    obj = get_object_or_404(CatMatPeligroso, id = id)
    context["data"] = CatMatPeligroso.objects.get(id = id)
    context["form"] = CatMatPeligrosoForm(request.POST or None, instance = obj)
    return render(request, "bitacora/cat_mat_peligroso/detalle.html", context)
@login_required(login_url='login')
def crear_cat_mat_peligroso(request):
    logger.warning('Se ejecuta la funcion crear_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligroso"
    context["accion"] = "Creacion"
    form = CatMatPeligrosoForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/cat_mat_peligroso/detalle.html", context)
    elif request.method == 'POST':
        try:
            form = CatMatPeligrosoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                logger.warning('Categoria material peligroso ha sido creado de manera exitosa.')
                messages.success(request, 'Categoria material peligroso ha sido creado de manera exitosa.')
                return redirect('listar_cat_mat_peligroso')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/cat_mat_peligroso/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def eliminar_cat_mat_peligroso(request, id):
    logger.warning('Se ejecuta la funcion eliminar_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligrosos"
    obj = get_object_or_404(CatMatPeligroso, id = id)
    try:
        obj.delete()
        logger.warning(f'Cat Mat Peligroso {id} eliminado de manera exitosa.')
        messages.success(request, f'Cat Mat Peligroso {id} eliminado de manera exitosa.')
        return redirect("listar_cat_mat_peligroso")
    except:
        logger.warning(f'No se pudo eliminar.')
        messages.success(request, f'El Cat Mat peligroso {id} no pudo eliminarse..')
    return render(request, "bitacora/cat_mat_peligroso/listar.html", context)
@login_required(login_url='login')
def actualizar_cat_mat_peligroso(request, id):
    logger.warning('Se ejecuta la funcion actualizar_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligrosos"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(CatMatPeligroso, id = id)
    form = CatMatPeligrosoForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["obj"] = obj
        context["form"] = form
        return render(request, "bitacora/cat_mat_peligroso/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning( f'Categoria Mat Peligroso {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Categoria Mat Peligroso {id} ha sido actualizado de manera exitosa.')
                return redirect("listar_cat_mat_peligroso")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/cat_mat_peligroso/detalle.html", {'context':context,'form':form})
        except:
            logger.warning( 'Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
























@login_required(login_url='login')
def listar_reg_almacen(request):
    logger.warning('Se ejecuta la funcion listar_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "RegAlmacen"
    context["dataset"] = RegAlmacen.objects.all()
    return render(request, "bitacora/reg_almacen/listar.html", context)
@login_required(login_url='login')
def visualizar_reg_almacen(request, id):
    logger.warning('Se ejecuta la funcion visualizar_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "RegAlmacen"
    context["accion"] = "Visualizacion"
    obj = get_object_or_404(RegAlmacen, id = id)
    context["data"] = RegAlmacen.objects.get(id = id)
    context["form"] = RegAlmacenForm(request.POST or None,instance=obj)
    return render(request, "bitacora/reg_almacen/detalle.html", context)
@login_required(login_url='login')
def crear_reg_almacen(request):
    logger.warning('Se ejecuta la funcion crear_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Reg_Almacen"
    context["accion"] = "Creacion"
    form = RegAlmacenForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/reg_almacen/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('Reg Almacen ha sido creado de manera exitosa.')
                messages.success(request, 'Reg Almacen ha sido creado de manera exitosa.')
                return redirect('listar_reg_almacen')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/reg_almacen/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def eliminar_reg_almacen(request, id):
    logger.warning('Se ejecuta la funcion eliminar_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "RegAlmacen"
    obj = get_object_or_404(RegAlmacen, id = id)
    try:
        obj.delete()
        logger.warning(f'Reg Almacen {id} eliminado de manera exitosa.')
        messages.success(request, f'Reg Almacen {id} eliminado de manera exitosa.')
        return redirect("listar_reg_almacen")
    except:
        logger.warning(f'No se pudo eliminar.')
        messages.success(request, f'El Reg_Almacen {id} no  pudo eliminarse..')
    return render(request, "bitacora/reg_almcen/listar.html", context)

@login_required(login_url='login')
def actualizar_reg_almacen(request, id):
    logger.warning('Se ejecuta la funcion actualizar_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Reg_Almacen"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(RegAlmacen, id = id)
    form = RegAlmacenForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["obj"] = obj
        context["form"] = form
        return render(request, "bitacora/reg_almacen/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'Reg Almacen {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Reg Almacen {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("listar_reg_almacen")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/reg_almacen/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')


@login_required(login_url='login')
def listar_seguimientos(request):
    logger.warning('Se ejecuta la funcion listar_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["dataset"] = Seguimientos.objects.all()
    context["form"] = SeguimientosForm(request.POST or None)
    return render(request, "bitacora/seguimientos/listar.html", context)
@login_required(login_url='login')
def visualizar_seguimientos(request, id):
    logger.warning('Se ejecuta la funcion visualizar_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["accion"] = "Visualizacion"
    context["data"] = Seguimientos.objects.get(id = id)
    obj = get_object_or_404(Seguimientos, id = id)
    context["form"] = SeguimientosForm(request.POST or None, instance = obj)
    return render(request, "bitacora/seguimientos/detalle.html", context)
@login_required(login_url='login')
def crear_seguimientos(request):
    logger.warning('Se ejecuta la funcion crear_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["accion"] = "Creacion"
    form = SeguimientosForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/seguimientos/detalle.html", context)
    elif request.method == 'POST':
        try:
            print("Llega aca 1")
            print(form.errors)
            if form.is_valid():
                img = make("http://127.0.0.1:8000/seguimientos/visualizar/4")
                img_name = 'qr' + str(time.time()) + '.png'
                img.save(settings.MEDIA_ROOT + '/qr/' + img_name)
                form.save()
                print("Llega aca 3")
                logger.warning('Seguimiento ha sido creado de manera exitosa.')
                messages.success(request, 'Seguimiento ha sido creado de manera exitosa.')
                return redirect('listar_seguimientos')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/seguimientos/detalle.html", {'context':context,'form':form})
        except Exception as e:
            logger.warning('Ha ocurrido un error inesperado.'+str(e))
            messages.error(request, 'Ha ocurrido un error inesperado.')
        return render(request, "bitacora/seguimientos/listar.html", context)

@login_required(login_url='login')
def eliminar_seguimientos(request, id):
    logger.warning('Se ejecuta la funcion eliminar_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["accion"] = "Eliminacion"
    obj = get_object_or_404(Seguimientos, id = id)
    try:
        obj.delete()
        logger.warning(f'Seguimiento {id} eliminado de manera exitosa.')
        messages.success(request, f'Seguimiento {id} eliminado de manera exitosa.')
        return redirect("listar_seguimientos")
    except:
        logger.warning(f'No se pudo eliminar.')
        messages.success(request, f'El departamento {id} no se pudo eliminarse..')
    return render(request, "bitacora/seguimientos/listar.html", context)
@login_required(login_url='login')
def actualizar_seguimientos(request, id):
    logger.warning('Se ejecuta la funcion actualizar_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Seguimientos, id = id)
    form = SeguimientosForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["obj"] = obj
        context["form"] = form
        return render(request, "bitacora/seguimientos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'Seguimiento {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Seguimiento {id} ha sido actualizado de manera exitosa.')
                return redirect("listar_seguimientos")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/seguimientos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def listar_departamentos(request):
    logger.warning('Se ejecuta la funcion listar_departamentos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Departamentos"
    context["dataset"] = Departamentos.objects.all()
    context["form"] = DepartamentosForm(request.POST or None)
    return render(request, "bitacora/departamentos/listar.html", context)
@login_required(login_url='login')
def visualizar_departamentos(request, id):
    logger.warning('Se ejecuta la funcion visualizar_departamentos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Departamentos"
    context["accion"] = "Visualizacion"
    context["data"] = Departamentos.objects.get(id = id)
    obj = get_object_or_404(Departamentos, id = id)
    context["form"] = DepartamentosForm(request.POST or None, instance = obj)
    return render(request, "bitacora/departamentos/detalle.html", context)

@login_required(login_url='login')
def crear_departamentos(request):
    logger.warning('Se ejecuta la funcion crear_departamentos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Departamentos"
    context["accion"] = "Creacion"
    form = DepartamentosForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/departamentos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('Departamento ha sido creado de manera exitosa.')
                messages.success(request, 'Departamento ha sido creado de manera exitosa.')
                return redirect('listar_departamentos')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/departamentos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
        return render(request, "bitacora/departamentos/listar.html", context)

@login_required(login_url='login')
def eliminar_departamentos(request, id):
    logger.warning('Se ejecuta la funcion eliminar_departamentos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Departamentos"
    context["accion"] = "Eliminacion"

    obj = get_object_or_404(Departamentos, id = id)
    try:
        obj.delete()
        logger.warning(f'Departamento {id} eliminado de manera exitosa.')
        messages.success(request, f'Departamento {id} eliminado de manera exitosa.')
        return redirect("listar_departamentos")
    except:
        logger.warning(f'No se pudo eliminar.')
        messages.success(request, f'El departamento {id} no se pudo eliminarse..')
    return render(request, "bitacora/departamentos/listar.html", context)
@login_required(login_url='login')
def actualizar_departamento(request, id):
    logger.warning('Se ejecuta la funcion actualizar_departamentos a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Departamentos"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Departamentos, id = id)
    form = DepartamentosForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["obj"] = obj
        context["form"] = form
        return render(request, "bitacora/departamentos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'El departamento {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Departamento {id} ha sido actualizado de manera exitosa.')
                return redirect("listar_departamentos")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/departamentos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

@login_required(login_url='login')
def listar_campus(request):
    logger.warning('Se ejecuta la funcion listar_campus a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Campus"
    context["dataset"] = Campus.objects.all()
    return render(request, "bitacora/campus/listar.html", context)
@login_required(login_url='login')
def visualizar_campus(request, id):
    logger.warning('Se ejecuta la funcion visualizar_campus a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Campus"
    context["accion"] = "Visualizacion"
    obj = get_object_or_404(Campus, id = id)
    context["data"] = Campus.objects.get(id = id)
    context["form"] = CampusForm(request.POST or None, instance = obj)
    return render(request, "bitacora/campus/detalle.html", context)
@login_required(login_url='login')
def crear_campus(request):
    logger.warning('Se ejecuta la funcion crear_campus a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Campus"
    context["accion"] = "Creacion"
    form = CampusForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/campus/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('El Campus ha sido creado de manera exitosa.')
                messages.success(request, 'El Campus ha sido creado de manera exitosa.')
                return redirect('listar_campus')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/campus/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def eliminar_campus(request, id):
    logger.warning('Se ejecuta la funcion eliminar_campus a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Campus"
    obj = get_object_or_404(Campus, id = id)
    try:
        obj.delete()
        logger.warning(f'Campus {id} eliminado de manera exitosa.')
        messages.success(request, f'Campus {id} eliminado de manera exitosa.')
        return redirect("listar_campus")
    except:
        logger.warning(f'No se pudo eliminar.')
        messages.success(request, f'El campus {id} no se pudo eliminarse..')
    return render(request, "bitacora/campus/listar.html", context)
@login_required(login_url='login')
def actualizar_campus(request, id):
    logger.warning('Se ejecuta la funcion actualizar_campus a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Campus"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Campus, id = id)
    form = CampusForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["obj"] = obj
        context["form"] = form
        return render(request, "bitacora/campus/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'El campus {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'El campus {id} ha sido actualizado de manera exitosa.')
                return redirect("listar_campus")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/campus/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def listar_sesiones(request):
    logger.warning('Se ejecuta la funcion listar_sesiones a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Sesiones"
    context["dataset"] = Sesiones.objects.all()
    return render(request, "bitacora/sesiones/listar.html", context)
@login_required(login_url='login')
def visualizar_sesiones(request, id):
    logger.warning('Se ejecuta la funcion visualizar_sesiones a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Sesiones"
    context["accion"] = "Visualizacion"
    obj = get_object_or_404(Sesiones, id = id)
    context["data"] = Sesiones.objects.get(id = id)
    context["form"] = SesionesForm(request.POST or None, instance = obj)
    return render(request, "bitacora/sesiones/detalle.html", context)
@login_required(login_url='login')
def crear_sesiones(request):
    logger.warning('Se ejecuta la funcion crear_sesiones a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Sesiones"
    context["accion"] = "Creacion"

    form = SesionesForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/sesiones/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('La sesion ha sido creado de manera exitosa.')
                messages.success(request, 'La sesion ha sido creado de manera exitosa.')
                return redirect('listar_sesiones')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/sesiones/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def eliminar_sesiones(request, id):
    logger.warning('Se ejecuta la funcion eliminar_sesiones a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Sesiones"
    obj = get_object_or_404(Sesiones, id = id)
    try:
        obj.delete()
        logger.warning( f'Sesion {id} eliminada de manera exitosa.')
        messages.success(request, f'Sesion {id} eliminada de manera exitosa.')
        return redirect("listar_sesiones")
    except:
        logger.warning(f'No se pudo eliminar.')
        messages.success(request, f'La sesion {id} no se pudo eliminarse..')
    return render(request, "bitacora/campus/sesiones.html", context)
@login_required(login_url='login')
def actualizar_sesiones(request, id):
    logger.warning('Se ejecuta la funcion actualizar_sesiones a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Sesiones"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Sesiones, id = id)
    form = SesionesForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["obj"] = obj
        context["form"] = form
        return render(request, "bitacora/sesiones/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning( f'Sesion {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Sesion {id} ha sido actualizado de manera exitosa.')
                return redirect("listar_sesiones")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/sesiones/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

@login_required(login_url='login')
def listar_usuarios(request):
    logger.warning('Se ejecuta la funcion listar_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    context["dataset"] = UsuarioPersonalizado.objects.all()
    return render(request, "bitacora/usuarios/listar.html", context)
@login_required(login_url='login')
def visualizar_usuarios(request, id):
    logger.warning('Se ejecuta la funcion visualizar_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    context["accion"] = "Visualizacion"

    context["data"] = UsuarioPersonalizado.objects.get(id = id)
    return render(request, "bitacora/usuarios/detalle.html", context)
@login_required(login_url='login')
def crear_usuarios(request):
    logger.warning('Se ejecuta la funcion crear_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    context["accion"] = "Creacion"

    form = UsuariosForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/usuarios/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('El usuario ha sido creado de manera exitosa.')
                messages.success(request, 'El usuario ha sido creado de manera exitosa.')
                return redirect('departamentos')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/usuarios/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
@login_required(login_url='login')
def eliminar_usuarios(request, id):
    logger.warning('Se ejecuta la funcion eliminar_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    obj = get_object_or_404(UsuarioPersonalizado, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Usuario {id} eliminado de manera exitosa.')
        messages.success(request, f'Usuario {id} eliminado de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "bitacora/usuarios/listar.html", context)
@login_required(login_url='login')
def actualizar_usuarios(request, id):
    logger.warning('Se ejecuta la funcion actualizar_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(UsuarioPersonalizado, id = id)
    form = UsuariosForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "bitacora/usuarios/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'Usuario {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Usuario {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("campus")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/usuarios/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')


def logout_request(request):
	logout(request)
	messages.info(request, "Has cerrado sesion correctamente")
	return redirect("inicio")

def iniciar_sesion(request):
    logout(request)
    logger.warning(f'Se desea iniciar sesion.')
    context ={}
    correo = contrasena = ''
    if request.POST:
        correo = request.POST['correo']
        contrasena = request.POST['password']
        usuario = authenticate(correo=correo, password=contrasena)
        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                print("Permisos del usuario al logueo ",usuario.get_user_permissions())
                request.session["sesion_usuario"] = usuario.nombre
                return redirect('inicio')
            messages.success(request, f'El usuario no esta activo, contacte al administrador')
        messages.success(request, f'Usuario o contrasena no validos')
    form = LoginForm()
    context={'form' : form}
    return render(request, "bitacora/login/InicioSesion.html", context)
def registrarse(request):
    logout(request)
    context ={}
    if request.POST:
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            tipo_usuario = formulario.cleaned_data.get('tipo_usuario')
            print(tipo_usuario)
            if tipo_usuario=='administrador':
                permission = Permission.objects.get(codename='administrador')
                usuario.user_permissions.add(permission)
            if tipo_usuario=='auditor':
                permission = Permission.objects.get(codename='auditor')
                usuario.user_permissions.add(permission)
            if tipo_usuario=='almacen':
                permission = Permission.objects.get(codename='almacen')
                usuario.user_permissions.add(permission)
            print("Finaliza")
            print("Permisos del usuario ",usuario.get_user_permissions())
            messages.success(request, "Registro de usuario exitoso.")
            return redirect("login")
        messages.error(request, "Registro invalido")
    form = RegistroForm()
    context={'form' : form}
    return render(request, "bitacora/registro/registro.html", context)
@login_required(login_url='login')
def almacen_inicio(request):
    return render(request, "bitacora/almacen/PrincipalAlmacen.html")
@login_required(login_url='login')
def registro_almacen(request):
    context ={}
    context["dataset"] = RegAlmacen.objects.all()

    if request.method == 'GET':
        form = NuevoRegAlmacenForm()
        context['form']= form
        return render(request, "bitacora/almacen/AlmacenUno.html", context)
    if request.method == 'POST':
        form = NuevoRegAlmacenForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request, "bitacora/almacen/AlmacenDos.html", {'formulario': form})
    return render(request, "bitacora/almacen/AlmacenUno.html",context)
@login_required(login_url='login')
def registro_almacen2(request):
    context ={}
    context['factura'] = request.GET.get('factura', None)
    context['lote'] = request.GET.get('lote', None)
    context['proveedor'] = request.GET.get('proveedor', None)
    context['fecha_llegada'] = request.GET.get('fecha_llegada', None)
    if request.method == 'POST':
        context['factura'] = request.POST.get('factura', None)
        context['lote'] = request.POST.get('lote', None)
        context['proveedor'] = request.POST.get('proveedor', None)
        context['fecha_llegada'] = request.POST.get('fecha_llegada', None)


        context['producto'] = request.POST.get('producto', None)
        context['tipo'] = request.POST.get('tipo', None)
        context['unidad'] = request.POST.get('unidad', None)
        context['cantidad'] = request.POST.get('cantidad', None)
        context['fecha'] = request.POST.get('fecha', None)
        context['descripcion'] = request.POST.get('descripcion', None)
        print(context)

    return render(request, "bitacora/almacen/AlmacenDos.html",context)

def reg_seguimiento(request):
    return render(request, "bitacora/seguimientos/NuevoSeguiminento.html")
def reg_nuevo_material(request):
    logger.warning('Se ejecuta la funcion crear_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligroso"
    context["accion"] = "Creacion"
    form = CatMatPeligrosoForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "bitacora/almacen/RegMateriales.html", context)
    elif request.method == 'POST':
        try:
            form = CatMatPeligrosoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                logger.warning('Categoria material peligroso ha sido creado de manera exitosa.')
                messages.success(request, 'Categoria material peligroso ha sido creado de manera exitosa.')
                return redirect('almacen_inicio')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "bitacora/almacen/RegMateriales.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
    return render(request, "bitacora/almacen/RegMateriales.html")
