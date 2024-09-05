# Advanced API Project - Django REST Framework

## Overview

This project demonstrates advanced API development using Django REST Framework (DRF). It includes custom views and generic views for handling CRUD operations on the `Book` model.

## API Endpoints

### 1. List and Create Books

- **Endpoint:** `/books/`
- **Methods:**
  - `GET`: Retrieve a list of all books.
  - `POST`: Create a new book (authentication not required).

- **Permissions:**
  - `GET`: Public access (anyone can view the list of books).
  - `POST`: Requires authentication (only authenticated users can create a new book).

- **Custom Behavior:**
  - Custom logic before saving a new book can be implemented in the `perform_create` method.

### 2. Retrieve, Update, and Delete a Book

- **Endpoint:** `/books/<int:pk>/`
- **Methods:**
  - `GET`: Retrieve the details of a specific book by its ID.
  - `PUT`: Update the book’s details (authentication required).
  - `DELETE`: Delete the book (authentication required).

- **Permissions:**
  - `GET`: Public access (anyone can view the details of a book).
  - `PUT` and `DELETE`: Requires authentication (only authenticated users can update or delete a book).

- **Custom Behavior:**
  - The view is restricted to authenticated users only, ensuring that only authorized users can modify or delete books.

## Permissions

- **Public Access:** The `BookListView` allows public access for retrieving the list of books.
- **Authenticated Access:** The `BookDetailView` restricts modification and deletion actions to authenticated users.

## Testing

- **List Books:** `GET` request to `/books/`
- **Create Book:** `POST` request to `/books/` with authentication
- **Retrieve Book:** `GET` request to `/books/<id>/`
- **Update Book:** `PUT` request to `/books/<id>/` with authentication
- **Delete Book:** `DELETE` request to `/books/<id>/` with authentication

## Notes

- Ensure proper authentication is handled when interacting with `POST`, `PUT`, and `DELETE` requests.
- Custom logic for creating books can be added to the `perform_create` method in `BookListView`.


## API Filtering, Searching, and Ordering

### Filtering
- **Filter by Title:** `/books/?title=<title>`
- **Filter by Author:** `/books/?author=<author_id>`
- **Filter by Publication Year:** `/books/?publication_year=<year>`

### Searching
- **Search by Title or Author:** `/books/?search=<query>`

### Ordering
- **Order by Title:** `/books/?ordering=title`
- **Order by Publication Year:** `/books/?ordering=publication_year`

*Examples of how to use these features are provided above. Adjust the query parameters as needed to filter, search, or order the book data.*





# API Testing

## Testing Overview

This project uses Django’s built-in testing framework to ensure API endpoints are functioning as expected. 

## Test Cases

- **Create Book:** Tests POST requests to add new books.
- **Get Book:** Tests GET requests to retrieve book details.
- **Update Book:** Tests PATCH requests to update book information.
- **Delete Book:** Tests DELETE requests to remove books.
- **Filter Books:** Tests filtering books by title.
- **Search Books:** Tests searching for books by title.
- **Order Books:** Tests ordering books by title.
- **Permissions:** Tests that unauthorized requests are properly restricted.

## Running Tests

Run the tests with:
```bash
python manage.py test api
