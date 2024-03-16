document.getElementById("userForm").addEventListener("submit", function(event) {
    const emailInput = document.getElementById("email");
    const ageInput = document.getElementById("age");
    const errorDiv = document.getElementById("error");
    let isValid = true;

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailInput.value)) {
        errorDiv.textContent = "Invalid email format";
        isValid = false;
    }

    // Validate age
    if (ageInput.value <= 0) {
        errorDiv.textContent = "Age must be a positive integer";
        isValid = false;
    }

    if (!isValid) {
        event.preventDefault(); // Prevent form submission
    }
});
