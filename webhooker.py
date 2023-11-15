from fastapi import FastAPI
import os

app = FastAPI()

@app.webhooks.post("update")
def update_site():
    print("Updating site")
    # os.system("git pull")   


@app.get("/it-works")
def it_works():
    return {"message": "It works!"}
