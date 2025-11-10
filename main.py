from fastapi import Depends, FastAPI

from schemas import UsuarioCreate
from security import verificar_token

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API do minicurso de FastAPI!"}


@app.get("/saudacao/{nome}")
def greetings(nome: str):
    return {"mensagem": f"Olá, {nome}!"}

@app.post("/create_user", dependencies=[Depends(verificar_token)])
def create_user(data: UsuarioCreate):
    data = {
        "mensagem": "Usuário criado com sucesso!",
        "object": data.model_dump()
        }

    return data

