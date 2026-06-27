with obitos as (
    select * from {{ ref('stg_sim_pe') }}
),

municipios as (
    select * from {{ ref('municipios_pe') }}
),

regionais as (
    select * from {{ ref('regionais_saude_pe') }}
),

enriquecido as (
    select
        o.*,
        m.nome_municipio,
        m.regional_saude_id,
        r.nome_regional,
        (
            o.codigo_municipio_residencia is not null
            and o.causa_basica_obito is not null
            and o.data_obito is not null
            and o.data_nascimento is not null
        ) as registro_completo
    from obitos o
    left join municipios m
        on o.codigo_municipio_residencia = cast(m.codigo_ibge as varchar)
    left join regionais r
        on m.regional_saude_id = r.regional_saude_id
)

select * from enriquecido
