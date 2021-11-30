""" Exercício de fast api (30/11):
Criar um crud para modelos de um pequeno ecommerce. 
Produto, Categoria, Fornecedor, Comprador. """

from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic.main import BaseModel


app = FastAPI(title="CRUD FastAPI - E COMMERCE")


# CRUD PRODUTO #
class BaseModelProduto(BaseModel):
    id: int
    descricao: str
    valor: int


produtos = []


@app.post('/produtos', status_code=status.HTTP_201_CREATED) # Create - cria descricao e valor
def adicionar_produto(produto: BaseModelProduto):
    produtos.append(produto)


@app.get('/produtos', status_code=status.HTTP_200_OK) # Read - lista todos os produtos criados
def listar_produtos():
    return produtos


@app.put('/produtos/{id}', status_code=status.HTTP_202_ACCEPTED) # Update - alterar atributos de produtos
def alterar_produto(id: int, produto: BaseModelProduto): 
    resultado = list(filter(lambda a: a.id == id, produtos)) # traz uma lista filtrando atraves do argumento 'id'
    if not resultado: # caso o resultado 'id' não seja o esperado, retorna uma mensagem
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Produto com a descrição {id} não encontrado')

    produto_encontrado = resultado[0]
    produto_encontrado.id = produto.id
    produto_encontrado.descricao = produto.descricao
    produto_encontrado.valor = produto.valor

    return produto_encontrado


@app.delete('/produtos/{id}', status_code=status.HTTP_202_ACCEPTED)
def remover_produto(id: int):
    resultado = list(filter(lambda a: a[1].id == id, enumerate(produtos)))
    #print(list(enumerate(produtos)))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Produto com a descrição {id} não encontrado')

    i, _ = resultado[0]
    del produtos[i]


# CRUD FORNECEDOR #


