from django.db import models


class Archivo(models.Model):
    # id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    new_file = models.FileField(upload_to="archivos/", null=True, blank=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'archivo'


class Admisiones(models.Model):
    codigo_e = models.CharField(max_length=50, blank=True, null=True)
    contar_ad = models.CharField(max_length=50, blank=True, null=True)
    cohorte_ad = models.CharField(max_length=50, blank=True, null=True)
    sem_actual_ad = models.CharField(max_length=50, blank=True, null=True)
    num_doc_ad = models.CharField(max_length=50, blank=True, null=True)
    estrato_ad = models.CharField(max_length=50, blank=True, null=True)
    cod_estado_ad = models.CharField(max_length=50, blank=True, null=True)
    nom_estado_ad = models.CharField(max_length=50, blank=True, null=True)
    prom_acu_ad_ad = models.CharField(max_length=50, blank=True, null=True)
    reliq_casos_esp_ad = models.CharField(max_length=50, blank=True, null=True)
    ult_exos_aplicadas_ad = models.CharField(max_length=50, blank=True, null=True)
    opcion_de_ingreso_ad = models.CharField(max_length=50, blank=True, null=True)
    modalidad_de_ingreso_ad = models.CharField(max_length=50, blank=True, null=True)
    cupo_especial_ad = models.CharField(max_length=50, blank=True, null=True)
    prom_sem_ad = models.CharField(max_length=50, blank=True, null=True)
    porc_cred_oblig_aprobados_ad = models.CharField(max_length=50, blank=True, null=True)
    nom_situacion_ad = models.CharField(max_length=50, blank=True, null=True)
    cod_situacion_ad = models.CharField(max_length=50, blank=True, null=True)
    readmisiones_ad = models.CharField(max_length=50, blank=True, null=True)
    periodos_readmisiones_ad = models.CharField(max_length=50, blank=True, null=True)
    plan_ad = models.CharField(max_length=50, blank=True, null=True)
    cod_pro_ad = models.CharField(max_length=50, blank=True, null=True)
    programa_ad = models.CharField(max_length=50, blank=True, null=True)
    facultad_ad = models.CharField(max_length=50, blank=True, null=True)
    gano_ingles_ad = models.CharField(max_length=50, blank=True, null=True)
    tipo_colegio_ad = models.CharField(max_length=50, blank=True, null=True)
    origen_colegio_ad = models.CharField(max_length=50, blank=True, null=True)
    sexo_ad = models.CharField(max_length=50, blank=True, null=True)
    ciudad_origen_ad = models.CharField(max_length=50, blank=True, null=True)
    ciudad_residencia_ad = models.CharField(max_length=50, blank=True, null=True)
    departamento_origen_ad = models.CharField(max_length=50, blank=True, null=True)
    departamento_residencia_ad = models.CharField(max_length=50, blank=True, null=True)
    colegio_ad = models.CharField(max_length=50, blank=True, null=True)
    edad_ad = models.CharField(max_length=50, blank=True, null=True)
    nacimiento_ad = models.CharField(max_length=50, blank=True, null=True)
    anio_undecimo_ad = models.CharField(max_length=50, blank=True, null=True)
    pago_ad = models.CharField(max_length=50, blank=True, null=True)
    modalidad_ad = models.CharField(max_length=50, blank=True, null=True)
    nivel_estudio_ad = models.CharField(max_length=50, blank=True, null=True)
    mencion_de_grado_ad = models.CharField(max_length=50, blank=True, null=True)
    fecha_de_grado_ad = models.CharField(max_length=50, blank=True, null=True)
    saber_11_ad = models.CharField(max_length=50, blank=True, null=True)
    saber_pro_ad = models.CharField(max_length=50, blank=True, null=True)
    ultimo_periodo_academico_ad = models.CharField(max_length=50, blank=True, null=True)
    ultimo_periodo_pagado_ad = models.CharField(max_length=50, blank=True, null=True)
    ultimo_tipo_de_pagado_ad = models.CharField(max_length=50, blank=True, null=True)
    ultimo_valor_pagado_ad = models.CharField(max_length=50, blank=True, null=True)
    ultimo_periodo_liquidado_ad = models.CharField(max_length=50, blank=True, null=True)
    ultimo_valor_liquidado_ad = models.CharField(max_length=50, blank=True, null=True)
    total_periodos_academicos_ad = models.CharField(max_length=50, blank=True, null=True)
    total_periodos_pagados_ad = models.CharField(max_length=50, blank=True, null=True)
    puntaje_admision_ad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admisiones'


class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Colegio(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad', blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colegio'


class Competencia(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competencia'


class Departamento(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class Estudiante(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20)
    cohorte = models.IntegerField(blank=True, null=True)
    sem_actual = models.IntegerField(blank=True, null=True)
    estrato = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    promedio_acumulado = models.IntegerField(blank=True, null=True)
    reliq_casos_especiales = models.IntegerField(blank=True, null=True)
    opcion_ingeso = models.CharField(max_length=50, blank=True, null=True)
    tipo_ingreso = models.CharField(max_length=50, blank=True, null=True)
    cupo_especial_ingreso = models.CharField(max_length=50, blank=True, null=True)
    ult_promedio_semestral = models.IntegerField(blank=True, null=True)
    porc_creditos_aprobados = models.IntegerField(blank=True, null=True)
    nombre_situacion = models.CharField(max_length=50, blank=True, null=True)
    numero_readmisiones = models.IntegerField(blank=True, null=True)
    numero_plan = models.IntegerField(blank=True, null=True)
    gano_examen_ingles = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.CharField(max_length=50, blank=True, null=True)
    anyo_11 = models.IntegerField(blank=True, null=True)
    pago_sem_actual = models.CharField(max_length=50, blank=True, null=True)
    modalidad = models.CharField(max_length=50, blank=True, null=True)
    nivel_estudio = models.CharField(max_length=50, blank=True, null=True)
    mencion_honorofica = models.CharField(max_length=50, blank=True, null=True)
    fecha_grado = models.CharField(max_length=50, blank=True, null=True)
    saber11 = models.CharField(max_length=50, blank=True, null=True)
    saberpro = models.CharField(max_length=50, blank=True, null=True)
    ult_periodo_academico = models.CharField(max_length=50, blank=True, null=True)
    ult_periodo_pagado = models.CharField(max_length=50, blank=True, null=True)
    ult_tipo_pago = models.CharField(max_length=50, blank=True, null=True)
    ult_valor_pagado = models.IntegerField(blank=True, null=True)
    ult_periodo_liquidado = models.CharField(max_length=50, blank=True, null=True)
    ult_valor_liquidado = models.IntegerField(blank=True, null=True)
    total_periodos_academicos = models.IntegerField(blank=True, null=True)
    total_periodos_pagados = models.IntegerField(blank=True, null=True)
    puntaje_admision = models.IntegerField(blank=True, null=True)
    num_documento = models.CharField(max_length=50, blank=True, null=True)
    num_registro = models.CharField(max_length=50, blank=True, null=True)
    ciudad_origen = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_origen', blank=True, null=True,
                                      related_name="ciudad_origen")
    programa = models.ForeignKey('Programa', models.DO_NOTHING, blank=True, null=True)
    ciudad_residencia = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_residencia', blank=True,
                                          null=True,related_name="ciudad_residencia")
    colegio = models.ForeignKey(Colegio, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'


class Facultad(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facultad'


class Periodo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'


class Planeacion(models.Model):
    tipo_de_documento = models.CharField(max_length=50, blank=True, null=True)
    documento = models.CharField(max_length=50, blank=True, null=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    numero_de_registro = models.CharField(max_length=50, blank=True, null=True)
    tipo_de_evaluado = models.CharField(max_length=50, blank=True, null=True)
    snies_programa_académico = models.CharField(max_length=50, blank=True, null=True)
    programa = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    grupo_de_referencia = models.CharField(max_length=50, blank=True, null=True)
    puntaje_global = models.CharField(max_length=50, blank=True, null=True)
    percentil_nacional_global = models.CharField(max_length=50, blank=True, null=True)
    percentil_grupo_de_referencia = models.CharField(max_length=50, blank=True, null=True)
    modulo = models.CharField(max_length=50, blank=True, null=True)
    puntaje_modulo = models.CharField(max_length=50, blank=True, null=True)
    nivel_de_desempeno = models.CharField(max_length=50, blank=True, null=True)
    percentil_nacional_modulo = models.CharField(max_length=50, blank=True, null=True)
    percentil_grupo_de_referencia_modulo = models.CharField(max_length=50, blank=True, null=True)
    novedades = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planeacion'


class Programa(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    cod_prog = models.IntegerField(blank=True, null=True)
    facultad = models.ForeignKey(Facultad, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programa'


class Readmisiones(models.Model):
    # periodo = models.ForeignKey(Periodo, models.DO_NOTHING, blank=True, null=True)
    # estudiante_codigo = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='estudiante_codigo', blank=True,                                      null=True)

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
    nivel_desemp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resultados'
        unique_together = (('competencia', 'estudiante_codigo'),)
