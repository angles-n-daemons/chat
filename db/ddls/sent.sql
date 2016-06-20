-- Create Sent Table

DROP TABLE IF EXISTS Sent;

CREATE TABLE Sent (
  rid CHAR(38) NOT NULL,
  mid CHAR(38) NOT NULL,
  sent_when DATETIME NOT NULL,
  PRIMARY KEY (rid, mid),
  FOREIGN KEY (rid) REFERENCES Room (rid),
  FOREIGN KEY (mid) REFERENCES Message (mid)
);