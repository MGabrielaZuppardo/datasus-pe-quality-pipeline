with sim as (
    select
        'SIM'                                                          as fonte,
        codigo_municipio_residencia                                    as codigo_municipio,
        count(*)                                                       as total_registros,
        sum(case when codigo_municipio_residencia is null then 1 else 0 end) as nulos_codmunres,
        sum(case when causa_basica_obito        is null then 1 else 0 end) as nulos_causabas,
        sum(case when data_obito               is null then 1 else 0 end) as nulos_dtobito,
        sum(case when data_nascimento           is null then 1 else 0 end) as nulos_dtnasc
    from {{ ref('stg_sim_pe') }}
    group by 1, 2
)

select
    *,
    round(100.0 - nulos_codmunres * 100.0 / nullif(total_registros, 0), 1) as completude_codmunres_pct,
    round(100.0 - nulos_causabas  * 100.0 / nullif(total_registros, 0), 1) as completude_causabas_pct,
    round(100.0 - nulos_dtobito   * 100.0 / nullif(total_registros, 0), 1) as completude_dtobito_pct,
    round(100.0 - nulos_dtnasc    * 100.0 / nullif(total_registros, 0), 1) as completude_dtnasc_pct
from sim
