--CREATE SCHEMA my_schema;

CREATE TABLE my_schema.todo(
    id SERIAL,
    prio INT,
    comment VARCHAR(100)
    );

SET search_path TO my_schema;

select * from my_schema.todo;

insert into my_schema.todo (prio, comment)
values  (1,'pie soup'), (2,'tooth paste');

ALTER TABLE my_schema.todo add column status
 VARCHAR(10);

UPDATE my_schema.todo SET status = 'DONE'
WHERE prio = 1;

UPDATE my_schema.todo SET status = 'NOT DONE'
WHERE prio = 2;