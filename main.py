from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint para ver os cardápios dos restaurantes  
    
    '''
    return {"message": "Hello World"}

@app.get('/api/restaurante')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios
    '''
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados_json = response.json()
        
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item["Item"],
                    "price": item['price'],
                    'description': item['description']
                })
        
        if dados_restaurante:
            return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
        else:
            return {'message': f"Restaurante '{restaurante}' não encontrado."}
        
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}