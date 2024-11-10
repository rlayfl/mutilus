function validateBeginForm() {

    $('#formErrorList').html("")

    var isValidated = true

    var uid = $('#uid').val();
    var password = $('#password').val();

    if (uid.length < 1) {
        $('#formErrorList').append('<li>Please include a .pickle file</li>')
        isValidated = false
    }

    if (password.length < 1) {
        $('#formErrorList').append('<li>Please include a .pickle file</li>')
        isValidated = false
    }

    alert(uid + " " + password)

    return isValidated
}