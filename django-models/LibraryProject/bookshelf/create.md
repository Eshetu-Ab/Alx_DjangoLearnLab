## Create Operation

**Command:**
```python
from bookshelf.models import Book



Book.objects.create(
    title="1984",
    author="George Orwell",
    published_date="1949-06-08"
)

