from fastapi import FastAPI
import os

app = FastAPI()

@app.post("update")
def update_site():
    print("Updating site")
    # os.system("git pull")   