from flask import flash
import json
from views import app
import os
import tempfile
import pytest

@pytest.fixture()
def client():
    app.config.update({'TESTING': True})
    app.testing = True
    with app.test_client() as client:
        yield client

def test_base_route_check():
    client=app.test_client()
    print(client)
    url='/fuel_quote/check'
    form_data={'reg_username':'Venkata_sai','reg_email':'YESJA'}
    response = client.get(url, json=form_data)
    assert response.status_code == 200

def test_base_route_check_1():
    client=app.test_client()
    print(client)
    url='/fuel_quote/check'
    form_data={'reg_username':'Sandeep','reg_email':'venkatasai@gmail.com'}
    response = client.get(url, json=form_data)
    assert response.status_code == 200

def test_base_route_check_2():
    client=app.test_client()
    print(client)
    url='/fuel_quote/check'
    form_data={'reg_username':'Sandeep','reg_email':'Sandeep@gmail.com'}
    response = client.get(url, json=form_data)
    assert response.status_code == 200

def test_base_route_login():
    client=app.test_client()
    print(client)
    url='/fuel_quote/'
    response = client.get(url)
    assert response.status_code == 200

def test_base_route_login2():
    client=app.test_client()
    print(client)
    url='/fuel_quote/'
    data={"username":"","password":""}
    response = client.post(url,data=data)
    assert response.status_code == 200

def test_base_route_login3():
    client=app.test_client()
    print(client)
    url='/fuel_quote/'
    data={"username":"Venkata_sai","password":""}
    response = client.post(url,data=data)
    assert response.status_code == 200

def test_base_route_login4():
    client=app.test_client()
    print(client)
    url='/fuel_quote/'
    data={"username":"Venkata_sai","password":"1111111111"}
    response = client.post(url,data=data)
    assert response.status_code == 302


def test_base_route_login5():
    client=app.test_client()
    print(client)
    url='/fuel_quote/'
    data={"username":"Vamshi","password":"1111111111"}
    response = client.post(url,data=data)
    assert response.status_code == 200


def test_base_route_client_registration():
    client=app.test_client()
    print(client)
    url='/fuel_quote/client_registration'
    data={"reg_username":"50 words handwritten and single-spaced produces Yeah","reg_email":"Sandeep@gmail.com","reg_password":"11111111"}
    response = client.post(url,json=data)
    assert response.status_code == 200

def test_base_route_client_registration1():
    client=app.test_client()
    print(client)
    url='/fuel_quote/client_registration'
    data={"reg_username":"Sandeep_kumar","reg_email":"Sandeepgmail.com","reg_password":"11111111"}
    response = client.post(url,json=data)
    assert response.status_code == 200

def test_base_route_client_registration2():
    client=app.test_client()
    print(client)
    url='/fuel_quote/client_registration'
    data={"reg_username":"Sandeep_kumar","reg_email":"Sandeep@gmail.com","reg_password":"11111111"}
    response = client.post(url,json=data)
    assert response.status_code == 200

def test_base_route_client_profile_management():
    client=app.test_client()
    print(client)
    url='/fuel_quote/client_profile_management'
    data={"reg_username":"Sandeep_kumar","reg_email":"Sandeep@gmail.com","reg_password":"11111111"}
    response = client.get(url,json=data)
    assert response.status_code == 200

def test_base_route_client_profile_management1():
    client=app.test_client()
    print(client)
    url='/fuel_quote/client_profile_management'
    data={"status":"completed","id":"1"}
    response = client.get(url,json=data)
    assert response.status_code == 200

def test_base_route_client_profile_management2():
    client=app.test_client()
    print(client)
    url='/fuel_quote/client_profile_management'
    data={"status":"completed","id":"2"}
    response = client.get(url,json=data)
    assert response.status_code == 200

def test_base_route_update_client():
    client=app.test_client()
    print(client)
    url='/fuel_quote/Update_client'
    data={"First_Name":"50 words handwritten and single-spaced produces Yeah 50 words handwritten and single-spaced produces Yeah","Address_1":"Sandeep@gmail.com","Address_2":"11111111","Zip_Code":"","City_name":""}
    response = client.post(url,json=data)
    assert response.status_code == 200

def test_base_route_update_client1():
    client=app.test_client()
    print(client)
    url='/fuel_quote/Update_client'
    data={"First_Name":"Sandeep_kumar","Address_1":"50 words handwritten and single-spaced produces Yeah50 words handwritten and single-spaced produces Yeah","Address_2":"11111111","Zip_Code":"","City_name":""}
    response = client.post(url,json=data)
    assert response.status_code == 200

def test_base_route_update_client2():
    client=app.test_client()
    print(client)
    url='/fuel_quote/Update_client'
    data={"First_Name":"Sandeep_kumar","Address_1":"Sandeep gmail.com","Address_2":"50 words handwritten and single-spaced produces Yeah50 words handwritten and single-spaced produces Yeah","Zip_Code":"","City_name":""}
    response = client.post(url,json=data)
    assert response.status_code == 200

def test_base_route_update_client3():
    client=app.test_client()
    print(client)
    url='/fuel_quote/Update_client'
    data={"First_Name":"Sandeep_kumar","Address_1":"Sandeep@gmail.com","Address_2":"11111111","Zip_Code":"1111111111","City_name":"50 words"}
    response = client.post(url,json=data)
    assert response.status_code == 200

def test_base_route_update_client4():
    client=app.test_client()
    print(client)
    url='/fuel_quote/Update_client'
    data={"First_Name":"Sandeep_kumar","Address_1":"Sandeep@gmail.com","Address_2":"11111111","Zip_Code":"11111111","City_name":"handwritten and single-spaced produces Yeah50 words handwritten and single-spaced produces Yeah produces producesproducesproduces "}
    response = client.post(url,json=data)
    assert response.status_code == 200

def test_base_route_fuel_quote_history():
    client=app.test_client()
    print(client)
    url='/fuel_quote/fuel_quote_history'
    response = client.get(url)
    assert response.status_code == 200

def test_base_route_fuel_quote_form():
    client=app.test_client()
    print(client)
    url='/fuel_quote/fuel_quote_form'
    response = client.get(url)
    assert response.status_code == 200

def test_base_route_fuel_quote_form2():
    client=app.test_client()
    print(client)
    url='/fuel_quote/fuel_quote_form'
    data = {"reg_username": "Sandeep_kumar", "reg_email": "Sandeep@gmail.com", "reg_password": "11111111"}
    response = client.post(url,json=data)
    assert response.status_code == 200

def test_base_route_logout():
    client=app.test_client()
    print(client)
    url='/fuel_quote/logout'
    response = client.get(url)
    assert response.status_code == 200