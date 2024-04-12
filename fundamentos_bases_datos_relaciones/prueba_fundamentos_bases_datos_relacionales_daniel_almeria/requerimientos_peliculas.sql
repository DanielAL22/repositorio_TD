-- 1. Crea el modelo (revisa bien cuál es el tipo de relación antes de crearlo), respeta las claves primarias, foráneas y tipos de datos.


/************ Update: Tables ***************/

/******************** Add Table: public.pelicula ************************/

/* Build Table Structure */
CREATE TABLE public.pelicula
(
	id INTEGER NOT NULL,
	nombre VARCHAR(255) NOT NULL,
	anno INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE public.pelicula ADD CONSTRAINT pkpelicula
	PRIMARY KEY (id);


/******************** Add Table: public.pelicula_tag ************************/

/* Build Table Structure */
CREATE TABLE public.pelicula_tag
(
	id INTEGER NOT NULL,
	id_pelicula INTEGER NOT NULL,
	id_tag INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE public.pelicula_tag ADD CONSTRAINT pkpelicula_tag
	PRIMARY KEY (id);


/******************** Add Table: public.tag ************************/

/* Build Table Structure */
CREATE TABLE public.tag
(
	id INTEGER NOT NULL,
	tag VARCHAR(32) NOT NULL
);

/* Add Primary Key */
ALTER TABLE public.tag ADD CONSTRAINT pktag
	PRIMARY KEY (id);





/************ Add Foreign Keys ***************/

/* Add Foreign Key: fk_pelicula_tag_pelicula */
ALTER TABLE public.pelicula_tag ADD CONSTRAINT fk_pelicula_tag_pelicula
	FOREIGN KEY (id_pelicula) REFERENCES public.pelicula (id)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_pelicula_tag_tag */
ALTER TABLE public.pelicula_tag ADD CONSTRAINT fk_pelicula_tag_tag
	FOREIGN KEY (id_tag) REFERENCES public.tag (id)
	ON UPDATE NO ACTION ON DELETE NO ACTION;
	


-- Extra: cargamos la función para generar IDs
CREATE OR REPLACE FUNCTION get_id(tabla varchar(25)) RETURNS integer AS $$
DECLARE
    id_actual integer;
    consulta text;
    ids RECORD;
BEGIN
    consulta := concat('SELECT id FROM ', tabla, ' ORDER BY id');
    id_actual := 1;

    FOR ids IN EXECUTE consulta LOOP
        RAISE NOTICE '-- CLIENTE: %', ids.id;

        IF ids.id <> id_actual THEN
            RAISE NOTICE 'EXIT';
            EXIT;
        ELSE
            id_actual := id_actual + 1;
            RAISE NOTICE 'se suma%', id_actual;
        END IF;
    END LOOP;

    RETURN id_actual;
END;
$$ LANGUAGE plpgsql;





	
-- 2. Inserta 5 películas y 5 tags, la primera película tiene que tener 3 tags asociados, la segunda película debe tener dos tags asociados.
select * from pelicula
select * from tag
select * from pelicula_tag


insert into pelicula (id, nombre, anno) values (get_id('pelicula'), 'Reservoir Dogs', 1992);
insert into pelicula (id, nombre, anno) values (get_id('pelicula'), 'A Clockwork Orange', 1972);
insert into pelicula (id, nombre, anno) values (get_id('pelicula'), 'Apocalypse Now', 1979);
insert into pelicula (id, nombre, anno) values (get_id('pelicula'), 'Full Metal Jacket', 1992);
insert into pelicula (id, nombre, anno) values (get_id('pelicula'), 'Scarface', 1983);

insert into tag (id, tag) values (get_id('tag'), 'tarantino');
insert into tag (id, tag) values (get_id('tag'), 'crimen');
insert into tag (id, tag) values (get_id('tag'), 'estados unidos');
insert into tag (id, tag) values (get_id('tag'), 'kubrick');
insert into tag (id, tag) values (get_id('tag'), 'ciencia ficcion');

insert into pelicula_tag (id, id_pelicula, id_tag) values (get_id('pelicula_tag'), 1, 1);
insert into pelicula_tag (id, id_pelicula, id_tag) values (get_id('pelicula_tag'), 1, 2);
insert into pelicula_tag (id, id_pelicula, id_tag) values (get_id('pelicula_tag'), 1, 3);
insert into pelicula_tag (id, id_pelicula, id_tag) values (get_id('pelicula_tag'), 2, 4);
insert into pelicula_tag (id, id_pelicula, id_tag) values (get_id('pelicula_tag'), 2, 5);


-- 3. Cuenta la cantidad de tags que tiene cada película. Si una película no tiene tags debe mostrar 0.
select count(id_tag), p.nombre from pelicula as p
left join pelicula_tag as pt on p.id = pt.id_pelicula
group by p.nombre






