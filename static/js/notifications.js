function updateNotifications() {
    fetch('/notifications/') // URL to your notifications view
        .then(response => response.text())
        .then(data => {
            document.getElementById('notification-box').innerHTML = data;
        });
}

// Update notifications every 5 seconds (adjust as needed)
setInterval(updateNotifications, 5000);

// Initial update on page load
updateNotifications();