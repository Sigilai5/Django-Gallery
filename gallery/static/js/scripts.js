$(document).ready(function () {
    $(".bton").click(function () {
        var text = $(".text").val();
        text.select()
        document.execCommand("copy");
        alert("has been succesfully Copied.");
    });

});