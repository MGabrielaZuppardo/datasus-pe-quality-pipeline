with sih as (
    select * from {{ ref('stg_sih_pe') }}
),

municipios as (
    select * from {{ ref('municipios_pe') }}
),

agregado as (
    select
        s.codigo_cnes,
        m.nome_municipio,
        m.regional_saude_id,
        date_trunc('month', s.data_internacao::date) as mes_internacao,
        count(*)                                       as total_aih,
        sum(s.dias_permanencia)                        as total_dias_permanencia,
        sum(s.valor_total_aih)                         as valor_total,
        sum(s.indicador_obito::int)                    as total_obitos
    from sih s
    left join municipios m
        on s.codigo_municipio_residencia = cast(m.codigo_ibge as varchar)
    group by 1, 2, 3, 4
)

select * from agregado
