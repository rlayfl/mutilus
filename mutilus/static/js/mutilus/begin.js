$(function() {
    populateUniqueIdentifierWithRandomString();
});


function validateBeginForm() {

    $('#formErrorList').html("")

    var isValidated = true

    var uid = $('#uid').val();
    var password = $('#password').val();

    if (uid.length < 1) {
        $('#formErrorList').append('<li>Please choose a unique identifier</li>')
        isValidated = false
    }

    if (password.length < 1) {
        $('#formErrorList').append('<li>Please choose a password</li>')
        isValidated = false
    }

    alert(uid + " " + password)

    storeExperimentAtFirebase(uid, password)

    // Change this
    return false;
}

function storeExperimentAtFirebase(uid, password) {

    var formData = new FormData()
    formData.append('uid', uid)
    formData.append('password', password)

    $.ajax(
        {
            url: "/upload_experiment_data_to_firebase/",
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {

                alert("Experiment Created")

                window.location.replace("/experiment/?experiment="+response.uid)

                // $('#loading-animation-container').addClass("d-none")
                // $('#form').removeClass("d-none")

                // worstCaseGameStates = response['finalResult']['worst_case']['game_state:']

                // worstCaseGameStates.forEach(appendGameStatesToResultsView)
            },
            error: function(error) {

                //$('#loading-animation-container').addClass("d-none")
                //$('#form').removeClass("d-none")
            }
        }
    )
}

function populateUniqueIdentifierWithRandomString() {
    
    $('#uid').val(makeRandomString(15))
}

// Function based on code available here:
// https://stackoverflow.com/questions/1349404/generate-random-string-characters-in-javascript
function makeRandomString(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
}