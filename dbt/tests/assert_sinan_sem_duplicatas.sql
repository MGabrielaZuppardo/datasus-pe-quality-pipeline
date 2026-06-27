-- Falha se int_dengue_deduplicado ainda contiver duplicatas pela chave de negócio
select
    numero_notificacao,
    semana_epidemiologica_notificacao,
    codigo_municipio_notificacao,
    count(*) as ocorrencias
from {{ ref('int_dengue_deduplicado') }}
group by 1, 2, 3
having count(*) > 1
