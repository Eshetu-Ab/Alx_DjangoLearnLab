# README.md

## Introduction to Django Development Environment Setup

I installed Django and created a new Django project named LibraryProject. 
This initial setup will serve as the foundation for developing Django applications.

### Integrating Book Model with Django Admin Interface

#### Registering the Book Model
- The `Book` model was registered with the Django admin by modifying `bookshelf/admin.py` to include the `Book` model.

#### Customizing the Admin Interface
- The admin interface for the `Book` model was customized to display the `title`, `author`, and `publication_year` in the list view.
- Filters for `author` and `publication_year` were added to the sidebar for better navigation.
- A search bar was enabled to search for books by `title` or `author`.

#### Steps to Access the Admin Interface
1. Start the Django development server.
2. Navigate to `http://127.0.0.1:8000/admin/`.
3. Log in with the superuser credentials.
4. Manage `Book` entries through the admin interface.
# Permissions and Groups Configuration

## Custom Permissions

Custom permissions added to the `Book` model:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups and Permissions

- **Editors**: Assigned `can_edit` and `can_create` permissions.
- **Viewers**: Assigned `can_view` permission.
- **Admins**: Assigned all permissions.

## Enforcing Permissions

Permissions are enforced in views using the `@permission_required` decorator. For example:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    ...
# CSRF protection enabled for all forms





## HTTPS and Security Configuration

### Django Settings

- **SECURE_SSL_REDIRECT**: Redirects all HTTP requests to HTTPS.
- **SECURE_HSTS_SECONDS**: Sets HSTS to one year.
- **SECURE_HSTS_INCLUDE_SUBDOMAINS**: Applies HSTS to subdomains.
- **SECURE_HSTS_PRELOAD**: Allows inclusion in HSTS preload list.
- **SESSION_COOKIE_SECURE** and **CSRF_COOKIE_SECURE**: Ensures cookies are sent over HTTPS only.
- **X_FRAME_OPTIONS**: Prevents clickjacking.
- **SECURE_CONTENT_TYPE_NOSNIFF**: Prevents MIME-sniffing.
- **SECURE_BROWSER_XSS_FILTER**: Enables XSS filtering.

### Deployment Configuration

- **Nginx Configuration**: Includes HTTPS redirection and SSL settings.

### Security Review

The application has been configured to enforce HTTPS, use secure cookies, and implement additional security headers. Ensure your deployment environment has SSL/TLS certificates properly configured.
