$("#id_abilities").change(function () {
    const url = $("#ability_id").val();  // get the url of the `load_cities` view
    const ability_id = $(this).val();  // get the selected country ID from the HTML input
    $.ajax({ // initialize an AJAX request
        url: url, // set the url of the request (= /members/ajax/load-cities/ )
        type: "POST",
        data: {
            'ability_id': ability_id  // GET parameters
        },
        success: function (data) {
            $("#ability_levels_id").html(data);
        },
        error: function (error){
            console.log(error)
        }
    });
});