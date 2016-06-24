-- Create User Table

DROP TABLE IF EXISTS User;

CREATE TABLE User (
  uid CHAR(38) NOT NULL,
  login VARCHAR(100) NOT NULL UNIQUE,
  hash CHAR(64),
  salt CHAR(32),
  iterations INTEGER,

  -- can include number of other audit fields if desired.
  PRIMARY KEY (uid)
);