with source as (
    select * from read_parquet('{{ env_var("PARQUET_PATH", "../../data/parquet") }}/SIM_PE*.parquet')
),

renamed as (
    select
        NUMERODO         as numero_do,
        CODMUNRES        as codigo_municipio_residencia,
        CAUSABAS         as causa_basica_obito,
        DTOBITO          as data_obito,
        DTNASC           as data_nascimento,
        SEXO             as sexo,
        RACACOR          as raca_cor,
        IDADE            as idade,
        CODESTAB         as codigo_estabelecimento,
        _arquivo_origem  as arquivo_origem,
        _data_extracao   as data_extracao,
        _versao_pipeline as versao_pipeline
    from source
    where left(CODMUNRES, 2) = '26'
)

select * from renamed
