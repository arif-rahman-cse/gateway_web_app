function getTemperatureColor(temp) {
    // Define a temperature range (e.g., -10°C to 40°C)
    const minTemp = -10;
    const maxTemp = 40;

    // Normalize the temperature value to a 0-1 range
    const normalizedTemp = (temp - minTemp) / (maxTemp - minTemp);

    // Use a gradient from blue to red
    const red = Math.min(255, Math.max(0, Math.round(255 * normalizedTemp)));
    const blue = 255 - red;

    return `rgb(${red}, 0, ${blue})`;
}

function setTemperature(temp) {
    const rectangle = document.getElementById('rectangle');
    const color = getTemperatureColor(temp);
    rectangle.style.backgroundColor = color;
}

// Example usage:
setTemperature(25); // Set temperature to 25°C
