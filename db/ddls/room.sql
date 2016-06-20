-- Create Room Table

DROP TABLE IF EXISTS Room;

CREATE TABLE Room (
  rid CHAR(38) NOT NULL,
  name VARCHAR(150) NOT NULL,
  PRIMARY KEY (rid)
);