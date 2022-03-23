
window.setTimeout(function () {
    $(".AMessage").fadeOut('slow')
}, 2000);

function set_message_count(notificationCount) {
    $('#message_count').text(notificationCount);
    $('#message_count').css('visibility', notificationCount ? 'visible' : 'hidden');
}

$(function () {
    var since = 0;
    setInterval(function () {
        $.ajax(`${window.notification_url}?since=` + since).done(
            function (notifications) {
                for (var i = 0; i < notifications.length; i++) {
                    if (notifications[i].name == 'unread_message_count')
                        set_message_count(notifications[i].data);
                    since = notifications[i].timestamp;
                }
            }
        );
    }, 5000);
});

function countCharacters(e) {
    var textEntered, countRemaining, counter;
    textEntered = document.getElementById('tweet').value;
    counter = (300 - (textEntered.length)) + '/' + 300;
    countRemaining = document.getElementById('charactersRemaining');
    countRemaining.textContent = counter;
}
el = document.getElementById('tweet');
el.addEventListener('keyup', countCharacters, false);