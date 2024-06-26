from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "welcome to my app"}

@app.get("/posts")
def get_posts():
    return {'data': 'this is your posts'}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return{"message":"successfully created post"}

@app.get("/user")
def user():
    return {'data': 'user page'}