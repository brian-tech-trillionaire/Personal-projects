"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const T = new Float32Array([parseFloat(prompt("Enter the temperature in Fahrenheit:"))]);
function convertTemperature(T) {
    return T * 9 / 5 + 32;
}
let Fahrenheit = convertTemperature(T[0] ?? 0);
console.log(`Fahrenheit: ${Fahrenheit}F`);
//# sourceMappingURL=index.js.map