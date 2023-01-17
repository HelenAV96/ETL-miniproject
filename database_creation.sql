create database archprep;
grant all privileges on database archprep to yourownusername;
alter database archprep owner to yourownusername;
\c archprep
create schema cleansed;
create schema staged;
create schema modelled;