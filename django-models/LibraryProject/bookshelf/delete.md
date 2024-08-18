## Delete Operation

**Command:**
```python
from bookshelf.models import Book

book = Book.objects.get(pk=1)  # Retrieve the book with ID 1
book.delete()  # Delete the book

Book.objects.filter(title="1984").delete()

