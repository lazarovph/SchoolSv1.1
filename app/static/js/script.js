<!-- static/js/script.js -->
document.addEventListener('DOMContentLoaded', function() {
    let flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = 0;
        }, 3000);  // Скриваме съобщението след 3 секунди
    });
});
