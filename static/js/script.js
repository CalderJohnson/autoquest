var slider = document.getElementById("price");
var output = document.getElementById("demo");
output.innerHTML = price.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}

var slider1 = document.getElementById("seats");
var output1 = document.getElementById("demo1");
output.innerHTML = price.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider1.oninput = function() {
  output1.innerHTML = this.value;
}