import gc
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file, make_response, \
    Response, jsonify
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from .models.UserCredentials import UserCredentials
from .models.ClientInformation import ClientInformation
from .models.price_management import PriceManagement
from .models.FuelQuote import FuelQuote
from . import LOG, APP
from .models import db
from datetime import datetime
from .helpers import get_random_numbers,validate_gmail
from .security import Encryption

bp = Blueprint('view', __name__, url_prefix='/fuel_quote', template_folder="./templates", static_folder="./static")

@bp.route('/check', methods=["GET", "POST"])
def enc_key():
    data = request.json
    print(data)
    reg_username=data['reg_username']
    reg_email=data['reg_email']
    print(data)
    try:
        users = UserCredentials.query.filter_by(username=reg_username).one()
        print(users.username)
        msg=''
        if users is not None:
            msg="user_name"
            return jsonify({"msg": msg})
    except NoResultFound:
        pass
    except Exception as e:
        LOG.error("Error occurred while login ")
        LOG.error(e, exc_info=True)
    finally:
        db.session.close()
    try:
        users2 = UserCredentials.query.filter_by(email_id=reg_email).one()
        if users2 is not None:
            msg = "email_id"
            return jsonify({
                "msg": msg})
        else:
            msg = "clear"
            return jsonify({
                "msg": msg})
    except NoResultFound:
        pass
    except Exception as e:
        LOG.error("Error occurred while login ")
        LOG.error(e, exc_info=True)
    finally:
        db.session.close()
    Status={"msg": "msg"}
    return jsonify(Status)


@bp.route('/', methods=["GET", "POST"])
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
            return render_template("login.html", invalid_msg=invalid_msg, access_name=access_name,access_pass=access_pass)
        if password =='':
            invalid_msg = "hidden"
            access_name = "hidden"
            access_pass = ""
            return render_template("login.html", invalid_msg=invalid_msg, access_name=access_name,
                                   access_pass=access_pass)
        try:
            encrypted_pwd = Encryption().encrypt(password)
            users = UserCredentials.query.filter_by(username=username, password=encrypted_pwd).one()
            user_id_get=users.user_uid
            print('user_id_get',user_id_get)
            if users is not None:
                if users.status=='completed':
                    session["user"] = username
                    session["user_uid"] = users.user_uid
                    session["id"] = users.Id
                    return redirect(url_for("view.fuel_quote_history",user_uid=users.user_uid))
                else:
                    users = ClientInformation.query.filter_by(user_id=user_id_get).one()
                    session["user"] = username
                    session["user_uid"] = users.user_id
                    session["username"] = users.username
                    session["email_id"] = users.email_id
                    session["id"] = users.Id
                    print('users.Id',users.Id)
                    UID=users.user_id
                    Username=users.username
                    Email_Id=users.email_id
                    First_Name = ""
                    Address_1 = ""
                    Address_2 = ""
                    country = "0"
                    state_code = ""
                    City_name=""
                    Zip_Code=""
                    Phone_Number=""
                    return render_template("client_profile_management.html", UID=UID, Username=Username,
                                           Email_Id=Email_Id,First_Name=First_Name,Address_1=Address_1,Address_2=Address_2
                                           ,country=country,state_code=state_code,City_name=City_name,Zip_Code=Zip_Code,Phone_Number=Phone_Number
                                           )
        except NoResultFound:
            pass
        except Exception as e:
            LOG.error("Error occurred while login ")
            LOG.error(e, exc_info=True)
        finally:
            db.session.close()
        invalid_msg = ""
        access_name = "hidden"
        access_pass="hidden"
        return render_template("login.html",invalid_msg=invalid_msg,access_name=access_name,access_pass=access_pass)


@bp.route('/client_profile_management/<string:user_uid>', methods=['GET','POST'])
def client_profile_management(user_uid):
    print('user_uid',user_uid)
    if request.method == "GET":
        users = ClientInformation.query.filter_by(user_id=user_uid).one()
        if users is not None:
            if users.status == 'completed':
                session["user"] = users.username
                session["user_uid"] = users.user_id
                session["username"] = users.username
                session["email_id"] = users.email_id
                session["id"] = users.Id
                UID = users.user_id
                Username = users.username
                Email_Id = users.email_id
                OFIICE_NAME = users.office_name
                Address_1 = users.address_1
                Address_2 = users.address_2
                country = users.country
                state_code =users.state
                City_name = users.attributes_1
                Zip_Code = users.zipcode
                Phone_Number = users.mobile_number
                return render_template("client_profile_management.html", UID=UID, Username=Username,
                                       Email_Id=Email_Id, First_Name=OFIICE_NAME,
                                       Address_1=Address_1, Address_2=Address_2
                                       , country=country, state_code=state_code, City_name=City_name, Zip_Code=Zip_Code,
                                       Phone_Number=Phone_Number
                                       )
            else:
                session["user"] = users.username
                session["user_uid"] = users.user_id
                session["username"] = users.username
                session["email_id"] = users.email_id
                session["id"] = users.Id
                print('users.Id', users.Id)
                UID = users.user_id
                Username = users.username
                Email_Id = users.email_id
                OFIICE_NAME = ""
                Address_1 = ""
                Address_2 = ""
                country = "0"
                state_code = ""
                City_name = ""
                Zip_Code = ""
                Phone_Number = ""
                return render_template("client_profile_management.html", UID=UID, Username=Username,
                                       Email_Id=Email_Id, First_Name=OFIICE_NAME,
                                       Address_1=Address_1, Address_2=Address_2
                                       , country=country, state_code=state_code, City_name=City_name, Zip_Code=Zip_Code,
                                       Phone_Number=Phone_Number
                                       )


@bp.route('/client_registration', methods=['POST'])
def client_registration():
    if request.method == "POST":
        data = request.json
        print('data',data)
        if not(len(data['reg_username']) <=50):
            msg = "User name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not validate_gmail(data['reg_email']):
            msg = "Invalid Gmail"
            Status = {"status": msg}
            return jsonify(Status)

        header_id = datetime.now().strftime("%d%m%Y%H%M%S") + get_random_numbers(5)
        encrypted_pwd = Encryption().encrypt(data['reg_password'])
        head = UserCredentials(user_uid=header_id,
                       password = encrypted_pwd,
                       username = data['reg_username'],
                       email_id=data['reg_email'],
                       active = 'y',
                       status = 'pending')
        try:
            db.session.add(head)
            db.session.commit()
            db.session.close()
        except Exception as e:
            LOG.error(e, exc_info=True)
            db.session.rollback()
            LOG.error("Error while pushing data")
            msg = "Failed"
            Status = {"status": msg}
            return jsonify(Status)
        head2 = ClientInformation(user_id=header_id,
                       username=data['reg_username'],
                       email_id=data['reg_email'],
                       mobile_number="None",
                       office_name="None",
                       active='y',
                       status='pending',
                       zipcode="None",
                       address_1="None",
                       address_2="None",
                       state="None",
                       country="None")
        try:
            db.session.add(head2)
            db.session.commit()
            db.session.close()
            msg = "successfully registered"
            Status = {"status": msg}
            print('Status',Status)
            return jsonify(Status)
        except Exception as e:
            LOG.error(e, exc_info=True)
            db.session.rollback()
            msg = "Failed"
            Status = {"status": msg}
            print('Status', Status)
            return jsonify(Status)


@bp.route('/Update_client/<string:user_uid>', methods=['POST'])
def update_client(user_uid):
    if request.method == "POST":
        data = request.json
        First_Name = data["First_Name"]
        Address_1 = data["Address_1"]
        Address_2 = data["Address_2"]
        Zip_Code = data["Zip_Code"]
        City_name = data["City_name"]
        if not (len(First_Name) <= 50):
            msg = "First name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not (len(Address_1) <= 100):
            msg = "Address 1 name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not (len(Address_2) <= 100):
            msg = "Address 2 is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not (len(Zip_Code) <= 9):
            msg = "Zip name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        if not (len(City_name) <= 100):
            msg = "City name is too long"
            Status = {"status": msg}
            return jsonify(Status)
        users = ClientInformation.query.filter_by(user_id=user_uid).one()
        head = ClientInformation(Id=users.Id,
                       username = users.username,
                       mobile_number = data['Phone_Number'],
                       office_name = data['First_Name'],
                       active = 'y',
                       status = 'completed',
                       zipcode = data['Zip_Code'],
                       address_1 = data['Address_1'],
                       address_2 = data['Address_2'],
                       state = data['state_code'],
                       country =data['country'],
                       attributes_1=data['City_name'])
        try:
            db.session.merge(head)
            db.session.commit()
            db.session.close()
        except Exception as e:
            LOG.error(e, exc_info=True)
            db.session.rollback()
            LOG.error("Error while pushing data")
            msg = "Failed"
            Status = {"status": msg}
            return jsonify(Status)
        users = UserCredentials.query.filter_by(user_uid=user_uid).one()
        head1 = UserCredentials(Id=users.Id,
                               username=users.username,
                               active='y',
                               status='completed')
        try:
            db.session.merge(head1)
            db.session.commit()
            db.session.close()
            msg = "successfully registered"
            Status = {"status": msg}
            return jsonify(Status)
        except Exception as e:
            LOG.error(e, exc_info=True)
            db.session.rollback()
            LOG.error("Error while pushing data")
            msg = "Failed"
            Status = {"status": msg}
            return jsonify(Status)



@bp.route('/fuel_quote_history/<string:user_uid>', methods=['GET','POST'])
def fuel_quote_history(user_uid):
    if request.method == "GET":
        fq = FuelQuote.query.filter_by(user_id=user_uid).all()
        users = ClientInformation.query.filter_by(user_id=user_uid).one()
        main_table = []
        inner_loop = []
        first_username=users.office_name
        for Quote in fq:
            print(Quote)
            inner_loop.append(Quote.fuel_quote_id)
            inner_loop.append(Quote.fuel_type)
            inner_loop.append(Quote.cur_gallon_price)
            inner_loop.append(Quote.quantity)
            inner_loop.append(Quote.total_price)
            inner_loop.append(Quote.created_date)
            inner_loop.append(Quote.delivery_date)
            main_table.append(inner_loop)
            inner_loop = []
        count_row = len(main_table)
        return render_template("fuel_quote_history.html",UID=user_uid,main_table=main_table,count_row=count_row,first_username=first_username)

@bp.route('/fuel_quote_form/<string:user_uid>', methods=['GET','POST'])
def fuel_quote_form(user_uid):
    try:
        users = ClientInformation.query.filter_by(user_id=user_uid).one()
        id = users.user_id
        Office_Name = users.office_name
        delivery_address = users.address_1
        Country = users.country
        state = users.state
        zipcode = users.zipcode
        city = users.attributes_1
        email_id = users.email_id
        mobile_number = users.mobile_number
        if request.method == "GET":
            return render_template("fuel_quote_form.html",UID=id,id=id, Office_Name=Office_Name,
                                   delivery_address=delivery_address,
                                   Country=Country, state=state, zipcode=zipcode, city=city, email_id=email_id,
                                   mobile_number=mobile_number)
    except NoResultFound:
        pass
    except Exception as e:
        LOG.error("Error occurred while login ")
        LOG.error(e, exc_info=True)
    finally:
        db.session.close()
    if request.method == "POST":
        data = request.json
        fuel_quote_id = "BKID" + datetime.now().strftime("%d%m%Y%H%M%S") + get_random_numbers(2)
        head = FuelQuote(fuel_quote_id=fuel_quote_id,
                       user_id=id,
                       quantity=data['quantity_quote'],
                       cur_gallon_price=data['Gallon_price'],
                       total_price=data['Total_Amount_Due'],
                       state=state,
                       country=Country,
                       status='completed',
                       address=delivery_address,
                       phone_number=mobile_number,
                       fuel_type=data['fuel_type'],
                       cur_gst=data['cur_gst'],
                       delivery_date=data['bdate'])
        try:
            db.session.merge(head)
            db.session.commit()
            db.session.close()
            msg = "successfully Saved"
            Status = {"status": msg}
            return jsonify(Status)
        except Exception as e:
            LOG.error(e, exc_info=True)
            db.session.rollback()
            LOG.error("Error while pushing data")
            msg = "Failed"
            Status = {"status": msg}
            return jsonify(Status)


@bp.route('/logout', methods=['GET','POST'])
def logout():
    if request.method == "GET":
        invalid_msg = "hidden"
        access_name = "hidden"
        access_pass = "hidden"
        session.clear()
        gc.collect()
        session['user'] = False
        return render_template("login.html", invalid_msg=invalid_msg,access_name=access_name,access_pass=access_pass)
