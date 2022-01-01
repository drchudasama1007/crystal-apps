odoo.define("crystal_reservation.custom", function (require) {
    "use strict";
    var rpc = require('web.rpc');

    $('.dome_img').click(function () {
        console.log("=========click======1======")
        $('#reservation_date').val('')
        $('#time_slot').val('')
    })

    $('#reservation_date').change(function () {
        console.log("=========click=====2=======")
        $('#time_slot').val('')
    })


    $('#time_slot').click(function () {
        var reservation_date = $('#reservation_date').val()
        var time_slot = $('#time_slot').val()
        var imgbackground = $('input[name="imgbackground"]:checked').val();
        if(!reservation_date){
            $('#time_slot').val('')
            alert("Please Select Date...!")
        }
        if(reservation_date && time_slot && imgbackground){
            rpc.query({route: '/check/slot',
                params:{
                    reservation_date:reservation_date,
                    time_slot:time_slot,
                    imgbackground:imgbackground,
                }
            }).then(function (result) {
                if(result){
                    console.log("===========OK=======",result)
                }
                else{
                    $('#time_slot').val('')
                    alert("Sorry...This Slot Is Already Booked !")
                }
            })
        }
    })



})