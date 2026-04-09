T = parseFloat(prompt("Enter the temperature in Celsius: "));

function Fahreinheit(F) {
  var F = T * 9/5 + 32;
  return F;
}

if (T === "") {
  alert("Please re-enter the temperature");
} else { 
  alert(`Temperature in Fahreinheit: ${Fahreinheit(T)}`);
}