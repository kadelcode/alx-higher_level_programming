-- script that ceates the database `hbtn_0d_usa` and the table `cities` (in the db `hbtn_0d_usa`)
CREATE DATABASE hbtn_0d_usa;

CREATE TABLE hbtn_0d_usa.cities (
	`id` INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
