create table public.product(
	id serial primary key,
	name varchar(20) not null,
	description varchar(100),
	quantity int,
	price float,
	cost float,
	category_id int not null
);

create table public.category(
	id serial primary key,
	name varchar(40) not null unique
);

alter table public.product 
	add constraint fk_product_category FOREIGN KEY (category_id) REFERENCES  category(id);
