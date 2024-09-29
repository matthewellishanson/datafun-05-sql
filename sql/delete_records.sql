--Delete redundant record from the authors table
DELETE FROM authors
WHERE author_id = '06cf58ab-90f1-448d-8e54-055e4393e75c' -- Love you, JRR, but you only get one row to rule them all. 

DELETE FROM books
WHERE title = "The Hobbit" -- This is the book we're deleting