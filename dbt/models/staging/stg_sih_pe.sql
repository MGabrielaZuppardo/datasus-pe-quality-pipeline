with source as (
    select * from read_parquet('{{ env_var("PARQUET_PATH", "../../data/parquet") }}/SIH_PE*.parquet')
),

renamed as (
    select
        N_AIH            as numero_aih,
        CNES             as codigo_cnes,
        MUNIC_RES        as codigo_municipio_residencia,
        DIAG_PRINC       as diagnostico_principal,
        DT_INTER         as data_internacao,
        DT_SAIDA         as data_saida,
        DIAS_PERM        as dias_permanencia,
        MORTE            as indicador_obito,
        VAL_TOT          as valor_total_aih,
        _arquivo_origem  as arquivo_origem,
        _data_extracao   as data_extracao,
        _versao_pipeline as versao_pipeline
    from source
    where left(MUNIC_RES, 2) = '26'
)

select * from renamed
