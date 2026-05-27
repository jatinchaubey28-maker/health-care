// Get today's date in YYYY-MM-DD format
const today = new Date().toISOString().split('T')[0];
// Set the 'min' attribute of the input to today
document.getElementById('date').setAttribute('min', today);

// restricting past time
const form = document.querySelector('form'); // Or use an ID
form.addEventListener('submit', function(e) {
    const selectedDate = document.getElementById('date').value;
    const selectedTime = document.querySelector('input[type="time"]').value;
    
    const now = new Date();
    const currentDateTime = new Date(selectedDate + 'T' + selectedTime);

    if (currentDateTime < now) {
        e.preventDefault(); // Stop the form from submitting
        alert("You cannot book an appointment in the past! Please choose a future time.");
    }
});

// Managing restriction on inactive hours
const dateInput = document.getElementById('date');
const timeInput = document.getElementById('time');

dateInput.addEventListener('change', function() {
    const date = new Date(this.value);
    const day = date.getUTCDay(); // 0 = Sunday, 1 = Monday... 6 = Saturday

    // Define your rules based on your "Working Hours" card
    if (day === 1 || day === 2 || day === 3) { // Monday, Tuesday, Wednesday
        timeInput.min = "8:00";
        timeInput.max = "17:00";
    } else if (day === 4 || day === 5) { // Thursday, Friday
        timeInput.min = "09:00";
        timeInput.max = "17:00";
    } else { // Weekdays (saturday and sunday)
        timeInput.min = "10:00";
        timeInput.max = "17:00";
    }

    // Optional: Clear the time if they change the date to avoid "illegal" old values
    timeInput.value = "";
});