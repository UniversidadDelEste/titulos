# -*- coding: utf-8 -*-
@auth.requires_login()
def cargarEgresados():
    db.t_egresados.id.readable = False
    db.t_egresados.f_cargo.readable = False
    form = SQLFORM.smartgrid(db.t_egresados,onupdate=auth.archive,deletable=False,csv=False,details=False,searchable=False,onvalidation=no_es_menor)
    return locals()

def no_es_menor(form):
    #Si estamos editando un campo
    if (request.args[1] == 'edit'):
        #obtenemos el id del campo a modificar
        idUpdate = request.args[3]
        #traemos el registro del valor
        r = db(db.t_egresados.id==idUpdate).select().first()
        if form.vars.f_egresados < r.f_egresados:
            form.errors.f_egresados = 'La cantidad de egresados no puede ser menor al valor anterior (%s)' % (r.f_egresados)
        if form.vars.f_anio != r.f_anio:
            form.errors.f_anio = 'El Año no puede modificarse (%s)' % (r.f_anio)
    else:
        #verificamos que no sea un anio repetido
        r = db(db.t_egresados.f_anio==form.vars.f_anio).select().first()
        print(r)
        if r != None:
            form.errors.f_anio = 'El Año (%s) ya esta ingresado. Por favor actualicelo' % (r.f_anio)
