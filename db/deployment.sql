DROP TABLE IF EXISTS Sent;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Room;
DROP TABLE IF EXISTS Message;


CREATE TABLE User (
  uid CHAR(38) NOT NULL,
  login VARCHAR(100),
  hash CHAR(64) NOT NULL,
  salt CHAR(32) NOT NULL,
  PRIMARY KEY (uid)
);

CREATE TABLE Room (
  rid CHAR(38) NOT NULL,
  name VARCHAR(150) NOT NULL,
  PRIMARY KEY (rid)
);

CREATE TABLE Message (
  mid CHAR(38) NOT NULL,
  content TEXT,
  PRIMARY KEY (mid)
);

CREATE TABLE Sent (
  rid CHAR(38) NOT NULL,
  mid CHAR(38) NOT NULL,
  uid CHAR(38) NOT NULL,
  sent_when DATETIME NOT NULL,
  PRIMARY KEY (rid, mid),
  FOREIGN KEY (rid) REFERENCES Room (rid),
  FOREIGN KEY (uid) REFERENCES User (uid),
  FOREIGN KEY (mid) REFERENCES Message (mid)
);

CREATE INDEX contains_date
ON Sent (rid, sent_when);