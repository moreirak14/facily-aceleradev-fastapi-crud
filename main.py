from typing import List
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()


class BaseAlunoModel(BaseModel):
    name: str
    age: int
    last_name: str
    address: str


class AdicionarAlunoModel(BaseAlunoModel):
    cpf: str


class AlterarAlunoModel(BaseAlunoModel):
    pass


alunos = []


@app.post('/alunos', status_code=status.HTTP_201_CREATED)
def adicionar_aluno(aluno: AdicionarAlunoModel):
    alunos.append(aluno)


@app.get('/alunos')
def lista_alunos():
    return alunos


@app.delete('/alunos/{cpf}', status_code=status.HTTP_204_NO_CONTENT)
def remover_aluno(cpf: str):
    resultado = list(filter(lambda a: a[1].cpf == cpf, enumerate(alunos)))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Aluno com o cpf: {cpf} nao foi encontrado')

    i, _ = resultado[0]
    del alunos[i]


@app.put('/alunos/{cpf}')
def alterar_aluno(cpf: str, aluno: AlterarAlunoModel):
    resultado = list(filter(lambda a: a.cpf == cpf, alunos))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Aluno com o cpf: {cpf} nao foi encontrado')

    aluno_encontrado = resultado[0]
    aluno_encontrado.name = aluno.name
    aluno_encontrado.age = aluno.age
    aluno_encontrado.last_name = aluno.last_name
    aluno_encontrado.address = aluno.address

    return aluno_encontrado


@app.patch('/alunos/alterar-cpf/{cpf}')
def alterar_cpf_aluno(cpf: str, cpf_novo: str = Body(...)):
    resultado = list(filter(lambda a: a.cpf == cpf, alunos))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Aluno com o cpf: {cpf} nao foi encontrado')

    aluno_encontrado = resultado[0]
    aluno_encontrado.cpf = cpf_novo

    return aluno_encontrado