-- Falha se CODMUNRES do SIM não existir na tabela de municípios PE (IBGE)
select s.codigo_municipio_residencia
from {{ ref('stg_sim_pe') }} s
left join {{ ref('municipios_pe') }} m
    on s.codigo_municipio_residencia = cast(m.codigo_ibge as varchar)
where s.codigo_municipio_residencia is not null
  and m.codigo_ibge is null
