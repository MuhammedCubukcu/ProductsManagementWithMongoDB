import requests
class Api:
    get_products = requests.get('https://fakestoreapi.com/products').json()


