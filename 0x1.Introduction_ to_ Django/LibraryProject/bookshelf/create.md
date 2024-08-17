## Create Operation

**Command:**
```python
from bookshelf.models import Book


Book.objects.create(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    published_date="1925-04-10"
)
