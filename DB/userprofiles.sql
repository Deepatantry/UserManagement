-- Table: public.userprofiles

-- DROP TABLE public.userprofiles;

CREATE TABLE public.userprofiles
(
    username character varying(30) COLLATE pg_catalog."default" NOT NULL,
    password character varying(200) COLLATE pg_catalog."default" NOT NULL,
    email character varying(150) COLLATE pg_catalog."default" NOT NULL,
    createddate timestamp without time zone NOT NULL,
    lastlogin timestamp without time zone,
    CONSTRAINT userprofiles_username_key UNIQUE (username)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.userprofiles
    OWNER to "GitlabPostgres";
