# Generated by Django 3.1.11 on 2021-07-05 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admisiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_e', models.CharField(blank=True, max_length=50, null=True)),
                ('contar_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('cohorte_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('sem_actual_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('num_doc_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('estrato_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('cod_estado_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('nom_estado_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('prom_acu_ad_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('reliq_casos_esp_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('ult_exos_aplicadas_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('opcion_de_ingreso_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('modalidad_de_ingreso_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('cupo_especial_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('prom_sem_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('porc_cred_oblig_aprobados_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('nom_situacion_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('cod_situacion_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('readmisiones_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('periodos_readmisiones_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('plan_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('cod_pro_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('programa_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('facultad_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('gano_ingles_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_colegio_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('origen_colegio_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('sexo_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad_origen_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad_residencia_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('departamento_origen_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('departamento_residencia_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('colegio_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('edad_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('nacimiento_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('anio_undecimo_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('pago_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('modalidad_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('nivel_estudio_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('mencion_de_grado_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_de_grado_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('saber_11_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('saber_pro_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('ultimo_periodo_academico_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('ultimo_periodo_pagado_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('ultimo_tipo_de_pagado_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('ultimo_valor_pagado_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('ultimo_periodo_liquidado_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('ultimo_valor_liquidado_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('total_periodos_academicos_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('total_periodos_pagados_ad', models.CharField(blank=True, max_length=50, null=True)),
                ('puntaje_admision_ad', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'admisiones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'colegio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'competencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cohorte', models.IntegerField(blank=True, null=True)),
                ('sem_actual', models.IntegerField(blank=True, null=True)),
                ('estrato', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('promedio_acumulado', models.IntegerField(blank=True, null=True)),
                ('reliq_casos_especiales', models.IntegerField(blank=True, null=True)),
                ('opcion_ingeso', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_ingreso', models.CharField(blank=True, max_length=50, null=True)),
                ('cupo_especial_ingreso', models.CharField(blank=True, max_length=50, null=True)),
                ('ult_promedio_semestral', models.IntegerField(blank=True, null=True)),
                ('porc_creditos_aprobados', models.IntegerField(blank=True, null=True)),
                ('nombre_situacion', models.CharField(blank=True, max_length=50, null=True)),
                ('numero_readmisiones', models.IntegerField(blank=True, null=True)),
                ('numero_plan', models.IntegerField(blank=True, null=True)),
                ('gano_examen_ingles', models.IntegerField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.CharField(blank=True, max_length=50, null=True)),
                ('anyo_11', models.IntegerField(blank=True, null=True)),
                ('pago_sem_actual', models.CharField(blank=True, max_length=50, null=True)),
                ('modalidad', models.CharField(blank=True, max_length=50, null=True)),
                ('nivel_estudio', models.CharField(blank=True, max_length=50, null=True)),
                ('mencion_honorofica', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_grado', models.CharField(blank=True, max_length=50, null=True)),
                ('saber11', models.CharField(blank=True, max_length=50, null=True)),
                ('saberpro', models.CharField(blank=True, max_length=50, null=True)),
                ('ult_periodo_academico', models.CharField(blank=True, max_length=50, null=True)),
                ('ult_periodo_pagado', models.CharField(blank=True, max_length=50, null=True)),
                ('ult_tipo_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('ult_valor_pagado', models.IntegerField(blank=True, null=True)),
                ('ult_periodo_liquidado', models.CharField(blank=True, max_length=50, null=True)),
                ('ult_valor_liquidado', models.IntegerField(blank=True, null=True)),
                ('total_periodos_academicos', models.IntegerField(blank=True, null=True)),
                ('total_periodos_pagados', models.IntegerField(blank=True, null=True)),
                ('puntaje_admision', models.IntegerField(blank=True, null=True)),
                ('num_documento', models.CharField(blank=True, max_length=50, null=True)),
                ('num_registro', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'estudiante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'facultad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'periodo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Planeacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_documento', models.CharField(blank=True, max_length=50, null=True)),
                ('documento', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('numero_de_registro', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_de_evaluado', models.CharField(blank=True, max_length=50, null=True)),
                ('snies_programa_académico', models.CharField(blank=True, max_length=50, null=True)),
                ('programa', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('grupo_de_referencia', models.CharField(blank=True, max_length=50, null=True)),
                ('puntaje_global', models.CharField(blank=True, max_length=50, null=True)),
                ('percentil_nacional_global', models.CharField(blank=True, max_length=50, null=True)),
                ('percentil_grupo_de_referencia', models.CharField(blank=True, max_length=50, null=True)),
                ('modulo', models.CharField(blank=True, max_length=50, null=True)),
                ('puntaje_modulo', models.CharField(blank=True, max_length=50, null=True)),
                ('nivel_de_desempeno', models.CharField(blank=True, max_length=50, null=True)),
                ('percentil_nacional_modulo', models.CharField(blank=True, max_length=50, null=True)),
                ('percentil_grupo_de_referencia_modulo', models.CharField(blank=True, max_length=50, null=True)),
                ('novedades', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'planeacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('cod_prog', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'programa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Readmisiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'readmisiones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField(blank=True, null=True)),
                ('percentil_nal', models.IntegerField(blank=True, null=True)),
                ('persentil_grupo', models.IntegerField(blank=True, null=True)),
                ('nivel_desemp', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'resultados',
                'managed': False,
            },
        ),
    ]