## Book API Views

This API uses Django REST Framework generic views to handle CRUD operations
for the Book model.

- ListAPIView: retrieves all books
- RetrieveAPIView: retrieves a book by ID
- CreateAPIView: allows authenticated users to add books
- UpdateAPIView: allows authenticated users to update books
- DestroyAPIView: allows authenticated users to delete books

Permissions are enforced using DRF permission classes.
