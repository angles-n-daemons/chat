DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Room;
DROP TABLE IF EXISTS Message;


CREATE TABLE User (
  uid CHAR(38) NOT NULL,
  login VARCHAR(100) NOT NULL UNIQUE,
  hash CHAR(64) NOT NULL,
  salt CHAR(32) NOT NULL,
  iterations INTEGER,
  PRIMARY KEY (uid)
);

CREATE TABLE Room (
  rid CHAR(38) NOT NULL,
  name VARCHAR(150) NOT NULL,
  color_hex VARCHAR(6),
  created DATETIME,
  PRIMARY KEY (rid)
);

CREATE TABLE Message (
  mid CHAR(38) NOT NULL,
  rid CHAR(38) NOT NULL,
  uid CHAR(38) NOT NULL,
  login VARCHAR(100),
  content TEXT,
  sent_when DATETIME,
  FOREIGN KEY (rid) REFERENCES Room (rid),
  FOREIGN KEY (uid) REFERENCES User (uid),
  PRIMARY KEY (mid)
);

CREATE INDEX contains_date
ON Message (rid, sent_when);
