$(document).ready(function() {
    var curr = new Date();
    $.validator.addMethod("past_date_validator", function(value,element) {
        var dob = $("#id_dob").val();
        curr = moment(curr).format('YYYY-MM-DD');
        if(dob < curr)
        {
            return true;
        } 
        else{
            return false;
        }
      }, "Date of Birth cannot be future date");
      $.validator.addMethod("future_date_validator", function(value,element) {
        var doa = $("#id_date_of_appointment").val();
        curr = moment(curr).format("YYYY-MM-DD");
        if(doa > curr || doa === curr)
        {
            return true;
        } 
        else{
            return false;
        }
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
        }
        }
    });
    });

