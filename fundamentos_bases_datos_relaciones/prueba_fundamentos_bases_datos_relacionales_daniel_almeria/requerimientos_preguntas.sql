-- 4. Crea las tablas respetando los nombres, tipos, claves primarias y foráneas y tipos de datos.
/************ Update: Tables ***************/

/******************** Add Table: public.pregunta ************************/

/* Build Table Structure */
CREATE TABLE public.pregunta
(
	id INTEGER NOT NULL,
	pregunta VARCHAR(255) NOT NULL,
	respuesta_correcta VARCHAR NOT NULL
);

/* Add Primary Key */
ALTER TABLE public.pregunta ADD CONSTRAINT pkpregunta
	PRIMARY KEY (id);


/******************** Add Table: public.respuestas ************************/

/* Build Table Structure */
CREATE TABLE public.respuestas
(
	id INTEGER NOT NULL,
	respuesta VARCHAR(255) NOT NULL,
	usuario_id INTEGER NOT NULL,
	pregunta_id INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE public.respuestas ADD CONSTRAINT pkrespuestas
	PRIMARY KEY (id);


/******************** Add Table: public.usuario ************************/

/* Build Table Structure */
CREATE TABLE public.usuario
(
	id INTEGER NOT NULL,
	nombre VARCHAR(255) NOT NULL,
	edad INTEGER NOT NULL
);

/* Add Primary Key */
ALTER TABLE public.usuario ADD CONSTRAINT pkusuario
	PRIMARY KEY (id);





/************ Add Foreign Keys ***************/

/* Add Foreign Key: fk_respuestas_pregunta */
ALTER TABLE public.respuestas ADD CONSTRAINT fk_respuestas_pregunta
	FOREIGN KEY (pregunta_id) REFERENCES public.pregunta (id)
	ON UPDATE NO ACTION ON DELETE NO ACTION;

/* Add Foreign Key: fk_respuestas_usuario */
ALTER TABLE public.respuestas ADD CONSTRAINT fk_respuestas_usuario
	FOREIGN KEY (usuario_id) REFERENCES public.usuario (id)
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



-- 5. Agrega 5 registros a la tabla preguntas, de los cuales:
-- a. 1. La primera pregunta debe ser contestada correctamente por dos usuarios distintos
-- b. 2. La pregunta 2 debe ser contestada correctamente por un usuario.
-- c. 3. Los otros dos registros deben ser respuestas incorrectas.

select * from pregunta;
select * from usuario;
select * from respuestas;

insert into pregunta (id, pregunta, respuesta_correcta) values (get_id('pregunta'), 'Pregunta 1', 'a');
insert into pregunta (id, pregunta, respuesta_correcta) values (get_id('pregunta'), 'Pregunta 2', 'b');
insert into pregunta (id, pregunta, respuesta_correcta) values (get_id('pregunta'), 'Pregunta 3', 'c');
insert into pregunta (id, pregunta, respuesta_correcta) values (get_id('pregunta'), 'Pregunta 4', 'a');
insert into pregunta (id, pregunta, respuesta_correcta) values (get_id('pregunta'), 'Pregunta 5', 'c');

insert into usuario (id, nombre, edad) values (get_id('usuario'), 'Daniel', 31);
insert into usuario (id, nombre, edad) values (get_id('usuario'), 'Consuelo', 39);
insert into usuario (id, nombre, edad) values (get_id('usuario'), 'Coti', 32);
insert into usuario (id, nombre, edad) values (get_id('usuario'), 'Raúl', 29);
insert into usuario (id, nombre, edad) values (get_id('usuario'), 'Diego', 35);

insert into respuestas (id, respuesta, usuario_id, pregunta_id) values (get_id('respuestas'), 'a', 1, 1);
insert into respuestas (id, respuesta, usuario_id, pregunta_id) values (get_id('respuestas'), 'a', 2, 1);
insert into respuestas (id, respuesta, usuario_id, pregunta_id) values (get_id('respuestas'), 'b', 3, 2);
insert into respuestas (id, respuesta, usuario_id, pregunta_id) values (get_id('respuestas'), 'c', 4, 2);
insert into respuestas (id, respuesta, usuario_id, pregunta_id) values (get_id('respuestas'), 'a', 3, 3);


-- 6. Cuenta la cantidad de respuestas correctas totales por usuario (independiente de la pregunta).
select count(pregunta_id) as respuestas_correctas, u.nombre from pregunta as p
inner join respuestas as r on p.id = r.pregunta_id
inner join usuario as u on u.id = r.usuario_id
where p.respuesta_correcta = r.respuesta
group by u.nombre
;


-- 7. Por cada pregunta, en la tabla preguntas, cuenta cuántos usuarios tuvieron la respuesta correcta.
select count(usuario_id), p.pregunta from pregunta as p
inner join respuestas as r on p.id = r.pregunta_id
inner join usuario as u on u.id = r.usuario_id
where p.respuesta_correcta = r.respuesta
group by p.pregunta
;


-- 8. Implementa borrado en cascada de las respuestas al borrar un usuario y borrar el primer usuario para probar la implementación.
-- Primero obtenemos el nombre de la foreign key
SELECT constraint_name, constraint_type, 'usuario', 'id', 'respuestas', 'usuario_id'
FROM information_schema.table_constraints
WHERE table_name = 'respuestas' AND constraint_type = 'FOREIGN KEY';

-- Segundo implementamos ON DELETE CASCADE
ALTER TABLE respuestas
DROP CONSTRAINT IF EXISTS fk_respuestas_usuario,
ADD CONSTRAINT fk_respuestas_usuario
FOREIGN KEY (id)
REFERENCES usuario(id)
ON DELETE CASCADE;

-- Probamos la implementación
select * from usuario;
select * from respuestas;

delete from usuario where id = 1;


-- 9. Crea una restricción que impida insertar usuarios menores de 18 años en la base de datos.
alter table usuario
add constraint mayores_edad check (edad >= 18);

-- Comprobamos el resultado
insert into usuario (id, nombre, edad) values (get_id('usuario'), 'Nora', 16);


-- 10. Altera la tabla existente de usuarios agregando el campo email con la restricción de único.
alter table usuario 
add email varchar(100) unique;

