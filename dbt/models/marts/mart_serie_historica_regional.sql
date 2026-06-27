with obitos as (
    select
        nome_regional,
        regional_saude_id,
        date_trunc('month', data_obito::date) as mes_obito,
        causa_basica_obito,
        count(*) as total_obitos
    from {{ ref('int_obitos_enriquecido') }}
    where data_obito is not null
    group by 1, 2, 3, 4
)

select * from obitos
order by regional_saude_id, mes_obito
