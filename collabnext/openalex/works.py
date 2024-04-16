from pyalex import Works, Work, Author

def get_works_by_authors(authors: list[Author]) -> list[Work]:
    works_by_authors = []
    for author in authors:
        works = Works().filter(authorships={"author": {"id": author["id"]}}).get()
        works_by_authors.extend(works)
    return works_by_authors