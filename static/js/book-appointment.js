$(document).ready(function() {
    var curr = new Date();
    $.validator.addMethod("past_date_validator", function(value,element) {
        var date = value;

        var d = new  Date(parseInt(date.substring(0,4)),parseInt(date.substring(5,7)-1),parseInt(date.substring(8,10)));
        if(d < curr)
        {
            return true;
        } 
        else{
            return false;
        }
      }, "Date of Birth cannot be future date");
      $.validator.addMethod("future_date_validator", function(value,element) {
        var date = value;
        var curr = new Date();
        var d = new  Date(parseInt(date.substring(0,4)),parseInt(date.substring(5,7)-1),parseInt(date.substring(8,10)));
        if(d > curr || (d.getFullYear() === curr.getFullYear() && d.getMonth() === curr.getMonth() && d.getDay() === curr.getDay() )) 
        {
            return true;
        } 
        else{
            return false;
        }
      }, "Please add future date");
      $.validator.addMethod("check_time", function(value,element) {
        var time = value;
        if(time.substring(0,2) > curr.getHours())
            return true;
        else
            return false;
      }, "Please add future date");
    $(".m-form").validate({
    errorClass: "error fail-alert",
    rules: {
    name : {
    required: true,
    minlength: 3
    },
    email: {
    required: true,
    email: true
    },
    dob:{
        past_date_validator:true
    },
    date_of_appointment:{
        future_date_validator:true
    },
    time_slot:{
        required:{
        depends: function(elem) {
            return $("#id_date_of_appointment").val() === curr;
            }
        },
        check_time:true

    }
},
    messages : {
        name: {
        minlength: "Name should be at least 3 characters",
        },
        email: {
        email: "The email should be in the format: abc@domain.com",
        },
        dob:{
        past_date_validator:"Date of birth cannot be a future date"
        },
        date_of_appointment:{
        future_date_validator:"Please add future date"
        },
        time_slot:{
            check_time:"please select future time-slot"
        }
        }
    });
    });