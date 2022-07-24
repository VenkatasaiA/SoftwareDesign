from flask import flash
import json
#from portal import APP as app
from portal import create_app
import os
import tempfile
import pytest

app=create_app()

# @pytest.fixture
# def client():
#     app.config.update({'TESTING': True})
#     with app.test_client() as client:
#         yield client

class TestCheck():
    def test_check_1(self):
        client=app.test_client()
        url='/fuel_quote/check'
        form_data={'reg_username':'VenkatSai','reg_email':''}
        response = client.get(url, json=form_data)
        assert response.status_code == 200
    def test_check_2(self):
        client=app.test_client()
        url='/fuel_quote/check'
        form_data={'reg_username':'VenkatSai123','reg_email':'VenkatSai@gmail.com'}
        response = client.get(url, json=form_data)
        assert response.status_code == 200
    def test_check_3(self):
        client=app.test_client()
        url='/fuel_quote/check'
        form_data={'reg_username':'VenkatSai123','reg_email':'VenkatSai1234@gmail.com'}
        response = client.get(url, json=form_data)
        assert response.status_code == 200


class TestLogin():
    def test_login_1(self):
        client=app.test_client()
        print(client)
        url='/fuel_quote/'
        response = client.get(url)
        assert response.status_code == 200
    def test_login_2(self):
        client=app.test_client()
        print(client)
        url='/fuel_quote/'
        data={"username":"","password":""}
        response = client.post(url,data=data)
        assert response.status_code == 200

    def test_login_3(self):
        client=app.test_client()
        print(client)
        url='/fuel_quote/'
        data={"username":"VenkatSai","password":""}
        response = client.post(url,data=data)
        assert response.status_code == 200

    def test_login_4(self):
        client=app.test_client()
        print(client)
        url='/fuel_quote/'
        data={"username":"VenkatSai","password":"Test@123678"}
        response = client.post(url,data=data)
        assert response.status_code == 200

    def test_login_5(self):
        client=app.test_client()
        print(client)
        url='/fuel_quote/'
        data={"username":"VenkatSai","password":"11111111"}
        response = client.post(url,data=data)
        assert response.status_code == 302

    def test_login_6(self):
        client=app.test_client()
        print(client)
        url='/fuel_quote/'
        data={"username":"Vamshi_123","password":"11111111"}
        response = client.post(url,data=data)
        assert response.status_code == 200


class TestClientRegistration():
    def test_client_registration_1(self):
        client = app.test_client()
        print(client)
        url = '/fuel_quote/client_registration'
        data = {"reg_username": "50 words handwritten and single-spaced produces Yeah",
                "reg_email": "Sandeep@gmail.com", "reg_password": "11111111"}
        response = client.post(url, json=data)
        assert response.status_code == 200

    def test_client_registration_2(self):
        client = app.test_client()
        print(client)
        url = '/fuel_quote/client_registration'
        data = {"reg_username": "Sandeep_kumar", "reg_email": "Sandeepgmail.com", "reg_password": "11111111"}
        response = client.post(url, json=data)
        assert response.status_code == 200

    def test_client_registration_3(self):
        client = app.test_client()
        print(client)
        url = '/fuel_quote/client_registration'
        data = {"reg_username": "Sandeep_kumar", "reg_email": "Sandeep@gmail.com", "reg_password": "11111111"}
        response = client.post(url, json=data)
        assert response.status_code == 200

    def test_client_registration_4(self):
        client = app.test_client()
        print(client)
        url = '/fuel_quote/client_registration'
        data = {"reg_username": "", "reg_email": "Sandeep@gmail.com", "reg_password": ""}
        response = client.post(url, json=data)
        assert response.status_code == 200


class TestClientProfileManagement():
    def test_client_profile_management_1(self):
        client = app.test_client()
        url = '/fuel_quote/client_profile_management/2407202205263653643'
        response = client.get(url)
        assert response.status_code == 200

    def test_client_profile_management_2(self):
        client = app.test_client()
        url = '/fuel_quote/client_profile_management/2407202207130294980'
        response = client.get(url)
        assert response.status_code == 200


class TestUpdateClient:
    def test_update_client_1(self):
        client = app.test_client()
        url = '/fuel_quote/Update_client/2407202207130294980'
        data = {
            "First_Name": "50 words handwritten and single-spaced produces Yeah 50 words handwritten and single-spaced produces Yeah",
            "Address_1": "Sandeep@gmail.com", "Address_2": "11111111", "Zip_Code": "", "City_name": ""}
        response = client.post(url, json=data)
        assert response.status_code == 200

    def test_update_client_2(self):
        client = app.test_client()
        url = '/fuel_quote/Update_client/2407202207130294980'
        data = {"First_Name": "Sandeep_kumar",
                "Address_1": "50 words handwritten and single-spaced produces Yeah50 words handwritten and single-spaced produces Yeah",
                "Address_2": "11111111", "Zip_Code": "", "City_name": ""}
        response = client.post(url, json=data)
        assert response.status_code == 200

    def test_update_client_3(self):
        client = app.test_client()
        url = '/fuel_quote/Update_client/2407202207130294980'
        data = {"First_Name": "Sandeep_kumar", "Address_1": "Sandeep gmail.com",
                "Address_2": "50 words handwritten and single-spaced produces Yeah50 words handwritten and single-spaced produces Yeah",
                "Zip_Code": "", "City_name": ""}
        response = client.post(url, json=data)
        assert response.status_code == 200

    def test_update_client_4(self):
        client = app.test_client()
        url = '/fuel_quote/Update_client/2407202207130294980'
        data = {"First_Name": "Sandeep_kumar", "Address_1": "Sandeep@gmail.com", "Address_2": "11111111",
                "Zip_Code": "1111111111", "City_name": "50 words"}
        response = client.post(url, json=data)
        assert response.status_code == 200

    def test_update_client_5(self):
        client = app.test_client()
        url = '/fuel_quote/Update_client/2407202207130294980'
        data = {"First_Name": "Sandeep_kumar", "Address_1": "Sandeep@gmail.com", "Address_2": "11111111",
                "Zip_Code": "11111111",
                "City_name": "handwritten and single-spaced produces Yeah50 words handwritten and single-spaced produces Yeah produces producesproducesproduces "}
        response = client.post(url, json=data)
        assert response.status_code == 200

    def test_update_client_6(self):
        client = app.test_client()
        url = '/fuel_quote/Update_client/2407202205263653643'
        data = {"First_Name": "Sandeep_kumar", "Address_1": "Sandeep adfsd", "Address_2": "11111111","Zip_Code": "11111111",
                "City_name": "HYD","Phone_Number":"9542192823","state_code":'09',"country":"DZ"}
        response = client.post(url, json=data)
        assert response.status_code == 200


class TestFuelQuoteHistory():
    def test_fuel_quote_history_1(self):
        client = app.test_client()
        url = '/fuel_quote/fuel_quote_history/2407202205263653643'
        response = client.get(url)
        assert response.status_code == 200


class TestFuelQuoteForm():
    def test_fuel_quote_form_1(self):
        client = app.test_client()
        print(client)
        url = '/fuel_quote/fuel_quote_form/2407202205263653643'
        response = client.get(url)
        assert response.status_code == 200

    def test_fuel_quote_form_2(self):
        client = app.test_client()
        print(client)
        url = '/fuel_quote/fuel_quote_form/2407202205263653643'
        data = {"quantity_quote": "8",
                "Gallon_price": "5.006",
                "Total_Amount_Due": "45.654720000000005",
                "fuel_type":"Gasoline",
                "cur_gst":"14%",
                "bdate":"2022-07-15 00:00:00"}
        response = client.post(url, json=data)
        assert response.status_code == 200

class TestLogOut():
    def test_log_out_1(self):
        client = app.test_client()
        print(client)
        url = '/fuel_quote/logout'
        response = client.get(url)
        assert response.status_code == 200






# tent =TestClientProfileManagement()
#
# response12 =tent.test_client_profile_management_2()
# print(response12.request)
# print(response12,"123")