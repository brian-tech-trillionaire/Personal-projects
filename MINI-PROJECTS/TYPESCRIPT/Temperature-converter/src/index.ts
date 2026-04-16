const T: Float32Array = new Float32Array([parseFloat(prompt("Enter the temperature in Fahrenheit:") as string)]);

function convertTemperature(T:number): number {
  return T * 9/5 + 32;
}
let Fahrenheit: number = convertTemperature(T[0] ?? 0);
console.log(`Fahrenheit: ${Fahrenheit}F`)