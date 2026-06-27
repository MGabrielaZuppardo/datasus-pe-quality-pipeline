with source as (
    select * from read_parquet('{{ env_var("PARQUET_PATH", "../../data/parquet") }}/SINASC_PE*.parquet')
),

renamed as (
    select
        NUMERODV         as numero_dn,
        CODMUNRES        as codigo_municipio_residencia,
        DTNASC           as data_nascimento,
        SEXO             as sexo,
        PESO             as peso_gramas,
        APGAR1           as apgar_1_minuto,
        APGAR5           as apgar_5_minutos,
        IDADEMAE         as idade_mae,
        ESCMAE           as escolaridade_mae,
        RACACORMAE       as raca_cor_mae,
        CODESTAB         as codigo_estabelecimento,
        _arquivo_origem  as arquivo_origem,
        _data_extracao   as data_extracao,
        _versao_pipeline as versao_pipeline
    from source
    where left(CODMUNRES, 2) = '26'
)

select * from renamed
