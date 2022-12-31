$("#id_city_living").change(function () {
    const url = $("#city_id").val();  // get the url of the `load_cities` view
    const cityId = $(this).val();  // get the selected country ID from the HTML input
    $.ajax({ // initialize an AJAX request
        url: url, // set the url of the request (= /members/ajax/load-cities/ )
        data: {
            'city_id': cityId  // GET parameters
        },
        success: function (data) {
            $("#id_district_living").html(data);
        },
        error: function (error){
            console.log(error)
        }
    });
});

$("#id_city_we").change(function () {
    const url = $("#city_id").val();  // get the url of the `load_cities` view
    const cityId = $(this).val();  // get the selected country ID from the HTML input
    $.ajax({ // initialize an AJAX request
        url: url, // set the url of the request (= /members/ajax/load-cities/ )
        data: {
            'city_id': cityId  // GET parameters
        },
        success: function (data) {
            $("#id_district_we").html(data);
        },
        error: function (error){
            console.log(error)
        }
    });
});

$("#id_city_education").change(function () {
    const url = $("#city_id").val();  // get the url of the `load_cities` view
    const cityId = $(this).val();  // get the selected country ID from the HTML input
    $.ajax({ // initialize an AJAX request
        url: url, // set the url of the request (= /members/ajax/load-cities/ )
        data: {
            'city_id': cityId  // GET parameters
        },
        success: function (data) {
            $("#id_district_education").html(data);
        },
        error: function (error){
            console.log(error)
        }
    });
});
