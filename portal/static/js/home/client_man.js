var GTR_={}
function save_details() {
    var UID= document.getElementById("UID").innerHTML
    let List_=["First_Name" ,"Address_1","City_name","Zip_Code","Phone_Number"];

    for (let i = 0; i < List_.length; i++)
    {
     if(document.getElementById(List_[i]).value == "")
     {
         document.getElementById("lb_"+List_[i]).className = '';
         return false;
      }
      else
      {
           if (List_[i]==="Zip_Code")
           {
               if (document.getElementById(List_[i]).value.length>=5 && document.getElementById(List_[i]).value.length<=9)
               {
                  document.getElementById("lb_"+List_[i]).className = 'required_';
                  GTR_[List_[i]]=document.getElementById(List_[i]).value
               }
               else
               {
                  document.getElementById("lb_"+List_[i]).className = '';
                  document.getElementById("lb_"+List_[i]).innerHTML="Zipcode Should be greater then 5 and less then 9"
                  return false;
               }
           }
           if (List_[i]==="Phone_Number")
           {
               if (document.getElementById(List_[i]).value.length==10)
               {
                  document.getElementById("lb_"+List_[i]).className = 'required_';
                  GTR_[List_[i]]=document.getElementById(List_[i]).value
               }
               else
               {
                  document.getElementById("lb_"+List_[i]).className = '';
                  document.getElementById("lb_"+List_[i]).innerHTML="Enter 10 Digits"
                  return false;
               }
           }
           else
           {
            document.getElementById("lb_"+List_[i]).className = 'required_';
            GTR_[List_[i]]=document.getElementById(List_[i]).value
           }

      }
    }
    if(document.getElementById("country").value=="select country"){
       document.getElementById("lb_country").className = '';
         return false;
    }
    else{
        GTR_['country']=document.getElementById("country").value
    }
    if(document.getElementById("state-code").value==""){
       document.getElementById("lb_state-code").className = '';
         return false;
    }
    else{
    GTR_['state_code']=document.getElementById("state-code").value
    }
    GTR_['Address_2']=document.getElementById("Address_2").value
    $.ajax({
            url: '/fuel_quote/Update_client/'+UID,
            data: JSON.stringify(GTR_),
            type: 'POST',
            contentType: "application/json",
            dataType: 'json',
            success: function (data1)
            {
                GTR_={}
                let List_=['First name is too long','Address 1 name is too long','Address 2 is too long','Zip name is too long','City name is too long']
                let d2_get=["First_Name" ,"Address_1","Address_2","Zip_Code","City_name"];
                try
                {
                    for (let i = 0; i < List_.length; i++)
                    {
                        if(data1['status'].toLowerCase() == List_[i].toLowerCase())
                         {
                             document.getElementById("lb_"+d2_get[i]).className = '';
                             document.getElementById("lb_"+d2_get[i]).innerHTML = List_[i];
                             return false;
                         }
                         else
                          {
                            document.getElementById("lb_"+d2_get[i]).className = 'required_';
                          }
                    }
                  }
                catch(err) {
                console.log('Error')
                alert('Something Went Wrong')
                }


                if(data1['status']=="successfully registered")
                {
                   GTR_={}
                   window.location.href = "/fuel_quote/fuel_quote_history/"+UID
                }
                else{
                    GTR_={}
                    return false;
                }

            },
            error: function(data1)
            {
                console.log(data1);
                GTR_={}
                return false;
            }
    });
}

function myFunction(item) {
    if(document.getElementById(item).value == ""){
     alert("Please enter "+item)
     return false
  }
  else{
  GTR_[item]=document.getElementById(item).value
  }
}



function order_fuel(){
  var UID = document.getElementById("user_id").value
  var fuel_type = document.getElementById("fuel_type").value
  var quantity_quote = document.getElementById("quantity_quote").value
  var Gallon_price=document.getElementById("Gallon_price").innerHTML
  var Total_Amount_Due=document.getElementById("Total_Amount_Due").innerHTML
  var bdate=document.getElementById("bdate").value
  var cur_gst="14%"
  if(quantity_quote == ""){
    document.getElementById("lb_quantity_quote").className = '';
    return false;
  }
  else
  {
   document.getElementById("lb_quantity_quote").className = 'required_';
  }
  if(fuel_type == "None"){
    document.getElementById("lb_fuel_type").className = '';
    return false;
  }
  else{
    document.getElementById("lb_fuel_type").className = 'required_';
  }
  if(bdate == ""){
    document.getElementById("lb_bdate").className = '';
    return false;
  }
  else{
    document.getElementById("lb_bdate").className = 'required_';
  }
     let details_={"fuel_type":fuel_type,"quantity_quote":quantity_quote,"Gallon_price":Gallon_price,"Total_Amount_Due":Total_Amount_Due,"bdate":bdate,"cur_gst":cur_gst}
     $.ajax({
            url: '/fuel_quote/fuel_quote_form/'+UID,
            data: JSON.stringify(details_),
            type: 'POST',
            contentType: "application/json",
            dataType: 'json',
            success: function (data2)
            {
                if(data2['status']=="successfully Saved")
                {
                   window.location.href = "/fuel_quote/fuel_quote_history/"+UID
                }
                else{
                    alert(data2['status'])
                    return false;
                }

            },
            error: function(data2)
            {
                console.log(data2);
                return false;
            }
    });
}