let elapsedTime;

function trackTime() {
    elapsedTime = parseInt($('#time-elapsed').text()) || 0;
    $('#time-elapsed').text(elapsedTime + 10); // Increase by 10 milliseconds

    setTimeout(trackTime, 10); // Update every 10 milliseconds
}

$(document).ready(function () {
    trackTime();
});
