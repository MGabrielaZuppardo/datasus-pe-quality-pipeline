with source as (
    select * from read_parquet('{{ env_var("PARQUET_PATH", "../../data/parquet") }}/SINAN_DENG_PE*.parquet')
),

renamed as (
    select
        NU_NOTIFIC       as numero_notificacao,
        DT_NOTIFIC       as data_notificacao,
        SE_NOTIFIC       as semana_epidemiologica_notificacao,
        CO_MUN_NOT       as codigo_municipio_notificacao,
        CO_MUN_RES       as codigo_municipio_residencia,
        DT_SIN_PRI       as data_inicio_sintomas,
        CLASSI_FIN       as classificacao_final,
        EVOLUCAO         as evolucao_caso,
        _arquivo_origem  as arquivo_origem,
        _data_extracao   as data_extracao,
        _versao_pipeline as versao_pipeline
    from source
    where left(CO_MUN_NOT, 2) = '26'
)

select * from renamed
