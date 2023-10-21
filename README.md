-- public."user" definition

-- Drop table

-- DROP TABLE public."user";

CREATE TABLE public."user" (
	username varchar(100) NOT NULL,
	"password" varchar(100) NOT NULL
);

grant all privileges on table "user" to username;