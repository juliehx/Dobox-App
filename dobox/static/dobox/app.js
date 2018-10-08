function get_transaction(name, cost, type) {
    const settings = {
        type: 'GET',
        url: "/dobox/ajax/add_transaction/",
        data: {
            'transaction_name': name,
            'amount': cost,
            'type': type
        },
        datatype: 'json',
        success: function(data) {
            console.log(data);
            data_display = "<li>" + data["transaction"] + " | ";
            if (data["type"] === "spendings") {
                data_display += "-$" + data["amount"] + "</li>";
            }
            else {
                data_display += "+$" + data["amount"] + "</li>";
            }
            $(".transactions").append(data_display);
        }
    };
    $.ajax(settings);
};

$(".trans-form").on("submit", function(event) {
    event.preventDefault();
    var name = $(this).find("#id_transaction_name").val();
    var cost = $(this).find("#id_amount").val();
    var type = $(this).find('#trans-type').val();
    $(this).find("#id_transaction_name").val('');
    $(this).find("#id_amount").val('');
    get_transaction(name, cost, type);
});