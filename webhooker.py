from fastapi import FastAPI
import os

app = FastAPI()

@app.post("/update")
def update_site():
    print("Atualizando o site. Executando o comando git pull")
    os.system("sudo git pull")    


@app.get("/it-works")
def it_works():
    print("It works!")
    return {"message": "It works!"}
