--Las tablas fueron subidas a BigQuery y las consultas fueron realizadas en él

--¿Qué aerolínea tiene más vuelos?: 7
Select aerolinea from(
SELECT aerolinea, ROW_NUMBER() OVER( partition by null order by count(*) desc) as rank
 FROM `test_vuelo`
group by aerolinea
) where rank = 1;



--¿Qué Origen se repite más?: SAP
Select origen from(
SELECT origen, ROW_NUMBER() OVER( partition by null order by count(*) desc) as rank
 FROM `test_vuelo`
group by origen
) where rank = 1;

--¿Desde donde vuela más la aerolínea 8?: SAP
Select origen from(
SELECT origen, ROW_NUMBER() OVER( partition by aerolinea order by count(*) desc) as rank
 FROM `test_vuelo`
 where aerolinea = 8
group by origen,aerolinea
) where rank = 1;

--¿Hacia dónde vuela más la aerolínea 4?: SAP
Select destino from(
SELECT destino, ROW_NUMBER() OVER( partition by aerolinea order by count(*) desc) as rank
 FROM `test_vuelo`
 where aerolinea = 4
group by destino,aerolinea
) where rank = 1;


----¿Qué piloto vuela más?: 43579
Select codigo_piloto from(
SELECT codigo_piloto, ROW_NUMBER() OVER( partition by null order by count(*) desc) as rank
 FROM `test_vuelo`
group by codigo_piloto
) where rank = 1;
