-- Create Message Table

DROP TABLE IF EXISTS Message;

CREATE TABLE Message (
  mid CHAR(38) NOT NULL,
  rid CHAR(38) NOT NULL,
  uid CHAR(38) NOT NULL,
  login VARCHAR(100) NOT NULL,
  content TEXT, -- note INNODB will store text data types in line until 16K so performance gain for varchar irrelevant.
  sent_when DATETIME,
  FOREIGN KEY (rid) REFERENCES Room (rid),
  FOREIGN KEY (uid) REFERENCES User (uid),
  PRIMARY KEY (mid)
);