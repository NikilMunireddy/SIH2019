CREATE TABLE "user_personal_info" (
	"id" VARCHAR(255) NOT NULL,
	"username" VARCHAR(255) NOT NULL,
	"first_name" VARCHAR(255) NOT NULL,
	"last_name" VARCHAR(255) NOT NULL,
	"photo_url" VARCHAR(255) NOT NULL,
	CONSTRAINT user_personal_info_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "registration_detail" (
	"id" VARCHAR(255) NOT NULL,
	"name" VARCHAR(255) NOT NULL,
	"age" integer NOT NULL,
	"height" FLOAT NOT NULL,
	"weight" FLOAT NOT NULL,
	"bmi" FLOAT NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "calories" (
	"id" VARCHAR(255) NOT NULL,
	"date" DATE NOT NULL,
	"calories_burnt" integer NOT NULL,
	"calories_consumed" integer NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "steps" (
	"id" VARCHAR(255) NOT NULL,
	"steps" integer NOT NULL,
	"date" DATE NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "exercise" (
	"id" VARCHAR(255) NOT NULL,
	"type" VARCHAR(255) NOT NULL,
	"count" integer NOT NULL,
	"time_duration" integer NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "gps_location" (
	"id" VARCHAR(255) NOT NULL,
	"gps_long" FLOAT NOT NULL,
	"gps_lat" FLOAT NOT NULL
) WITH (
  OIDS=FALSE
);




ALTER TABLE "registration_detail" ADD CONSTRAINT "registration_detail_fk0" FOREIGN KEY ("id") REFERENCES "user_personal_info"("id");

ALTER TABLE "calories" ADD CONSTRAINT "calories_fk0" FOREIGN KEY ("id") REFERENCES "user_personal_info"("id");

ALTER TABLE "steps" ADD CONSTRAINT "steps_fk0" FOREIGN KEY ("id") REFERENCES "user_personal_info"("id");

ALTER TABLE "exercise" ADD CONSTRAINT "exercise_fk0" FOREIGN KEY ("id") REFERENCES "user_personal_info"("id");

ALTER TABLE "gps_location" ADD CONSTRAINT "gps_location_fk0" FOREIGN KEY ("id") REFERENCES "user_personal_info"("id");


ALTER TABLE calories ADD COLUMN misc json;
ALTER TABLE exercise ADD COLUMN misc json;
ALTER TABLE gps_location ADD COLUMN misc json;
ALTER TABLE steps ADD COLUMN misc json;
ALTER TABLE user_personal_info  ADD COLUMN misc json;
ALTER TABLE registration_detail ADD COLUMN misc json;


ALTER TABLE registration_detail ADD CONSTRAINT "id_unique" UNIQUE(id);
ALTER TABLE gps_location  ADD COLUMN time float;
ALTER TABLE steps ADD COLUMN time float;

ALTER TABLE user_personal_info ADD COLUMN email varchar(255);
//------------------------------------------------------------------------------------------------


CREATE TABLE login (id varchar(255), access_tkn varchar(255) NOT NULL,email_id varchar(255) PRIMARY KEY,password varchar(255));
 ALTER TABLE login ADD COLUMN misc json;

CREATE TABLE self_challenge(c_id varchar(255) PRIMARY KEY , id varchar(255) , descripition varchar(1200), imageurl varchar(500),eventname varchar(255),steps integer,calories float);




