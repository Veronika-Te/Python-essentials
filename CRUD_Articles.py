from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Definition of a Pydantic model named "Item" with three fields: id, name, and price.
class Article(BaseModel):
    id: int
    name: str
    price: float

# Empty list to store created articles.
articles = []

# Route for the home page that returns a welcome message.
@app.get('/')
def welcome():
    return {'message': 'Welcome to my FastAPI application'}

# Route to get all articles stored in the list.
# The "response_model" parameter specifies that the response will be a list of "Article" objects.
@app.get("/articles", response_model=List[Article])
async def read_articles():
    return articles

# Route to create a new article.
# The "response_model" parameter specifies that the response will be an "Article" object.
@app.post("/articles", response_model=Article)
async def create_article(article: Article):
    articles.append(article)  # Adds the article to the list.
    return article
     
# Route to update an existing article by its ID.
# The "response_model" parameter specifies that the response will be an "Article" object.
@app.put("/articles/{article_id}", response_model=Article)
async def update_article(article_id: int, article: Article):
    articles[article_id] = article  # Updates the article in the list.
    return article

# Route to delete an article by its ID.
# "response_model" is not specified since no object is returned in the response.
@app.delete("/articles/{article_id}")
async def delete_article(article_id: int):
    del articles[article_id]  # Deletes the article from the list.
    return {"message": "Article deleted"}  # Returns an informative message.

if __name__ == "__main__":
    import uvicorn
    HOST="127.0.0.1"
    PORT=8000
    # Start the FastAPI server
    uvicorn.run("CRUD_Articles:app", host=HOST, port=PORT, reload=True)
  
