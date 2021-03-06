response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Inicio'),URL('default','index')==URL(),URL('default','index'),[]),
]

if auth.user:
    groups = db((db.auth_membership.user_id==auth.user.id)& (db.auth_membership.group_id==db.auth_group.id)).select(db.auth_group.role)
    for group in groups:
        if group.role =='titulos':
            response.menu.append(('Titulos',  URL()==URL('titulos','impresos'), URL('impresos','titulos_impresos')))
        if group.role =='egresados':
            response.menu.append(('Egresados', URL()==URL('titulos','egresados'), URL('egresados','cargarEgresados')))
        if group.role =='auditados':
            response.menu.append(('Auditados', URL()==URL('titulos','auditados'), URL('auditados','cargarAuditados')))
        if group.role =='autoridades':
            response.menu.append(('Vision', False, None,[
                        ('Auditados', URL()==URL('autoridades', 'auditados'), URL('autoridades', 'auditados')),
                        ('Egresados', URL()==URL('autoridades', 'egresados'), URL('autoridades', 'egresados')),
                        ('Impresos', URL()==URL('autoridades', 'auditados'), URL('autoridades', 'impresos')),
                    ]))

        if group.role =='estadisticas':
            response.menu.append(('Estadisticas', False, None,[
                        ('Auditados', URL()==URL('titulos', 'estadisticas'), URL('estadisticas', 'auditados')),
                        ('Egresados', URL()==URL('titulos', 'estadisticas'), URL('estadisticas', 'egresados')),
                        ('Impresos', URL()==URL('titulos', 'estadisticas'), URL('estadisticas', 'impresos')),
                    ]))
            response.menu.append(('Graficos', False, None,[
                      #  ('Auditados', URL()==URL('titulos', 'graficos'), URL('graficos', 'auditados')),
                        ('Egresados', URL()==URL('titulos', 'graficos'), URL('graficos', 'otro')),
                      #  ('Impresos', URL()==URL('titulos', 'graficos'), URL('graficos', 'impresos')),
                    ]))
