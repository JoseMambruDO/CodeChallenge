create type public.continent_enum as enum(
'North America','South America','Antarctica','Europe','Asia','Africa','Australia'
);

create table public.country(
	id serial primary key,
	code varchar(3) not null,
	name varchar(52) not null,
	continent continent_enum not null,
	region varchar(26) not null,
	surfaceArea real,
	indepYear smallint, 
	population int, 
	lifeExpectancy float,
	gnp float,
	localName varchar,
	governmentForm varchar,
	headOfState varchar,
	code2 varchar(3) 
);

create table public.city(
	id serial primary key,
	name varchar(35),
	countrycode varchar(3),
	country_id int references public.country(id),
	district varchar(20),
	population int
);

create table public.countrylanguage(
	id serial primary key,
    country_id int references public.country(id) not null ,
    language varchar(20),
    isOfficial boolean,
    percentage float
 );
 

create table public.countrygbp(
	id serial primary key,
    country_id int references public.country(id) not null ,
	year smallint,
    val float
 );
 
