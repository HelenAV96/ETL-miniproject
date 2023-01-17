create database archprep;
grant all privileges on database archprep to postgres;
alter database archprep owner to postgres;
\c archprep
create schema cleansed;
create schema staged;
create schema modelled;