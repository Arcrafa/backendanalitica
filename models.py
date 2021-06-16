# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admisiones(models.Model):
    codigo_e = models.CharField(max_length=-1, blank=True, null=True)
    contar_ad = models.CharField(max_length=-1, blank=True, null=True)
    cohorte_ad = models.CharField(max_length=-1, blank=True, null=True)
    sem_actual_ad = models.CharField(max_length=-1, blank=True, null=True)
    num_doc_ad = models.CharField(max_length=-1, blank=True, null=True)
    estrato_ad = models.CharField(max_length=-1, blank=True, null=True)
    cod_estado_ad = models.CharField(max_length=-1, blank=True, null=True)
    nom_estado_ad = models.CharField(max_length=-1, blank=True, null=True)
    prom_acu_ad_ad = models.CharField(max_length=-1, blank=True, null=True)
    reliq_casos_esp_ad = models.CharField(max_length=-1, blank=True, null=True)
    ult_exos_aplicadas_ad = models.CharField(max_length=-1, blank=True, null=True)
    opcion_de_ingreso_ad = models.CharField(max_length=-1, blank=True, null=True)
    modalidad_de_ingreso_ad = models.CharField(max_length=-1, blank=True, null=True)
    cupo_especial_ad = models.CharField(max_length=-1, blank=True, null=True)
    prom_sem_ad = models.CharField(max_length=-1, blank=True, null=True)
    porc_cred_oblig_aprobados_ad = models.CharField(max_length=-1, blank=True, null=True)
    nom_situacion_ad = models.CharField(max_length=-1, blank=True, null=True)
    cod_situacion_ad = models.CharField(max_length=-1, blank=True, null=True)
    readmisiones_ad = models.CharField(max_length=-1, blank=True, null=True)
    periodos_readmisiones_ad = models.CharField(max_length=-1, blank=True, null=True)
    plan_ad = models.CharField(max_length=-1, blank=True, null=True)
    cod_pro_ad = models.CharField(max_length=-1, blank=True, null=True)
    programa_ad = models.CharField(max_length=-1, blank=True, null=True)
    facultad_ad = models.CharField(max_length=-1, blank=True, null=True)
    gano_ingles_ad = models.CharField(max_length=-1, blank=True, null=True)
    tipo_colegio_ad = models.CharField(max_length=-1, blank=True, null=True)
    origen_colegio_ad = models.CharField(max_length=-1, blank=True, null=True)
    sexo_ad = models.CharField(max_length=-1, blank=True, null=True)
    ciudad_origen_ad = models.CharField(max_length=-1, blank=True, null=True)
    ciudad_residencia_ad = models.CharField(max_length=-1, blank=True, null=True)
    departamento_origen_ad = models.CharField(max_length=-1, blank=True, null=True)
    departamento_residencia_ad = models.CharField(max_length=-1, blank=True, null=True)
    colegio_ad = models.CharField(max_length=-1, blank=True, null=True)
    edad_ad = models.CharField(max_length=-1, blank=True, null=True)
    nacimiento_ad = models.CharField(max_length=-1, blank=True, null=True)
    anio_undecimo_ad = models.CharField(max_length=-1, blank=True, null=True)
    pago_ad = models.CharField(max_length=-1, blank=True, null=True)
    modalidad_ad = models.CharField(max_length=-1, blank=True, null=True)
    nivel_estudio_ad = models.CharField(max_length=-1, blank=True, null=True)
    mencion_de_grado_ad = models.CharField(max_length=-1, blank=True, null=True)
    fecha_de_grado_ad = models.CharField(max_length=-1, blank=True, null=True)
    saber_11_ad = models.CharField(max_length=-1, blank=True, null=True)
    saber_pro_ad = models.CharField(max_length=-1, blank=True, null=True)
    ultimo_periodo_academico_ad = models.CharField(max_length=-1, blank=True, null=True)
    ultimo_periodo_pagado_ad = models.CharField(max_length=-1, blank=True, null=True)
    ultimo_tipo_de_pagado_ad = models.CharField(max_length=-1, blank=True, null=True)
    ultimo_valor_pagado_ad = models.CharField(max_length=-1, blank=True, null=True)
    ultimo_periodo_liquidado_ad = models.CharField(max_length=-1, blank=True, null=True)
    ultimo_valor_liquidado_ad = models.CharField(max_length=-1, blank=True, null=True)
    total_periodos_academicos_ad = models.CharField(max_length=-1, blank=True, null=True)
    total_periodos_pagados_ad = models.CharField(max_length=-1, blank=True, null=True)
    puntaje_admision_ad = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admisiones'


class Archivo(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=-1, blank=True, null=True)
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    new_file = models.CharField(max_length=-1, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'archivo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Ciudad(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Competencia(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competencia'


class Departamento(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estudiante(models.Model):
    codigo = models.CharField(primary_key=True, max_length=-1)
    cohorte = models.IntegerField(blank=True, null=True)
    sem_actual = models.IntegerField(blank=True, null=True)
    estrato = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=-1, blank=True, null=True)
    promedio_acumulado = models.IntegerField(blank=True, null=True)
    reliq_casos_especiales = models.IntegerField(blank=True, null=True)
    opcion_ingeso = models.CharField(max_length=-1, blank=True, null=True)
    tipo_ingreso = models.CharField(max_length=-1, blank=True, null=True)
    cupo_especial_ingreso = models.CharField(max_length=-1, blank=True, null=True)
    ult_promedio_semestral = models.IntegerField(blank=True, null=True)
    porc_creditos_aprobados = models.IntegerField(blank=True, null=True)
    nombre_situacion = models.CharField(max_length=-1, blank=True, null=True)
    numero_readmisiones = models.IntegerField(blank=True, null=True)
    numero_plan = models.IntegerField(blank=True, null=True)
    codigo_programa = models.IntegerField(blank=True, null=True)
    programa = models.CharField(max_length=-1, blank=True, null=True)
    facultad = models.CharField(max_length=-1, blank=True, null=True)
    gano_examen_ingles = models.IntegerField(blank=True, null=True)
    tipo_colegio = models.CharField(max_length=-1, blank=True, null=True)
    colegioumento = models.CharField(max_length=-1, blank=True, null=True)
    sexo = models.CharField(max_length=-1, blank=True, null=True)
    colegio = models.CharField(max_length=-1, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    anyo_11 = models.IntegerField(blank=True, null=True)
    pago_sem_actual = models.CharField(max_length=-1, blank=True, null=True)
    modalidad = models.CharField(max_length=-1, blank=True, null=True)
    nivel_estudio = models.CharField(max_length=-1, blank=True, null=True)
    mencion_honorofica = models.CharField(max_length=-1, blank=True, null=True)
    fecha_grado = models.CharField(max_length=-1, blank=True, null=True)
    saber11 = models.CharField(max_length=-1, blank=True, null=True)
    saberpro = models.CharField(max_length=-1, blank=True, null=True)
    ult_periodo_academico = models.CharField(max_length=-1, blank=True, null=True)
    ult_periodo_pagado = models.CharField(max_length=-1, blank=True, null=True)
    ult_tipo_pago = models.CharField(max_length=-1, blank=True, null=True)
    ult_valor_pagado = models.IntegerField(blank=True, null=True)
    ult_periodo_liquidado = models.CharField(max_length=-1, blank=True, null=True)
    ult_valor_liquidado = models.IntegerField(blank=True, null=True)
    total_periodos_academicos = models.IntegerField(blank=True, null=True)
    total_periodos_pagados = models.IntegerField(blank=True, null=True)
    puntaje_admision = models.IntegerField(blank=True, null=True)
    condigo_joven_en_accion = models.CharField(max_length=-1, blank=True, null=True)
    tipo_doc = models.CharField(max_length=-1, blank=True, null=True)
    num_documento = models.CharField(max_length=-1, blank=True, null=True)
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    num_registro = models.CharField(max_length=-1, blank=True, null=True)
    tipo_evaluado = models.CharField(max_length=-1, blank=True, null=True)
    novedades = models.IntegerField(blank=True, null=True)
    periodo_exam = models.CharField(max_length=-1, blank=True, null=True)
    prom_acum_exam = models.IntegerField(blank=True, null=True)
    ciudad_origen = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_origen', blank=True, null=True)
    programa_0 = models.ForeignKey('Programa', models.DO_NOTHING, db_column='programa_id', blank=True,
                                   null=True)  # Field renamed because of name conflict.
    ciudad_residencia = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_residencia', blank=True,
                                          null=True)
    ciudad_colegio = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_colegio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'


class Exoneracion(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exoneracion'


class ExoneracionEstudiante(models.Model):
    id = models.ForeignKey(Exoneracion, models.DO_NOTHING, db_column='id', blank=True, null=True)
    estudiante_codigo = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='estudiante_codigo', blank=True,
                                          null=True)

    class Meta:
        managed = False
        db_table = 'exoneracion_estudiante'


class Facultad(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facultad'


class Periodo(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'


class Planeacion(models.Model):
    tipo_de_documento = models.CharField(max_length=-1, blank=True, null=True)
    documento = models.CharField(max_length=-1, blank=True, null=True)
    codigo = models.CharField(max_length=-1, blank=True, null=True)
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    numero_de_registro = models.CharField(max_length=-1, blank=True, null=True)
    tipo_de_evaluado = models.CharField(max_length=-1, blank=True, null=True)
    snies_programa_académico = models.CharField(max_length=-1, blank=True, null=True)
    programa = models.CharField(max_length=-1, blank=True, null=True)
    ciudad = models.CharField(max_length=-1, blank=True, null=True)
    grupo_de_referencia = models.CharField(max_length=-1, blank=True, null=True)
    puntaje_global = models.CharField(max_length=-1, blank=True, null=True)
    percentil_nacional_global = models.CharField(max_length=-1, blank=True, null=True)
    percentil_grupo_de_referencia = models.CharField(max_length=-1, blank=True, null=True)
    modulo = models.CharField(max_length=-1, blank=True, null=True)
    puntaje_modulo = models.CharField(max_length=-1, blank=True, null=True)
    nivel_de_desempeno = models.CharField(max_length=-1, blank=True, null=True)
    percentil_nacional_modulo = models.CharField(max_length=-1, blank=True, null=True)
    percentil_grupo_de_referencia_modulo = models.CharField(max_length=-1, blank=True, null=True)
    novedades = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planeacion'


class Programa(models.Model):
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    cod_prog = models.IntegerField(blank=True, null=True)
    facultad = models.ForeignKey(Facultad, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programa'


class Readmisiones(models.Model):
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING, blank=True, null=True)
    estudiante_codigo = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='estudiante_codigo', blank=True,
                                          null=True)

    class Meta:
        managed = False
        db_table = 'readmisiones'


class Resultados(models.Model):
    competencia = models.ForeignKey(Competencia, models.DO_NOTHING, blank=True, null=True)
    estudiante_codigo = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='estudiante_codigo', blank=True,
                                          null=True)
    puntaje = models.IntegerField(blank=True, null=True)
    percentil_nal = models.IntegerField(blank=True, null=True)
    persentil_grupo = models.IntegerField(blank=True, null=True)
    nivel_desemp = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resultados'
        unique_together = (('competencia', 'estudiante_codigo'),)


class SaberproSaberpro(models.Model):
    field1 = models.IntegerField(blank=True, null=True)
    codigo = models.IntegerField(primary_key=True)
    cohorte = models.IntegerField(blank=True, null=True)
    sem_actual = models.IntegerField(blank=True, null=True)
    estrato = models.IntegerField(blank=True, null=True)
    codigo_estado = models.CharField(max_length=1, blank=True, null=True)
    estado = models.CharField(max_length=8, blank=True, null=True)
    promedio_acumulado = models.IntegerField(blank=True, null=True)
    reliq_casos_especiales = models.IntegerField(blank=True, null=True)
    ult_exos_aplicadas = models.CharField(max_length=79, blank=True, null=True)
    opcion_ingeso = models.CharField(max_length=1, blank=True, null=True)
    tipo_ingreso = models.CharField(max_length=11, blank=True, null=True)
    cupo_especial_ingreso = models.CharField(max_length=7, blank=True, null=True)
    ult_promedio_semestral = models.IntegerField(blank=True, null=True)
    porc_creditos_aprobados = models.IntegerField(blank=True, null=True)
    nombre_situacion = models.CharField(max_length=22, blank=True, null=True)
    codigo_situacion_estudiante = models.CharField(max_length=1, blank=True, null=True)
    numero_readmisiones = models.IntegerField(blank=True, null=True)
    peridos_readmisiones = models.CharField(max_length=21, blank=True, null=True)
    numero_plan = models.IntegerField(blank=True, null=True)
    codigo_programa = models.IntegerField(blank=True, null=True)
    programa = models.CharField(max_length=26, blank=True, null=True)
    facultad = models.CharField(max_length=47, blank=True, null=True)
    gano_examen_ingles = models.TextField(blank=True, null=True)
    tipo_colegio = models.CharField(max_length=7, blank=True, null=True)
    colegioumento = models.CharField(max_length=22, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    ciudad_origen = models.CharField(max_length=11, blank=True, null=True)
    ciudad_residencia = models.CharField(max_length=11, blank=True, null=True)
    dpto_origen = models.CharField(max_length=9, blank=True, null=True)
    dpto_residencia = models.CharField(max_length=9, blank=True, null=True)
    colegio = models.CharField(max_length=43, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    anyo_11 = models.TextField(blank=True, null=True)
    pago_sem_actual = models.CharField(max_length=12, blank=True, null=True)
    modalidad = models.CharField(max_length=1, blank=True, null=True)
    nivel_estudio = models.CharField(max_length=2, blank=True, null=True)
    mencion_honorofica = models.CharField(max_length=7, blank=True, null=True)
    fecha_grado = models.CharField(max_length=10, blank=True, null=True)
    saber11 = models.CharField(max_length=14, blank=True, null=True)
    saberpro = models.CharField(max_length=14, blank=True, null=True)
    ult_periodo_academico = models.CharField(max_length=6, blank=True, null=True)
    ult_periodo_pagado = models.CharField(max_length=6, blank=True, null=True)
    ult_tipo_pago = models.CharField(max_length=23, blank=True, null=True)
    ult_valor_pagado = models.IntegerField(blank=True, null=True)
    ult_periodo_liquidado = models.CharField(max_length=6, blank=True, null=True)
    ult_valor_liquidado = models.IntegerField(blank=True, null=True)
    total_periodos_academicos = models.IntegerField(blank=True, null=True)
    total_periodos_pagados = models.IntegerField(blank=True, null=True)
    puntaje_admision = models.IntegerField(blank=True, null=True)
    condigo_joven_en_accion = models.CharField(max_length=1, blank=True, null=True)
    tipo_doc = models.CharField(max_length=2, blank=True, null=True)
    num_documento_y = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=31, blank=True, null=True)
    num_registro = models.CharField(max_length=14, blank=True, null=True)
    tipo_evaluado = models.CharField(max_length=10, blank=True, null=True)
    snies_prg = models.IntegerField(blank=True, null=True)
    cprog = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=11, blank=True, null=True)
    grupo_ref = models.CharField(max_length=23, blank=True, null=True)
    puntaje_global = models.IntegerField(blank=True, null=True)
    percentil_nal_global = models.IntegerField(blank=True, null=True)
    percentil_grupo_ref = models.IntegerField(blank=True, null=True)
    novedades = models.IntegerField(blank=True, null=True)
    nivel_desemp_competencias_ciudadanas = models.IntegerField(blank=True, null=True)
    nivel_desemp_comunicacion_escrita = models.IntegerField(blank=True, null=True)
    nivel_desemp_ingles = models.CharField(max_length=3, blank=True, null=True)
    nivel_desemp_lectura_critica = models.IntegerField(blank=True, null=True)
    nivel_desemp_razonamiento_cuantitativo = models.IntegerField(blank=True, null=True)
    percentil_grupo_ref_mod_competencias_ciudadanas = models.IntegerField(blank=True, null=True)
    percentil_grupo_ref_mod_comunicacion_escrita = models.IntegerField(blank=True, null=True)
    percentil_grupo_ref_mod_ingles = models.IntegerField(blank=True, null=True)
    percentil_grupo_ref_mod_lectura_critica = models.IntegerField(blank=True, null=True)
    percentil_grupo_ref_mod_razonamiento_cuantitativo = models.IntegerField(blank=True, null=True)
    percentil_nal_mod_competencias_ciudadanas = models.IntegerField(blank=True, null=True)
    percentil_nal_mod_comunicacion_escrita = models.IntegerField(blank=True, null=True)
    percentil_nal_mod_ingles = models.IntegerField(blank=True, null=True)
    percentil_nal_mod_lectura_critica = models.IntegerField(blank=True, null=True)
    percentil_nal_mod_razonamiento_cuantitativo = models.IntegerField(blank=True, null=True)
    puntaje_mod_competencias_ciudadanas = models.IntegerField(blank=True, null=True)
    puntaje_mod_comunicacion_escrita = models.IntegerField(blank=True, null=True)
    puntaje_mod_ingles = models.IntegerField(blank=True, null=True)
    puntaje_mod_lectura_critica = models.IntegerField(blank=True, null=True)
    puntaje_mod_razonamiento_cuantitativo = models.IntegerField(blank=True, null=True)
    periodo_exam = models.CharField(max_length=6, blank=True, null=True)
    prom_acum_exam = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saberpro_saberpro'
