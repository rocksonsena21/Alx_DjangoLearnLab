
---

## 📄 `CRUD_operations.md`

```markdown
# Django ORM CRUD Operations – Book Model

## Create
```python
Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)


<Book: 1984>
Book.objects.all()
<QuerySet [<Book: 1984>]>

book.title = "Nineteen Eighty-Four"
book.save()

<Book: Nineteen Eighty-Four>

book.delete()
Book.objects.all()

<QuerySet []>
