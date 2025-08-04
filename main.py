from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {
        "item":"guarana",
        "preco_unitario":4,
        "qauntidade":2
    },
    1: {
        "item":"coca_cola",
        "preco_unitario":3.50,
        "qauntidade":6
    },
    1: {
        "item":"pepsi",
        "preco_unitario":3.75,
        "qauntidade":8
    }
}

@app.get("/")
def home():
    return {"Vendas": len(vendas)}

@app.get("/search/{id_venda}")
def pegar_venda(id_venda: int):
    return vendas[id_venda]