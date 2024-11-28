from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date
from starlette import status
import uvicorn

app=FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: date
  

    def __init__(self, id:int, title: str, author:str, description:str, rating:int,published_date:date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
       

class BookRequest(BaseModel):
    
    id: Optional[int] = Field(description="Id is not needed for create", default=None) 
    #using Field to validate data
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=0, max_length=100) #not allowed to exceed 100
    #rating between 0 and 5
    rating: int = Field(gt=-1, lt=6) #if gt=0 rating should be between 1 and 5
    published_date: date =Field(gt=date(2000,1,1), lt=date(2027,1,1))
    #for changing example values
    model_config={
        "json_schema_extra":{
            "example":{
                "title": "A new book",
                "author": "Coding with ruby",
                "description": "A new description",
                "rating" : 5,
                "published date": 1990-10-7
            }
        }
    }
 
        
BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, date(2020,12,8)),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, date(1998,11,8)),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, date(1977,9,8)),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, date(1944,7,8)),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, date(1947,7,7)),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, date(1989,4,3)),
    Book(7, 'HP4', 'Author 4', 'Book Description', 1, date(1989,4,3))
]



@app.get("/books", status_code=status.HTTP_200_OK)  #after read all books is successful we will 200 status code
async def read_all_books():
    return BOOKS     

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')
        

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0,lt=6)):
    books_to_return =[]
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_published_date(book_published_date: date ):
    books_to_return=[]
    for book in BOOKS:
        if book.published_date==book_published_date:
            books_to_return.append(book)
    return books_to_return

    
@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    #transforming book_request into book
    new_book=Book(**book_request.model_dump()) #or  .dict() depends on pydantic 1 or 2
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))

@app.put("/books/update_book/", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):    #for published_date this format--"published_date": "2020-12-08"
    book_changed=False
    for i in range(len(BOOKS)):   
        if BOOKS[i].id==book.id:
           BOOKS[i] = book
           book_changed=True
    if not book_changed:
       raise HTTPException(status_code=404, detail='Item not found')


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int =Path(gt=0) ):
    book_deleted=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted=True
            break
    if not book_deleted:
       raise HTTPException(status_code=404, detail='Item not found')


def find_book_id(book: Book):
    """Sets book ID by incrementing value of last ID in the list"""
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1   
    return book  



def run()->None:
    try:
        HOST="127.0.0.1"
        PORT=8000
        # Start the server
        uvicorn.run("Books_fast_api:app", host=HOST, port=PORT, reload=True, log_level=2)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()