-- Database: worldgbp

-- DROP DATABASE worldgdp;

--CREATE DATABASE worldgdp
--    WITH 
--    OWNER = postgres
--    ENCODING = 'UTF8'
--    LC_COLLATE = 'en_US.UTF-8'
--    LC_CTYPE = 'en_US.UTF-8'
--    TABLESPACE = pg_default
--    CONNECTION LIMIT = -1;


--create type public.continent_enum as enum(
--'North America','South America','Antarctica','Europe','Asia','Africa','Australia'
--);

create table public.country(
	id serial primary key,
	code varchar(3) not null,
	countryname varchar(52) not null,
	continent varchar not null,
--	continent continent_enum not null,
	region varchar(26) not null,
	surfaceArea real,
	indepYear smallint, 
	population int, 
	lifeExpectancy float,
	gnp float,
	localName varchar,
	governmentForm varchar,
	headOfState varchar,
	capital int,
	code2 varchar(3) 
);

create table public.city(
	id serial primary key,
	name varchar(35),
	countrycode varchar(3),
	country_id int  not null references public.country(id),
	district varchar(20),
	population int
);

alter table public.country 
	add constraint fk_country_city FOREIGN KEY (capital) REFERENCES city (id);

create table public.countrylanguage(
	id serial primary key,
    country_id int  not null references public.country(id),
    language varchar(20),
    isOfficial boolean,
    percentage float
 );
 
create table public.countrygbp(
	id serial primary key,
    country_id int  not null references public.country(id),
	year smallint,
    val float
 );
 
