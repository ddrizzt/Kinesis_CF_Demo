DROP TABLE IF EXISTS books;
CREATE TABLE books (
  book_id BIGINT NULL ENCODE LZO,
  isbn VARCHAR(20) NULL ENCODE LZO,
  authors VARCHAR(100) NULL ENCODE LZO,
  original_publication_year VARCHAR(20) NULL ENCODE LZO,
  original_title VARCHAR(512) NULL ENCODE LZO,
  title VARCHAR(512) NULL ENCODE LZO,
  language_code VARCHAR(20) NULL ENCODE LZO,
  small_image_url VARCHAR(512) NULL ENCODE LZO,
  updated_at TIMESTAMP NULL DEFAULT getdate() ENCODE LZO
);

DROP TABLE IF EXISTS rating;
CREATE TABLE rating (
  logtime timestamp null encode lzo,
  user_id BIGINT NULL ENCODE LZO,
  book_id BIGINT NULL ENCODE LZO,
  rating INT NULL ENCODE LZO,
  updated_at TIMESTAMP NULL DEFAULT getdate() ENCODE LZO
);

GRANT ALL ON TABLE books TO PUBLIC;
GRANT ALL ON TABLE rating TO PUBLIC;

COPY books (book_id, isbn, authors, original_publication_year, original_title, title, language_code, small_image_url)
FROM 's3://gd-shdevops/eason/datastream/books_new.tar.gz'
CREDENTIALS 'aws_access_key_id=AKIAIAFIFMS6PVJ47WCA;aws_secret_access_key=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'
GZIP
REGION 'us-west-1'
EMPTYASNULL
TRUNCATECOLUMNS
DELIMITER '\t'
TIMEFORMAT 'YYYY-MM-DD HH:MI:SS';

