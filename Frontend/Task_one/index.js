// Function to get current time in UTC and current day of the week
function updateTimeAndDay() {
  const now = new Date();
  
  // Get current time in UTC
  const hours = now.getUTCHours().toString().padStart(2, '0');
  const minutes = now.getUTCMinutes().toString().padStart(2, '0');
  const seconds = now.getUTCSeconds().toString().padStart(2, '0');
  const currentTimeUTC = `${hours}:${minutes}:${seconds}`;
  
  // Get current day of the week
  const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  const currentDay = daysOfWeek[now.getUTCDay()];
  
  // Display the current time and day in the specified format
  document.querySelector('[data-testid="currentTimeUTC"]').textContent = `Time is ${currentTimeUTC}`;
  document.querySelector('[data-testid="currentDay"]').textContent = `Today is ${currentDay}`;
}

updateTimeAndDay();
setInterval(updateTimeAndDay, 1000);
