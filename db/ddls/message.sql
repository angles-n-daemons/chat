-- Create Message Table

DROP TABLE IF EXISTS Message;

CREATE TABLE Message (
  mid CHAR(38) NOT NULL,
  content TEXT, -- note INNODB will store text data types in line until 16K so performance gain for varchar irrelevant.
  PRIMARY KEY (mid)
);