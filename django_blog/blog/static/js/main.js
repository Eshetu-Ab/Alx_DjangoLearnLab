// Example: Basic form validation
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const email = document.querySelector('input[name="email"]');
        if (!email.value) {
            alert('Email field cannot be empty!');
            event.preventDefault();
        }
    });
});
