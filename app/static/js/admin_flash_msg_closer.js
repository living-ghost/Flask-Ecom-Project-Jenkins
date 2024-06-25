// Find the close button element
var closeButton = document.querySelector('#flash-message .close');

// Add a click event listener to hide the flash message
if (closeButton) {
    closeButton.addEventListener('click', function() {
        var flashMessage = document.querySelector('#flash-message');
        if (flashMessage) {
            flashMessage.style.display = 'none'; // Hide the flash message
        }
    });
}