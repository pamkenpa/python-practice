books = {
    "The Hobbit": {"copies": 3, "checked_out": 1},
    "Dune": {"copies": 2, "checked_out": 2},
    "1984": {"copies": 5, "checked_out": 0}
}

def available_copies(books):
    details = books[books]
    return details["copies"] - details["checked_out"]
        
  
def is_available(books):
    if available_copies(books) > 0:
        return True
    else:
        return False


def checkout_books(books, title):
    try:
        if title in books and is_available:
            details = books[title]
        return details["checked_out"] + 1 and True
    except KeyError:
        return False
    
    if title in books and is_available is False:
        return False

def library_report(books):
    for book in books:
        return {"The Hobbit:", available_copies(book), "available"}

library_report(books)
print(checkout_books(books, "Dune"))
print(checkout_books(books, "The Hobbit"))
library_report(books)
print(checkout_books(books, "Nonexistent Book"))


        
        
    
       
    

