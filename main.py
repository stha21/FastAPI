from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello, FastAPI!"}

@app.get('/about')
def about():
    return {"message": "Welcome to the about page"}

@app.get("/profile")
def profile():
    return {"message": "This is the profile page"}