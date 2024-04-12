-- 1. Crear una base de datos llamada películas.

CREATE TABLE IF NOT EXISTS public.peliculas
(
    id integer NOT NULL,
    pelicula character varying(100) COLLATE pg_catalog."default" NOT NULL,
    anio_estreno character varying(4) COLLATE pg_catalog."default" NOT NULL,
    director character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT peliculas_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.peliculas
    OWNER to postgres;



-- 2. Cargar ambos archivos a su tabla correspondiente.
-- Realizado con pgAdmin4: botón derecho sobre la tabla --> Import/Export Data (no se generó el código SQL asociado)
select * from peliculas;
select * from reparto;

-- 3. Obtener el ID de la película “Titanic”.
select id from peliculas where pelicula = 'Titanic';

-- 4. Listar a todos los actores que aparecen en la película "Titanic".
select r.actor from peliculas as p
inner join reparto as r
on p.id = r.id_pelicula
where p.pelicula = 'Titanic';

-- 5. Consultar en cuántas películas del top 100 participa Harrison Ford.
select count(*) from peliculas as p
inner join reparto as r
on p.id = r.id_pelicula
where r.actor = 'Harrison Ford';

-- 6. Indicar las películas estrenadas entre los años 1990 y 1999 ordenadas por título de manera ascendente.
select pelicula, anio_estreno from peliculas
where anio_estreno >= '1990' and anio_estreno <= '1999'
order by pelicula;

-- 7. Hacer una consulta SQL que muestre los títulos con su longitud, la longitud debe ser nombrado para la consulta como “longitud_titulo”.
select pelicula, length(pelicula) as longitud_titulo from peliculas;

-- 8. Consultar cual es la longitud más grande entre todos los títulos de las películas.
select pelicula, length(pelicula) as longitud_titulo 
from peliculas
order by longitud_titulo DESC
limit 1;
	 






