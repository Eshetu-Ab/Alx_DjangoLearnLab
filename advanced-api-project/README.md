# Advanced API Project

## Custom Views and Generic Views

This project demonstrates the use of Django REST Framework's generic views and custom views for handling CRUD operations on `Book` objects.

### API Endpoints:

- **List all books**: `GET /books/`
- **Retrieve a single book**: `GET /books/<int:pk>/`
- **Create a new book**: `POST /books/` (Authenticated users only)
- **Update a book**: `PUT /books/<int:pk>/` (Authenticated users only)
- **Delete a book**: `DELETE /books/<int:pk>/` (Authenticated users only)

### Permissions:

- Unauthenticated users can view books (list and detail views).
- Authenticated users can create, update, and delete books.
