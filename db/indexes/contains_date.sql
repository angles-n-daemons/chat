-- Index on Contains table for message retrieval performance

CREATE INDEX contains_date
ON Message (rid, sent_when);