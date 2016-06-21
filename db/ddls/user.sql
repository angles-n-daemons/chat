-- Create User Table

DROP TABLE IF EXISTS User;

CREATE TABLE User (
  uid CHAR(38) NOT NULL,
  login VARCHAR(100) NOT NULL,
  hash CHAR(64) NOT NULL,
  salt CHAR(32) NOT NULL,
  iterations INTEGER NOT NULL,

  -- can include number of other audit fields if desired.
  PRIMARY KEY (uid)
);