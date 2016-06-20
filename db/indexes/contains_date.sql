-- Index on Contains table for message retrieval performance

CREATE INDEX contains_date
ON Sent (rid, sent_when);