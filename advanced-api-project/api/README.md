## Book API Views

This API uses Django REST Framework generic views to handle CRUD operations
for the Book model.

- ListAPIView: retrieves all books
- RetrieveAPIView: retrieves a book by ID
- CreateAPIView: allows authenticated users to add books
- UpdateAPIView: allows authenticated users to update books
- DestroyAPIView: allows authenticated users to delete books

Permissions are enforced using DRF permission classes.






## Filtering, Searching, and Ordering

The Book list endpoint supports advanced query features.

### Filtering
Filter books by fields such as title, author, and publication year.

Example:
GET /api/books/?publication_year=2022

### Searching
Text-based search is enabled for title and author fields.

Example:
GET /api/books/?search=django

### Ordering
Results can be ordered by title or publication year.

Example:
GET /api/books/?ordering=-publication_year





## API Testing

Unit tests were written using Django REST Framework’s APITestCase.

The tests cover:
- CRUD operations for the Book model
- Filtering, searching, and ordering functionality
- Authentication and permission enforcement

### Running Tests
python manage.py test api

All tests run against a separate test database automatically created by Django.
