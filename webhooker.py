from fastapi import FastAPI
import os

app = FastAPI()

@app.post("/webhook/update")
def update_site():
    print("Atualizando o site. Executando o comando git pull")
    os.system("git pull")    


@app.get("/webhook/it-works")
def it_works():
    print("It works!")
    return {"message": "It works!"}
