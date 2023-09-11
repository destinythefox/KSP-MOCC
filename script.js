document.addEventListener("DOMContentLoaded", function() {
    // Code here will run after the entire page is loaded

    // Your existing logic

    // Initialize alerts
    checkForAlerts();
});

function checkForAlerts() {
    // Your conditions for triggering alerts go here

    // Example condition for Low Fuel Levels
    let lowFuel = false; // Replace with real logic
    if (lowFuel) {
        triggerAlert("Low Fuel Levels", "warning");
    }

    // Example condition for Critical Battery Levels
    let criticalBattery = false; // Replace with real logic
    if (criticalBattery) {
        triggerAlert("Critical Battery Levels", "danger");
    }

    // Add more conditions as needed
}

function triggerAlert(message, alertType) {
    const alertBox = document.getElementById("alertBox");

    let alertClass = "";
    switch(alertType) {
        case "success":
            alertClass = "bg-success";
            break;
        case "warning":
            alertClass = "bg-warning";
            break;
        case "danger":
            alertClass = "bg-danger";
            break;
        default:
            alertClass = "bg-success";
    }

    alertBox.className = alertClass + " text-center";
    alertBox.textContent = message;
}
