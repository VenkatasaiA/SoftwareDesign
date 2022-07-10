import json
import os
import gc
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file, make_response, \
    Response, jsonify
from portal import create_app
from portal import LOG,APP
from models import db
from datetime import datetime
from helpers import get_random_numbers,validate_gmail

app = create_app()


@app.route('/fuel_quote/check', methods=["GET", "POST"])
def enc_key():
    data = request.json
    reg_username=data['reg_username']
    reg_email=data['reg_email']
    print(data)
    try:
        if reg_username =='Venkata_sai':
            msg="user_name"
            return jsonify({"msg": msg})
    except Exception as e:
        LOG.error("Error occurred while login")
        LOG.error(e, exc_info=True)
    try:
        if reg_email=='venkatasai@gmail.com':
            msg = "email_id"
            return jsonify({"msg": msg})
        else:
            msg = "clear"
            return jsonify({"msg": msg})
    except Exception as e:
        LOG.error("Error occurred while login ")
        LOG.error(e, exc_info=True)


@app.route('/fuel_quote/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        invalid_msg = "hidden"
        access_name = "hidden"
        access_pass= "hidden"
        return render_template("login.html", invalid_msg=invalid_msg,access_name=access_name,access_pass=access_pass)
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username =='':
            invalid_msg = "hidden"
            access_name = ""
            access_pass = "hidden"
            return render_template("login.html", invalid_msg=invalid_msg, access_name=access_name,access_pass=access_pass),200
        if password =='':
            invalid_msg = "hidden"
            access_name = "hidden"
            access_pass = ""
            return render_template("login.html", invalid_msg=invalid_msg, access_name=access_name,
                                   access_pass=access_pass)
        try:
            if username=='Venkata_sai':
                session["user"] = username
                session["user_uid"] = "1234567890"
                session["id"] = "1"
                session["status"]='completed'
                return redirect(url_for("fuel_quote_history"))
            else:
                session["user"] = username
                session["user_uid"] = "12345678902"
                session["username"] = username
                session["email_id"] = "vamshi@gmail.com"
                session["id"] = "2"
                UID="12345678902"
                Username=username
                Email_Id="vamshi@gmail.com"
                First_Name = ""
                Last_Name = ""
                Address_1 = ""
                Address_2 = ""
                country = "0"
                state_code = ""
                City_name=""
                Zip_Code=""
                Phone_Number=""
                return render_template("client_profile_management.html", UID=UID, Username=Username,
                                       Email_Id=Email_Id,First_Name=First_Name,Last_Name=Last_Name,Address_1=Address_1,Address_2=Address_2
                                       ,country=country,state_code=state_code,City_name=City_name,Zip_Code=Zip_Code,Phone_Number=Phone_Number
                                       )
        except Exception as e:
            LOG.error("Error occurred while login ")
            LOG.error(e, exc_info=True)
        invalid_msg = ""
        access_name = "hidden"
        access_pass="hidden"
        return render_template("login.html",invalid_msg=invalid_msg,access_name=access_name,access_pass=access_pass)


@app.route('/fuel_quote/client_registration', methods=['POST'])
def client_registration():
    if request.method == "POST":
        data = request.json
        if not(len(data['reg_username']) <=50):
            msg = "User name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not validate_gmail(data['reg_email']):
            msg = "Invalid Gmail"
            Status = {"status": msg}
            return jsonify(Status)
        else:
            msg = "successfully registered"
            Status = {"status": msg}
            return jsonify(Status)


@app.route('/fuel_quote/client_profile_management', methods=['GET','POST'])
def client_profile_management():
    if request.method == "GET":
        e1=''
        e2=''
        try:
            data =request.json
            e1=data['status']
            e2=data['id']
        except:
            pass
        if session.get("status")=='completed' or e1=='completed':
            if session.get("id") =='1' or e2=='1':
                session["user"] = "Venkata_sai"
                session["user_uid"] = "1234567890"
                session["username"] ="Venkata_sai"
                session["email_id"] = "Venkata_sai@gmail.com"
                session["id"] ="1"
                UID = "1234567890"
                Username = "Venkata_sai"
                Email_Id = "Venkata_sai@gmail.com"
                First_Name = "Venkata Sai PVT"
                Last_Name = ""
                Address_1 = "4800 Calhoun Rd, Houston, TX 77004, United States"
                Address_2 = "4811 Calhoun Rd, Houston, TX 77004, United States"
                country ="US"
                state_code ="CA"
                City_name = "callifornia"
                Zip_Code = "77001"
                Phone_Number = "1234567890"
                return render_template("client_profile_management.html", UID=UID, Username=Username,
                                       Email_Id=Email_Id, First_Name=First_Name, Last_Name=Last_Name,
                                       Address_1=Address_1, Address_2=Address_2
                                       , country=country, state_code=state_code, City_name=City_name, Zip_Code=Zip_Code,
                                       Phone_Number=Phone_Number
                                       )
            else:
                if session.get("id") =='2' or e2=='2':
                    session["user"] = "vamshi"
                    session["user_uid"] = "1234567891"
                    session["username"] ="vamshi"
                    session["email_id"] = "vamshi@gmail.com"
                    session["id"] ="2"
                    UID = "1234567890"
                    Username = "vamshi"
                    Email_Id = "vamshi@gmail.com"
                    First_Name = "vamshi Sai PVT"
                    Last_Name = ""
                    Address_1 = "4800 Calhoun Rd, Houston, TX 77004, United States"
                    Address_2 = "4811 Calhoun Rd, Houston, TX 77004, United States"
                    country ="US"
                    state_code ="CA"
                    City_name = "callifornia"
                    Zip_Code = "77001"
                    Phone_Number = "1234567891"
                    return render_template("client_profile_management.html", UID=UID, Username=Username,
                                           Email_Id=Email_Id, First_Name=First_Name, Last_Name=Last_Name,
                                           Address_1=Address_1, Address_2=Address_2
                                           , country=country, state_code=state_code, City_name=City_name, Zip_Code=Zip_Code,
                                           Phone_Number=Phone_Number
                                           )
        else:
            session["user"] = "vamshi"
            session["user_uid"] = "1234567891"
            session["username"] = "vamshi"
            session["email_id"] = "vamshi@gmail.com"
            session["id"] = "2"
            UID = "1234567891"
            Username = "vamshi"
            Email_Id = "vamshi@gmail.com"
            First_Name = ""
            Last_Name = ""
            Address_1 = ""
            Address_2 = ""
            country = "0"
            state_code = ""
            City_name = ""
            Zip_Code = ""
            Phone_Number = ""
            return render_template("client_profile_management.html", UID=UID, Username=Username,
                                   Email_Id=Email_Id, First_Name=First_Name, Last_Name=Last_Name,
                                   Address_1=Address_1, Address_2=Address_2
                                   , country=country, state_code=state_code, City_name=City_name, Zip_Code=Zip_Code,
                                   Phone_Number=Phone_Number
                                   )


@app.route('/fuel_quote/Update_client', methods=['POST'])
def update_client():
    if request.method == "POST":
        data = request.json
        session['status'] = 'completed'
        First_Name=data["First_Name"]
        Address_1=data["Address_1"]
        Address_2=data["Address_2"]
        Zip_Code=data["Zip_Code"]
        City_name=data["City_name"]
        if not(len(First_Name) <=50):
            msg = "First name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not(len(Address_1) <=100):
            msg = "Address 1 name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not(len(Address_2) <=100):
            msg = "Address 1 is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not(len(Zip_Code) <=9):
            msg = "Zip name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not(len(City_name) <=100):
            msg = "City name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        msg="successfully registered"
        Status = {"status": msg}
        return jsonify(Status)


@app.route('/fuel_quote/fuel_quote_history', methods=['GET','POST'])
def fuel_quote_history():
    main_table = []
    inner_loop = []
    first_username=session.get("user")
    fq=[{"fuel_quote_id":"BKID0907202221064728","fuel_type":"Diesel","cur_gallon_price":"5.718","quantity":"8"
            ,"total_price":"52.148160000000004	","created_date":"2022-07-10 01:40:51","delivery_date":"2022-07-26 00:00:00"
         },
        {"fuel_quote_id": "BKID1007202201405166", "fuel_type": "Gasoline", "cur_gallon_price": "5.006",
         "quantity": "8"
            , "total_price": "45.654720000000005", "created_date": "2022-07-10 01:47:11",
         "delivery_date": "2022-07-11 00:00:00"
         }
        ]
    for Quote in fq:
        inner_loop.append(Quote['fuel_quote_id'])
        inner_loop.append(Quote["fuel_type"])
        inner_loop.append(Quote["cur_gallon_price"])
        inner_loop.append(Quote["quantity"])
        inner_loop.append(Quote["total_price"])
        inner_loop.append(Quote["created_date"])
        inner_loop.append(Quote["delivery_date"])
        main_table.append(inner_loop)
        inner_loop = []
    count_row = len(main_table)
    return render_template("fuel_quote_history.html",main_table=main_table,count_row=count_row,first_username=first_username)

@app.route('/fuel_quote/fuel_quote_form', methods=['GET','POST'])
def fuel_quote_form():
    try:
        if request.method == "GET":
            id = "1234567890"
            Username = "Venkata_sai"
            email_id = "Venkata_sai@gmail.com"
            Office_Name = "Venkata Sai PVT"
            delivery_address = "4800 Calhoun Rd, Houston, TX 77004, United States"
            Country = "US"
            state = "CA"
            city = "callifornia"
            zipcode = "77001"
            mobile_number = "1234567890"
            return render_template("fuel_quote_form.html", id=id, Office_Name=Office_Name,
                                   delivery_address=delivery_address,
                                   Country=Country, state=state, zipcode=zipcode, city=city, email_id=email_id,
                                   mobile_number=mobile_number)
        if request.method == "POST":
            data = request.json
            fuel_quote_id = "BKID" + datetime.now().strftime("%d%m%Y%H%M%S") + get_random_numbers(2)
            msg = "successfully Saved"
            Status = {"status": msg}
            return jsonify(Status)
    except Exception as e:
        LOG.error("Error occurred while login ")
        LOG.error(e, exc_info=True)



@app.route('/fuel_quote/logout', methods=['GET','POST'])
def logout():
    if request.method == "GET":
        invalid_msg = "hidden"
        access_name = "hidden"
        access_pass = "hidden"
        session.clear()
        return render_template("login.html", invalid_msg=invalid_msg,access_name=access_name,access_pass=access_pass)


if __name__ == "__main__":
    app.run()