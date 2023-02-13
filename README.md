<h1>Teste para à vaga de dev</h1>

## Instalação do projeto.
Para utilizar voce precisa primeiro, executar o comando:
```
pip install requirements.txt
```
execute os comandos:
```
python manage.py makemigrations / python manage.py migrate
```

Depois excute o projeto:
```
python manage.py runserver
```

# Utilize o Postman ou insomnia para fazer requisição a API.
## Links da API endpoint PRODUCTS:

Buscar dados por filtro: method [GET]

* "score-asc" ==> Produtos com maior score,<br>
* "score-desc" ==> Produtos com menor score,
* "order-alpha" ==> Produtos em ordem em alfabética,
* "low-price" ==> Produtos com menor preço,
* "big-price" ==> Produtos com maior preço,
* "all-products" ==> Todos os produtos

``` 
http://127.0.0.1:8000/products/list-products/{filtro} ==> Utilize os que estão entre aspas.
```
adicionar produtos: method [POST]
```
http://127.0.0.1:8000/products/create-products/
```
---------------------------------

## Links da API endpoint User:
Fazer login: method [POST]
```
http://127.0.0.1:8000/user/login/
``` 
-----
## Links da API endpoint SHOPPINGCART:
Fazer pedido: method [POST]
``` 
http://127.0.0.1:8000/shoppingcart/carrinho-post/
``` 

Ver meus pedidos: method [GET]<br>
obs: é passado o ID do user no final:
``` 
http://127.0.0.1:8000/shoppingcart/carrinho-mylist/{id}
``` 
