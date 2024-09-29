-- Insert authors data
INSERT INTO authors (author_id, first_name, last_name, year_born) 
VALUES 
('06cf58ab-90f1-448d-8e54-055e4393e75c', 'George R.R.', 'Martin', 1948),
('18760ec1-0591-4137-ae0b-cf52b3ec0da5', 'David', 'Mitchell', 1969),
('1f6a7f1b-2e4b-4b3b-8b4b-0b2b1b2b1b2b', 'Margaret', 'Atwood', 1939),
('2b3b1b2b-3b4b-4b5b-8b6b-0b7b1b2b1b2', 'Philip', 'Pullman', 1946),
('b3e3b39a-4b9d-467b-b60b-c2efbeffde25', 'Neil', 'Gaiman', 1960),
('c77632ea-f251-49c4-bc8b-f9b77b6d7f4b', 'Stephen', 'King', 1947),
('47b4b44d-1d29-45ea-8dff-99645d963a5a', 'Ann', 'Patchett', 1963),
('0078aebb-0508-4998-82c8-dbd3da5bbb9a', 'Patrick', 'Rothfuss', 1973),
('573ee3e9-431d-4f2e-ad15-b55ee793e21b', 'Yuval Noah', 'Harari', 1976),
('c6815a60-ebad-47ea-ae27-0bfb8badb824', 'Nicholas', 'Carr', 1959)

-- Insert books data
INSERT INTO books (book_id, title, year_published, author_id) 
VALUES 
('c8e87338-49cd-406a-bf78-55583563bad5', 'A Storm of Swords', 2000, '06cf58ab-90f1-448d-8e54-055e4393e75c'),
('9da8ce37-fae2-403b-89de-db73866af250', 'Cloud Atlas', 2004, '18760ec1-0591-4137-ae0b-cf52b3ec0da5'),
('9ec5aaa3-8ff0-4db6-9639-1e85f855d424', 'The Handmaid''s Tale', 1985, '1f6a7f1b-2e4b-4b3b-8b4b-0b2b1b2b1b2b'),
('840e7bcd-5572-441b-9816-9d7aa6cd6275', 'The Subtle Knife', 1997, '2b3b1b2b-3b4b-4b5b-8b6b-0b7b1b2b1b2'),
('513a4d98-bfad-491e-9d91-f527aef39548', 'American Gods', 2001, 'b3e3b39a-4b9d-467b-b60b-c2efbeffde25'),
('a050c07a-3b80-44a0-8e97-8bb01149b865', 'The Stand', 1978, 'c77632ea-f251-49c4-bc8b-f9b77b6d7f4b'),
('1e209ae9-2ed7-484c-94ee-b3e4979bcf26', 'Bel Canto', 2001, '47b4b44d-1d29-45ea-8dff-99645d963a5a'),
('839eb4e9-c582-4a49-a076-a0bdcc139ccd', 'The Name of the Wind', 2007, '0078aebb-0508-4998-82c8-dbd3da5bbb9a'),
('5faeee3e-531f-4708-91ce-daa371cbc8c6', 'Sapiens: A Brief History of Humankind', 2011, '573ee3e9-431d-4f2e-ad15-b55ee793e21b'),
('b3e3b39a-4b9d-467b-b60b-c2efbeffde25', 'The Shallows: What the Internet is Doing to Our Brains', 2010, 'c6815a60-ebad-47ea-ae27-0bfb8badb824');
