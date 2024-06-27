const apiKey = "f00c38e0279b7bc85480c3fe775d518c";
const city = "London";
const url =
`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;
async function fetchWeatherData() {
try {
const response = await fetch(url);
const data = await response.json();
const tempK = data.main.temp; // Temperature in Kelvin
const tempC = tempK - 273.15; // Convert to Celsius
const ctx = document.getElementById("weatherchart").
getContext("2d");
const weatherChart = new Chart(ctx, {
type: "bar",
data: {
labels: ["Temperature"],
datasets: [{
label: `Temperature in ${city} (°C)`,
data: [tempC],
backgroundColor: "rgba(75, 192, 192, 0.6)",
borderColor: "rgba(75, 192, 192, 1)",
borderWidth: 1
}]
},
options: {
scales: {
yAxes: [{
ticks: {
beginAtZero: true
}
}]
}
}
});
} catch (error) {
console.error("Error fetching weather data:", error);
}
}
// Call the function to fetch the weather data
fetchWeatherData();