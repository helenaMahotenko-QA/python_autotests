import requests
import json

token='79ef786dcc62447123d6722b7fe96adf'

create=requests.post('https://pokemonbattle.me:5000/pokemons',headers={'Content-Type':'application/json','trainer_token':token},json={
    "name": "Чужой",
    "photo": "https://www.pngmart.com/files/13/Mewtwo-Pokemon-Species-PNG-File.png"
}) 

pokemon_id=create.json()['id']

print(create.text)

change=requests.put('https://pokemonbattle.me:5000/pokemons',headers={'Content-Type':'application/json','trainer_token':token},json={
    "pokemon_id": pokemon_id,
    "name": "Mewtwo",
}) 

print(change.text)

add=requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',headers={'Content-Type':'application/json','trainer_token':token},json={
    "pokemon_id": pokemon_id,
    }) 

print(add.text)
