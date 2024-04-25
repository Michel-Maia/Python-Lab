from fastapi import FastAPI

app = FastAPI()

# no terminal digite uvicorn main(nome arquivo python) : app(nome da api) --reload
# uvicorn main:app --reload
# doc fastapi https://fastapi.tiangolo.com/

vendas = {
    1: {"item": "lata","preco_unitario":4, "quantidade":5},
    2: {"item": "garrafa","preco_unitario":12, "quantidade":7},
    3: {"item": "lata","preco_unitario":5, "quantidade":10},
}


@app.get("/")
def home():
    return {"Vendas":len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_vendas(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID Venda não encontrado"}