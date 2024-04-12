select * from inscritos

-- 1. ¿Cuántos registros hay?
select count(*) from inscritos

-- 2. ¿Cuántos inscritos hay en total?
select sum(cantidad) from inscritos

-- 3. ¿Cuál o cuáles son los registros de mayor antigüedad?
select * from inscritos where fecha = (select min(fecha) from inscritos)

-- 4. ¿Cuántos inscritos hay por día? (entendiendo un día como una fecha distinta de ahora en adelante)
select sum(cantidad), fecha from inscritos group by fecha

-- 5. ¿Qué día se inscribieron la mayor cantidad de personas y cuántas personas se inscribieron en ese día?
select sum(cantidad) as total_inscritos, fecha from inscritos group by fecha order by total_inscritos desc limit 1

