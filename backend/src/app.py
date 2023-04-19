from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

### urlconf ###
@app.get("/")
async def index():
    return {"message": "hello world!"}

# パスパラメータ
@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {'country': country_name}

# クエリパラメータ ... パスパラメータに設定されていない値はクエリパラメータとして受け取る.
@app.get("/countries/")
async def country(country_name: str = 'japan', country_num: int = 1):
    return {
        'country_name': country_name,
        'country_num': country_num,
    }