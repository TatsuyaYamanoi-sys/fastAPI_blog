from typing import Optional
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.get("/")
async def index():
    return "Hello restAPI!"

@app.get("/article")
async def article_list(limit: Optional[int]=None, published: bool=True, sort: Optional[str]=None):
    # get article-list
    if sort:
        pass

    if published:
        if limit:
            return {'data': f'{limit} articles from the database'}
        else:
            return {'data': f'all articles from the database'}
    else:
        if limit:
            return {'data': f'{limit} unpublished articles from the database'}
        else:
            return {'data': f'all unpublished articles from the database'}

@app.post("/article")
async def create_article():
    return {'data': 'article is created'}

@app.get("/article/unpublished")
async def unpub_article_list():
    return {'data': 'unpublished_articles'}

@app.get("/article/{id}")
async def article_detail(id: int):
    # fetch article with id
    return {'article_id': id}

@app.get("/article/{id}/comments")
async def article_comments(id: int, limit: Optional[int]=None):
    # fetch comments of article with id
    comments = [f'comment{i}' for i in range(10)]
    if limit:
        return {'data': comments[:limit]}
    else:
        return {'data': comments}
