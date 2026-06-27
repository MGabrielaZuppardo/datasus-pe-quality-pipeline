-- Municípios abaixo de 70% de completude recebem flag qualidade_suficiente = false
-- e são excluídos de análises finais pela SES-PE
with obitos as (
    select
        codigo_municipio_residencia as codigo_municipio,
        nome_municipio,
        regional_saude_id,
        nome_regional,
        count(*)                         as total_obitos,
        sum(registro_completo::int)      as obitos_completos
    from {{ ref('int_obitos_enriquecido') }}
    group by 1, 2, 3, 4
)

select
    *,
    round(obitos_completos * 100.0 / nullif(total_obitos, 0), 1) as completude_pct,
    (obitos_completos * 100.0 / nullif(total_obitos, 0)) >= 70    as qualidade_suficiente
from obitos
