CREATE TABLE message
(
  sid character varying(40) NOT NULL,
  date_created character varying(40) NOT NULL,
  account_sid character varying(40) NOT NULL,
  to_ character varying(40) NOT NULL,
  from_ character varying(40) NOT NULL,
  body character varying(200) NOT NULL,
  status character varying(40) NOT NULL,
  CONSTRAINT message_pkey PRIMARY KEY (sid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE message
  OWNER TO postgres;