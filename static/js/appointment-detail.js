var status = $("#status").html()
if($("#status").html() === "IN PROGRESS")
{
    $("#status").css("background-color", "#F2EA21");
}
else if($("#status").html() === "ACCEPTED")
{
    $("#status").css("background-color", "#65DE3A");
}
else if($("#status").html() === "REJECTED")
{
    $(".m-grid-info__item--cancel").hide()
    $("#status").css("background-color", "#F45656");
}
else if($("#status").html() === "CANCELED")
{
    $(".m-grid-info__item--cancel").hide()
    $(".m-grid-info").css({
        "background-color":"#F1F2F2",
        "color":"#237d9e",
        "border-left":"14px solid #237d9e"})
    $(".m-grid-info").html("You cancelled your appointment")
    $("#status").css("background-color", "#F45656");
}