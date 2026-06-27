-- Chave de deduplicação: nu_notificacao + se_notificacao + co_mun_not
-- SINAN-dengue tem duplicatas em anos de epidemia (2019, 2022, 2024)
with source as (
    select * from {{ ref('stg_sinan_dengue_pe') }}
),

ranked as (
    select *,
        row_number() over (
            partition by numero_notificacao, semana_epidemiologica_notificacao, codigo_municipio_notificacao
            order by data_notificacao desc
        ) as rn
    from source
)

select * exclude (rn)
from ranked
where rn = 1
