create table country(
	id serial primary key,
	code varchar(3) not null,
	name varchar(52) not null,
	continent varchar(26) not null,
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

create table city(
	id serial primary key,
	name varchar(35),
	countrycode varchar(3),
	country_id int references country(id),
	district varchar(20),
	population int
);