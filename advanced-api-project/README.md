# Advanced API Project

## API Endpoints

### List and Create Books

- **Endpoint:** `/books/`
- **Methods:** GET, POST
- **Permissions:** Read-only for unauthenticated users, full access for authenticated users.

### Retrieve, Update, and Delete Book

- **Endpoint:** `/books/<int:pk>/`
- **Methods:** GET, PUT, PATCH, DELETE
- **Permissions:** Read-only for unauthenticated users, full access for authenticated users.

## Permissions

- **IsAuthenticatedOrReadOnly:** Allows read-only access for unauthenticated users and full access for authenticated users.
