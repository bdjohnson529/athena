DROP TABLE IF EXISTS inverted_index;


CREATE TABLE inverted_index (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Term varchar NOT NULL,
  Frequency varchar NOT NULL,
  Postings varchar NOT NULL
);