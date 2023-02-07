import requests
import pytest

def test_status_code():
    response=requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code==200

@pytest.mark.parametrize('key,value',[('trainer_name','Elma')])

def test_trainer_name(key,value):
    response=requests.get('https://pokemonbattle.me:5000/trainers',params={'trainer_id':'2119'})
    assert response.json()[key]==value
