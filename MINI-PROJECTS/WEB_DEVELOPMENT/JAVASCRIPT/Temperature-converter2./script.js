T = parseFloat(prompt("Enter the temperature in Celsius: "));

function Fahreinheit(F) {
  return T * 9/5 + 32;
}

if (T === "") {
  alert("Please re-enter the temperature");
} else { 
  alert(`Temperature in Fahreinheit: ${Fahreinheit(T)}`);
}