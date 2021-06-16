CREATE TABLE IF NOT EXISTS SaberPro(
   FIELD1                                            INTEGER 
  ,codigo                                            INTEGER  PRIMARY KEY 
  ,cohorte                                           INTEGER 
  ,sem_actual                                        INTEGER 
  ,estrato                                           INTEGER 
  ,codigo_estado                                     VARCHAR(1)
  ,estado                                            VARCHAR(8)
  ,promedio_acumulado                                INTEGER 
  ,reliq_casos_especiales                            INTEGER 
  ,ult_exos_aplicadas                                VARCHAR(79)
  ,opcion_ingeso                                     VARCHAR(1)
  ,tipo_ingreso                                      VARCHAR(11)
  ,cupo_especial_ingreso                             VARCHAR(7)
  ,ult_promedio_semestral                            INTEGER 
  ,porc_creditos_aprobados                           INTEGER 
  ,nombre_situacion                                  VARCHAR(22)
  ,codigo_situacion_estudiante                       VARCHAR(1)
  ,numero_readmisiones                               INTEGER 
  ,peridos_readmisiones                              VARCHAR(21)
  ,numero_plan                                       INTEGER 
  ,codigo_programa                                   INTEGER 
  ,programa                                          VARCHAR(26)
  ,facultad                                          VARCHAR(47)
  ,gano_examen_ingles                                BIT 
  ,tipo_colegio                                      VARCHAR(7)
  ,colegioumento                                     VARCHAR(22)
  ,sexo                                              VARCHAR(1)
  ,ciudad_origen                                     VARCHAR(11)
  ,ciudad_residencia                                 VARCHAR(11)
  ,dpto_origen                                       VARCHAR(9)
  ,dpto_residencia                                   VARCHAR(9)
  ,colegio                                           VARCHAR(43)
  ,edad                                              INTEGER 
  ,fecha_nacimiento                                  DATE 
  ,anyo_11                                           BIT 
  ,pago_sem_actual                                   VARCHAR(12)
  ,modalidad                                         VARCHAR(1)
  ,nivel_estudio                                     VARCHAR(2)
  ,mencion_honorofica                                VARCHAR(7)
  ,fecha_grado                                       VARCHAR(10)
  ,saber11                                           VARCHAR(14)
  ,saberPro                                          VARCHAR(14)
  ,ult_periodo_academico                             VARCHAR(6)
  ,ult_periodo_pagado                                VARCHAR(6)
  ,ult_tipo_pago                                     VARCHAR(23)
  ,ult_valor_pagado                                  INTEGER 
  ,ult_periodo_liquidado                             VARCHAR(6)
  ,ult_valor_liquidado                               INTEGER 
  ,total_periodos_academicos                         INTEGER 
  ,total_periodos_pagados                            INTEGER 
  ,puntaje_admision                                  INTEGER 
  ,condigo_joven_en_accion                           VARCHAR(1)
  ,tipo_doc                                          VARCHAR(2)
  ,num_documento_y                                   INTEGER 
  ,nombre                                            VARCHAR(31)
  ,num_registro                                      VARCHAR(14)
  ,tipo_evaluado                                     VARCHAR(10)
  ,snies_prg                                         INTEGER 
  ,cprog                                             INTEGER 
  ,ciudad                                            VARCHAR(11)
  ,grupo_ref                                         VARCHAR(23)
  ,puntaje_global                                    INTEGER 
  ,percentil_nal_global                              INTEGER 
  ,percentil_grupo_ref                               INTEGER 
  ,novedades                                         INTEGER 
  ,nivel_desemp_competencias_ciudadanas              INTEGER 
  ,nivel_desemp_comunicacion_escrita                 INTEGER 
  ,nivel_desemp_ingles                               VARCHAR(3)
  ,nivel_desemp_lectura_critica                      INTEGER 
  ,nivel_desemp_razonamiento_cuantitativo            INTEGER 
  ,percentil_grupo_ref_mod_competencias_ciudadanas   INTEGER 
  ,percentil_grupo_ref_mod_comunicacion_escrita      INTEGER 
  ,percentil_grupo_ref_mod_ingles                    INTEGER 
  ,percentil_grupo_ref_mod_lectura_critica           INTEGER 
  ,percentil_grupo_ref_mod_razonamiento_cuantitativo INTEGER 
  ,percentil_nal_mod_competencias_ciudadanas         INTEGER 
  ,percentil_nal_mod_comunicacion_escrita            INTEGER 
  ,percentil_nal_mod_ingles                          INTEGER 
  ,percentil_nal_mod_lectura_critica                 INTEGER 
  ,percentil_nal_mod_razonamiento_cuantitativo       INTEGER 
  ,puntaje_mod_competencias_ciudadanas               INTEGER 
  ,puntaje_mod_comunicacion_escrita                  INTEGER 
  ,puntaje_mod_ingles                                INTEGER 
  ,puntaje_mod_lectura_critica                       INTEGER 
  ,puntaje_mod_razonamiento_cuantitativo             INTEGER 
  ,periodo_exam                                      VARCHAR(6)
  ,prom_acum_exam                                    INTEGER 
);
