from pydantic import BaseModel, Field

class UsuarioCreate(BaseModel):
    nome: str = Field(...)
    email: str = Field(...)
    idade: int = Field(...)
    profissao: str = Field(default="Prestador Externo")

