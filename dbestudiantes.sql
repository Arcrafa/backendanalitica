SET DATESTYLE TO EUROPEAN;

DROP TABLE IF EXISTS
    public.Archivo,
    public.Ciudad,
    public.Competencia,
    public.Departamento,
    public.Estudiante,
    public.Exoneracion,
    public.Exoneracion_estudiante,
    public.Facultad,
    public.Periodo,
    public.Programa,
    public.Readmisiones,
    public.Resultados,
    public.colegio
    CASCADE;
CREATE EXTENSION IF NOT EXISTS unaccent;
DROP FOREIGN TABLE IF EXISTS
    public.Admisiones,
    public.Planeacion,
    public.talento;

CREATE SEQUENCE if not exists Departamento_id_seq;

CREATE TABLE public.Departamento
(
    id     INTEGER NOT NULL DEFAULT nextval('Departamento_id_seq'),
    nombre VARCHAR,
    CONSTRAINT PK_departamento PRIMARY KEY (id)
);
ALTER SEQUENCE Departamento_id_seq
    OWNED BY public.Departamento.id;

CREATE SEQUENCE if not exists Ciudad_id_seq;
CREATE TABLE public.Ciudad
(
    id              INTEGER NOT NULL DEFAULT nextval('Ciudad_id_seq'),
    nombre          VARCHAR,
    departamento_id INTEGER,
    CONSTRAINT PK_ciudad PRIMARY KEY (id)
);
ALTER SEQUENCE Ciudad_id_seq
    OWNED BY public.Ciudad.id;

CREATE SEQUENCE if not exists Competencia_id_seq;
CREATE TABLE public.Competencia
(
    id     INTEGER NOT NULL DEFAULT nextval('Competencia_id_seq'),
    nombre VARCHAR,
    CONSTRAINT PK_competencia PRIMARY KEY (id)
);
ALTER SEQUENCE Competencia_id_seq
    OWNED BY public.Competencia.id;

CREATE SEQUENCE if not exists Periodo_id_seq;
CREATE TABLE public.Periodo
(
    id     INTEGER NOT NULL DEFAULT nextval('Periodo_id_seq'),
    nombre VARCHAR,
    CONSTRAINT PK_periodo PRIMARY KEY (id)
);
ALTER SEQUENCE Periodo_id_seq
    OWNED BY public.Periodo.id;

CREATE SEQUENCE if not exists Exoneracion_id_seq;
CREATE TABLE public.Exoneracion
(
    id     INTEGER NOT NULL DEFAULT nextval('Exoneracion_id_seq'),
    nombre VARCHAR,
    CONSTRAINT PK_exoneracion PRIMARY KEY (id)
);
ALTER SEQUENCE Exoneracion_id_seq
    OWNED BY public.Exoneracion.id;

CREATE SEQUENCE if not exists Colegio_id_seq;

CREATE TABLE IF NOT EXISTS public.Colegio
(
    id        INTEGER NOT NULL DEFAULT nextval('Colegio_id_seq'),
    nombre    varchar,
    id_ciudad int,
    tipo      varchar,
    CONSTRAINT colegio_pkey PRIMARY KEY (id)
);
ALTER SEQUENCE Colegio_id_seq
    OWNED BY public.Colegio.id;

CREATE TABLE public.Estudiante
(
    codigo                    VARCHAR NOT NULL,
    cohorte                   INTEGER,
    sem_actual                INTEGER,
    estrato                   INTEGER,
    estado                    VARCHAR,
    promedio_acumulado        INTEGER,
    reliq_casos_especiales    INTEGER,
    opcion_ingeso             VARCHAR,
    tipo_ingreso              VARCHAR,
    cupo_especial_ingreso     VARCHAR,
    ult_promedio_semestral    INTEGER,
    porc_creditos_aprobados   INTEGER,
    nombre_situacion          VARCHAR,
    numero_readmisiones       INTEGER,
    numero_plan               INTEGER,
    gano_examen_ingles        INTEGER,
    sexo                      VARCHAR,
    fecha_nacimiento          varchar,
    anyo_11                   INTEGER,
    pago_sem_actual           VARCHAR,
    modalidad                 VARCHAR,
    nivel_estudio             VARCHAR,
    mencion_honorofica        VARCHAR,
    fecha_grado               VARCHAR,
    saber11                   VARCHAR,
    saberPro                  VARCHAR,
    ult_periodo_academico     VARCHAR,
    ult_periodo_pagado        VARCHAR,
    ult_tipo_pago             VARCHAR,
    ult_valor_pagado          INTEGER,
    ult_periodo_liquidado     VARCHAR,
    ult_valor_liquidado       INTEGER,
    total_periodos_academicos INTEGER,
    total_periodos_pagados    INTEGER,
    puntaje_admision          INTEGER,
    num_documento             varchar,
    num_registro              VARCHAR,
    ciudad_origen             INTEGER,
    programa_id               INTEGER,
    ciudad_residencia         INTEGER,
    colegio_id                INTEGER,
    CONSTRAINT PK_codigo PRIMARY KEY (codigo)
);
CREATE SEQUENCE if not exists Facultad_id_seq;

CREATE TABLE public.Facultad
(
    id     INTEGER NOT NULL DEFAULT nextval('Facultad_id_seq'),
    nombre VARCHAR,
    CONSTRAINT PK_facultad PRIMARY KEY (id)
)
;
ALTER SEQUENCE Exoneracion_id_seq
    OWNED BY public.Exoneracion.id;

CREATE SEQUENCE if not exists Programa_id_seq;
CREATE TABLE public.Programa
(
    id          INTEGER NOT NULL DEFAULT nextval('Programa_id_seq'),
    nombre      varchar,
    cod_prog    INTEGER,
    facultad_id INTEGER NOT NULL,
    CONSTRAINT PK_programa PRIMARY KEY (id)
);
ALTER SEQUENCE Programa_id_seq
    OWNED BY public.Programa.id;

CREATE SEQUENCE if not exists Resultados_id_seq;
CREATE TABLE public.Resultados
(
    id                INTEGER NOT NULL DEFAULT nextval('Resultados_id_seq'),
    competencia_id    INTEGER,
    estudiante_codigo VARCHAR,
    puntaje           INTEGER,
    percentil_nal     INTEGER,
    persentil_grupo   INTEGER,
    nivel_desemp      VARCHAR,
    CONSTRAINT PK_resultado PRIMARY KEY (id),
    UNIQUE (competencia_id, estudiante_codigo)
)
;
ALTER SEQUENCE Resultados_id_seq
    OWNED BY public.Resultados.id;
CREATE TABLE public.Readmisiones
(
    periodo_id        INTEGER,
    estudiante_codigo VARCHAR
)
;

CREATE TABLE public.Exoneracion_estudiante
(
    id                INTEGER,
    estudiante_codigo VARCHAR
)
;

/*============================================================================*/
/*                               FOREIGN KEYS                                 */
/*============================================================================*/
ALTER TABLE Ciudad
    ADD CONSTRAINT FK_REFERENCE_1
        FOREIGN KEY (departamento_id)
            REFERENCES Departamento (id)
;
ALTER TABLE Estudiante
    ADD CONSTRAINT FK_REFERENCE_18
        FOREIGN KEY (colegio_id)
            REFERENCES Colegio (id)
;

ALTER TABLE Estudiante
    ADD CONSTRAINT FK_REFERENCE_2
        FOREIGN KEY (ciudad_origen)
            REFERENCES Ciudad (id)
;

ALTER TABLE Estudiante
    ADD CONSTRAINT FK_REFERENCE_6
        FOREIGN KEY (programa_id)
            REFERENCES Programa (id)
;

ALTER TABLE Estudiante
    ADD CONSTRAINT FK_REFERENCE_11
        FOREIGN KEY (ciudad_residencia)
            REFERENCES Ciudad (id)
;
ALTER TABLE Estudiante
    ADD CONSTRAINT FK_REFERENCE_15
        FOREIGN KEY (ciudad_origen)
            REFERENCES Ciudad (id)
;



ALTER TABLE Programa
    ADD CONSTRAINT FK_REFERENCE_3
        FOREIGN KEY (facultad_id)
            REFERENCES Facultad (id)
;

ALTER TABLE Resultados
    ADD CONSTRAINT FK_REFERENCE_5
        FOREIGN KEY (estudiante_codigo)
            REFERENCES Estudiante (codigo)
;

ALTER TABLE Resultados
    ADD CONSTRAINT FK_REFERENCE_4
        FOREIGN KEY (competencia_id)
            REFERENCES Competencia (id)
;

ALTER TABLE Readmisiones
    ADD CONSTRAINT FK_REFERENCE_8
        FOREIGN KEY (estudiante_codigo)
            REFERENCES Estudiante (codigo)
;

ALTER TABLE Readmisiones
    ADD CONSTRAINT FK_REFERENCE_7
        FOREIGN KEY (periodo_id)
            REFERENCES Periodo (id)
;

ALTER TABLE Exoneracion_estudiante
    ADD CONSTRAINT FK_REFERENCE_9
        FOREIGN KEY (id)
            REFERENCES Exoneracion (id)
;

ALTER TABLE Exoneracion_estudiante
    ADD CONSTRAINT FK_REFERENCE_10
        FOREIGN KEY (estudiante_codigo)
            REFERENCES Estudiante (codigo)
;

ALTER TABLE Colegio
    ADD CONSTRAINT FK_REFERENCE_20
        FOREIGN KEY (id_ciudad)
            REFERENCES Ciudad (id)
;

CREATE SEQUENCE if not exists Archivo_id_seq;

CREATE TABLE IF NOT EXISTS public.Archivo
(
    id             INTEGER NOT NULL DEFAULT nextval('Archivo_id_seq'),
    descripcion    varchar,
    tipo           varchar,
    new_file       varchar,
    fecha_creacion date,
    estado         varchar,
    year           INTEGER,
    CONSTRAINT archivo_archivo_pkey PRIMARY KEY (id)
);
ALTER SEQUENCE Archivo_id_seq
    OWNED BY public.Archivo.id;


CREATE EXTENSION IF NOT EXISTS file_fdw;
CREATE SERVER IF NOT EXISTS files_csv FOREIGN DATA WRAPPER file_fdw;

CREATE FOREIGN TABLE Admisiones(

    codigo_e VARCHAR NOT NULL
    ,contar_ad VARCHAR
    ,COHORTE_ad VARCHAR
    ,SEM_ACTUAL_ad VARCHAR
    ,NUM_DOC_ad VARCHAR
    ,ESTRATO_ad VARCHAR
    ,COD_ESTADO_ad VARCHAR
    ,NOM_ESTADO_ad VARCHAR
    ,PROM_ACU_ad_ad VARCHAR
    ,RELIQ_CASOS_ESP_ad VARCHAR
    ,ULT_EXOS_APLICADAS_ad VARCHAR
    ,OPCION_DE_INGRESO_ad VARCHAR
    ,MODALIDAD_DE_INGRESO_ad VARCHAR
    ,CUPO_ESPECIAL_ad VARCHAR
    ,PROM_SEM_ad VARCHAR
    ,Porc_Cred_Oblig_Aprobados_ad VARCHAR
    ,NOM_SITUACION_ad VARCHAR
    ,COD_SITUACION_ad VARCHAR
    ,READMISIONES_ad VARCHAR
    ,PERIODOS_READMISIONES_ad VARCHAR
    ,PLAN_ad VARCHAR
    ,COD_PRO_ad VARCHAR
    ,PROGRAMA_ad VARCHAR
    ,FACULTAD_ad VARCHAR
    ,GANO_INGLES_ad VARCHAR
    ,TIPO_COLEGIO_ad VARCHAR
    ,ORIGEN_COLEGIO_ad VARCHAR
    ,SEXO_ad VARCHAR
    ,CIUDAD_ORIGEN_ad VARCHAR
    ,CIUDAD_RESIDENCIA_ad VARCHAR
    ,DEPARTAMENTO_ORIGEN_ad VARCHAR
    ,DEPARTAMENTO_RESIDENCIA_ad VARCHAR
    ,COLEGIO_ad VARCHAR
    ,EDAD_ad VARCHAR
    ,NACIMIENTO_ad VARCHAR
    ,ANIO_UNDECIMO_ad VARCHAR
    ,PAGO_ad VARCHAR
    ,MODALIDAD_ad VARCHAR
    ,NIVEL_ESTUDIO_ad VARCHAR
    ,MENCION_DE_GRADO_ad VARCHAR
    ,FECHA_DE_GRADO_ad VARCHAR
    ,SABER_11_ad VARCHAR
    ,SABER_PRO_ad VARCHAR
    ,ULTIMO_PERIODO_ACADEMICO_ad VARCHAR
    ,ULTIMO_PERIODO_PAGADO_ad VARCHAR
    ,ULTIMO_TIPO_DE_PAGADO_ad VARCHAR
    ,ULTIMO_VALOR_PAGADO_ad VARCHAR
    ,ULTIMO_PERIODO_LIQUIDADO_ad VARCHAR
    ,ULTIMO_VALOR_LIQUIDADO_ad VARCHAR
    ,TOTAL_PERIODOS_ACADEMICOS_ad VARCHAR
    ,TOTAL_PERIODOS_PAGADOS_ad VARCHAR
    ,PUNTAJE_ADMISION_ad VARCHAR
    ) SERVER files_csv
    OPTIONS ( filename '/var/lib/postgresql/data/archivos/blanco.csv', format 'csv' , delimiter ';', header 'true' );
CREATE FOREIGN TABLE Planeacion(
    tipo_de_documento VARCHAR
    ,documento VARCHAR
    ,codigo VARCHAR
    ,nombre VARCHAR
    ,numero_de_registro VARCHAR
    ,tipo_de_evaluado VARCHAR
    ,snies_programa_académico VARCHAR
    ,programa VARCHAR
    ,ciudad VARCHAR
    ,grupo_de_referencia VARCHAR
    ,puntaje_global VARCHAR
    ,percentil_nacional_global VARCHAR
    ,percentil_grupo_de_referencia VARCHAR
    ,modulo VARCHAR
    ,puntaje_modulo VARCHAR
    ,nivel_de_desempeno VARCHAR
    ,percentil_nacional_modulo VARCHAR
    ,percentil_grupo_de_referencia_modulo VARCHAR
    ,novedades VARCHAR
    ) SERVER files_csv
    OPTIONS ( filename '/var/lib/postgresql/data/archivos/blanco.csv', format 'csv', delimiter ';' , header 'true');
CREATE foreign TABLE Talento(
    COHORTE_INGRESO VARCHAR
    ,ULT_PERIODO_PAGO VARCHAR
    ,CODIGO_ESTUDIANTE VARCHAR
    ,FACULTAD VARCHAR
    ,PROGRAMA VARCHAR
    ,ESTADO_ACTUAL VARCHAR
    ,PROMEDIO_ACUMULADO VARCHAR
    ,NOMBRES VARCHAR
    ,APELLIDOS VARCHAR
    ,TIPO_DOCUMENTO VARCHAR
    ,NUMERO_DOCUMENTO VARCHAR
    ,CORREO_ELECTRONICO VARCHAR
    ,TELEFONO VARCHAR
    ,ESTRATO VARCHAR
    ,FECHA_NACIMIENTO VARCHAR
    ,DPTO_ORIGEN VARCHAR
    ,MPIO_ORIGEN VARCHAR
    ,REGISTRO_ICFES VARCHAR
    ,NOMBRE_COLEGIO VARCHAR
    ,DPTO_COLEGIO VARCHAR
    ,MPIO_COLEGIO VARCHAR
    ) SERVER files_csv
    OPTIONS ( filename '/var/lib/postgresql/data/archivos/blanco.csv', format 'csv', delimiter ';' , header 'true');

CREATE OR REPLACE FUNCTION NEW_FILE_FUNCTION() RETURNS TRIGGER
    LANGUAGE PLPGSQL AS
$$
DECLARE
    strquery TEXT := '';
BEGIN
    NEW.fecha_creacion := now();
    --configura la external correspondiente
    strquery :=
            CONCAT('ALTER FOREIGN TABLE public.', NEW.tipo, ' OPTIONS (SET filename ', CHR(39),
                   '/var/lib/postgresql/data/',
                   NEW.new_file, CHR(39),
                   ')');
    raise notice '%',strquery;
    EXECUTE format(strquery);


    --carga informacion de planeacion
    --guarda las competencias si que no esten en la tabla
    insert into public.Competencia (nombre) values ('GLOBAL');
    insert into public.Competencia (nombre)
    select distinct unaccent(upper(pl.modulo))
    from public.Planeacion pl
    where unaccent(upper(pl.modulo)) not in (select distinct nombre from public.Competencia);

    --guarda los codigos y numero de registro que no esten en la tabla estudiante
    INSERT INTO PUBLIC.ESTUDIANTE (CODIGO, NUM_REGISTRO)
    SELECT PL.CODIGO, MAX(PL.NUMERO_DE_REGISTRO)
    FROM PUBLIC.PLANEACION AS PL
    WHERE PL.CODIGO NOT IN
          (SELECT DISTINCT CODIGO
           FROM PUBLIC.ESTUDIANTE)
      AND TIPO_DE_EVALUADO = 'Estudiante'
    GROUP BY PL.CODIGO;

    -- guarda los resultados para las competencias de cada estudiante
    INSERT INTO public.resultados(competencia_id, estudiante_codigo, puntaje, percentil_nal, persentil_grupo,
                                  nivel_desemp)
    SELECT ID::INTEGER,
           CODIGO,
           CASE
               WHEN PUNTAJE_MODULO = '-' THEN NULL
               ELSE PUNTAJE_MODULO::INTEGER
               END,
           CASE
               WHEN PERCENTIL_NACIONAL_MODULO = '-' THEN NULL
               ELSE PERCENTIL_NACIONAL_MODULO::INTEGER
               END,
           CASE
               WHEN PERCENTIL_GRUPO_DE_REFERENCIA_MODULO = '-' THEN NULL
               ELSE PERCENTIL_GRUPO_DE_REFERENCIA_MODULO::INTEGER
               END,
           NIVEL_DE_DESEMPENO
    FROM PUBLIC.COMPETENCIA AS CO
             INNER JOIN PUBLIC.PLANEACION AS PL ON CO.NOMBRE = unaccent(PL.MODULO)
    WHERE PL.NOVEDADES = '-'
      AND PL.TIPO_DE_EVALUADO = 'Estudiante'
    ON CONFLICT (competencia_id, estudiante_codigo) DO NOTHING;
    INSERT INTO public.resultados(competencia_id, estudiante_codigo, puntaje, percentil_nal, persentil_grupo,
                                  nivel_desemp)
    SELECT 1,
           CODIGO,
           CASE
               WHEN puntaje_global = '-' THEN NULL
               ELSE puntaje_global::INTEGER
               END,
           CASE
               WHEN percentil_nacional_global = '-' THEN NULL
               ELSE percentil_nacional_global::INTEGER
               END,
           CASE
               WHEN percentil_grupo_de_referencia = '-' THEN NULL
               ELSE percentil_grupo_de_referencia::INTEGER
               END,
           ''
    FROM PUBLIC.COMPETENCIA AS CO
             INNER JOIN PUBLIC.PLANEACION AS PL ON CO.NOMBRE = unaccent(PL.MODULO)
    WHERE PL.NOVEDADES = '-'
      AND PL.TIPO_DE_EVALUADO = 'Estudiante'
    ON CONFLICT (competencia_id, estudiante_codigo) DO NOTHING;

    -- cargar departamentos y ciudades
    --select departamento_origen,departamento_residencia,ciudad_origen,ciudad_residencia from public.admisiones;
    INSERT INTO public.Departamento(nombre)
    select distinct unaccent(upper(departamento_origen_ad))
    from public.admisiones
    where unaccent(upper(departamento_origen_ad)) not in (select distinct nombre from public.departamento);
    INSERT INTO public.Departamento(nombre)
    select distinct trim(unaccent(upper(split_part(origen_colegio_ad, ';', 1))))
    from public.admisiones
    where trim(unaccent(upper(split_part(origen_colegio_ad, ';', 1)))) not in
          (select distinct nombre from public.departamento);
    INSERT INTO public.Departamento(nombre)
    select distinct unaccent(upper(departamento_residencia_ad))
    from public.admisiones
    where unaccent(upper(departamento_residencia_ad)) not in (select distinct nombre from public.departamento);


    INSERT INTO public.Ciudad(nombre, departamento_id)
    SELECT UNACCENT(UPPER(AD.ciudad_origen_ad)),
           MAX(DE.id)
    FROM PUBLIC.ADMISIONES AS AD
             INNER JOIN PUBLIC.DEPARTAMENTO AS DE ON UNACCENT(UPPER(AD.departamento_origen_ad)) = DE.NOMBRE
    WHERE UNACCENT(UPPER(AD.ciudad_origen_ad)) not in
          (SELECT DISTINCT NOMBRE
           FROM PUBLIC.CIUDAD)
    GROUP BY AD.ciudad_origen_ad;


    INSERT INTO public.Ciudad(nombre, departamento_id)
    select trim(unaccent(upper(split_part(ad.ORIGEN_COLEGIO_ad, ';', 2)))), max(d.id)
    from Admisiones as ad
             left join departamento as d on
            trim(unaccent(upper(split_part(ad.ORIGEN_COLEGIO_ad, ';', 1)))) = d.nombre
    where trim(unaccent(upper(split_part(ad.ORIGEN_COLEGIO_ad, ';', 2)))) not in (select distinct nombre from ciudad)
    group by trim(unaccent(upper(split_part(ad.ORIGEN_COLEGIO_ad, ';', 2))));

    INSERT INTO public.Ciudad(nombre, departamento_id)
    SELECT UNACCENT(UPPER(AD.ciudad_residencia_ad)),
           MAX(DE.id)
    FROM PUBLIC.ADMISIONES AS AD
             INNER JOIN PUBLIC.DEPARTAMENTO AS DE ON UNACCENT(UPPER(AD.departamento_residencia_ad)) = DE.NOMBRE
    WHERE UNACCENT(UPPER(AD.ciudad_residencia_ad)) not in
          (SELECT DISTINCT NOMBRE
           FROM PUBLIC.CIUDAD)
    GROUP BY AD.ciudad_residencia_ad;
    -- cargar programas y facultades
    INSERT INTO public.Facultad(nombre)
    select distinct unaccent(upper(facultad_ad))
    from public.admisiones
    where unaccent(upper(facultad_ad)) not in (select distinct nombre from public.Facultad);

    insert into public.Programa(nombre, cod_prog, facultad_id)
    select unaccent(upper(ad.programa_ad)), max(ad.cod_pro_ad)::integer, max(fa.id)
    FROM public.Admisiones as ad
             INNER JOIN public.Facultad as fa
                        ON unaccent(upper(ad.facultad_ad)) = fa.nombre
    where unaccent(upper(ad.programa_ad)) not in (select distinct nombre from public.programa)
    group by ad.programa_ad;
    /*
     ===========================================================================================================
     FALTA ASEGURARSE DE METER LAS CIUDADES DE LOS COLEGIOS
     ===========================================================================================================
    */

    --llena la tabla colegio
    insert into colegio (nombre, id_ciudad, tipo)
    select trim(unaccent(upper(COLEGIO_ad))) as nombre,
           max(c.id)                         as id_ciudad,
           CASE
               WHEN trim(unaccent(upper(max(TIPO_COLEGIO_ad)))) = 'PUBLICO' THEN 'PUBLICO'
               ELSE 'PRIVADO'
               END                           as tipo
    from Admisiones
             left join ciudad as c on trim(unaccent(upper(split_part(ORIGEN_COLEGIO_ad, ';', 2)))) = c.nombre
    where trim(unaccent(upper(COLEGIO_ad))) not in (select distinct nombre from colegio)
    group by trim(unaccent(upper(COLEGIO_ad))), trim(unaccent(upper(split_part(ORIGEN_COLEGIO_ad, ';', 2))));
    -- cargar exoneraciones


    --cargar periodos


    --cargar info restante de admisiones
    UPDATE public.estudiante as est
    set cohorte=subquery.cohorte_ad::integer,
        sem_actual=subquery.sem_actual_ad::integer,
        estrato=subquery.estrato_ad::integer,
        estado=
            CASE
                WHEN trim(unaccent(upper(subquery.nom_estado_ad))) = 'ANTIGUO'
                    OR
                     trim(unaccent(upper(subquery.nom_estado_ad))) = 'GRADUADO'
                    THEN
                    trim(unaccent(upper(subquery.nom_estado_ad)))

                ELSE 'OTROS'
                END,
        promedio_acumulado=subquery.prom_acu_ad_ad::integer,
        reliq_casos_especiales=subquery.reliq_casos_esp_ad::integer,
        opcion_ingeso=subquery.opcion_de_ingreso_ad,
        ciudad_origen=subquery.cir_id,
        programa_id=subquery.pr_id,
        ciudad_residencia=subquery.cio_id,
        cupo_especial_ingreso=unaccent(upper(subquery.cupo_especial_ad)),
        ult_promedio_semestral=subquery.prom_sem_ad::integer,
        porc_creditos_aprobados=subquery.porc_cred_oblig_aprobados_ad::integer,
        nombre_situacion=subquery.nombre_situacion,
        numero_readmisiones=subquery.readmisiones_ad::integer,
        numero_plan=subquery.plan_ad::integer,
        gano_examen_ingles=subquery.gano_ingles_ad::integer,
        sexo=subquery.sexo_ad,
        fecha_nacimiento=subquery.nacimiento_ad,--::date,
        anyo_11=subquery.anio_undecimo_ad::integer,
        pago_sem_actual=subquery.pago_ad,
        modalidad=subquery.modalidad_ad,
        nivel_estudio=subquery.nivel_estudio_ad,
        mencion_honorofica=unaccent(upper(subquery.mencion_de_grado_ad)),
        fecha_grado=subquery.fecha_de_grado_ad,
        saber11=subquery.saber_11_ad,
        saberpro=subquery.saber_pro_ad,
        ult_periodo_academico=subquery.ultimo_periodo_academico_ad,
        ult_periodo_pagado=subquery.ultimo_periodo_pagado_ad,
        ult_tipo_pago=subquery.ultimo_tipo_de_pagado_ad,
        ult_valor_pagado=subquery.ultimo_valor_pagado_ad::integer,
        ult_valor_liquidado= subquery.ultimo_valor_liquidado_ad::integer,
        ult_periodo_liquidado =subquery.ultimo_periodo_liquidado_ad,
        total_periodos_academicos=subquery.total_periodos_academicos_ad::integer,
        total_periodos_pagados=subquery.total_periodos_pagados_ad::numeric,
        puntaje_admision=replace(subquery.puntaje_admision_ad, ',', '.')::numeric::integer,
        num_documento=subquery.num_doc_ad,
        colegio_id=subquery.col_id

    from (
             select *, cio.id as cio_id, cir.id as cir_id, pr.id as pr_id, col.id as col_id
             from public.estudiante
                      inner join public.admisiones as ad on codigo = ad.codigo_e
                      inner join public.ciudad as cio on unaccent(upper(ad.ciudad_origen_ad)) = cio.nombre
                      inner join public.ciudad as cir on unaccent(upper(ad.ciudad_residencia_ad)) = cir.nombre
                      inner join public.programa as pr on pr.nombre = unaccent(upper(ad.programa_ad))
                      inner join ciudad coc
                                 on coc.nombre = trim(unaccent(upper(split_part(ad.ORIGEN_COLEGIO_ad, ';', 2))))
                      inner join public.colegio as col
                                 on trim(unaccent(upper(ad.colegio_ad))) = col.nombre and col.id_ciudad = coc.id
         ) AS subquery
    where est.codigo = subquery.codigo_e;
    NEW.estado = 'Subido OK';
    RETURN NEW;

exception
    when others then
        NEW.estado = 'Error: %';
        RETURN NEW;


END;
$$;
DROP TRIGGER IF EXISTS new_file_trigger ON public.Archivo CASCADE;

CREATE TRIGGER new_file_trigger
    BEFORE INSERT
    ON public.Archivo
    FOR EACH ROW
EXECUTE PROCEDURE new_file_function();

INSERT INTO public.Archivo (descripcion, tipo, new_file, year)
VALUES ('DESCIPCION del archivo de planeacion de prueba', 'Planeacion',
        'archivos/planeacion.csv', 2020);

INSERT INTO public.Archivo (descripcion, tipo, new_file, year)
VALUES ('DESCIPCION del archivo de admisiones de prueba', 'Admisiones',
        'archivos/admisiones.csv', 2020);

INSERT INTO public.Archivo (descripcion, tipo, new_file, year)
VALUES ('DESCIPCION del archivo de talento de sistemas de prueba', 'Talento',
        'archivos/Sistemas.csv', 2020);



select *
from estudiante;

SELECT count(*)
FROM public.resultados t
