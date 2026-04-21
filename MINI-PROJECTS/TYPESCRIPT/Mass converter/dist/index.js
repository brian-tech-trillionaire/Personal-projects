"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function massConverter(Unit, from, to) {
    if (from === "kg" && to === "g") {
        return `${Unit * 1000} ${to}`;
    }
    else if (from === "g" && to === "kg") {
        return `${Unit / 1000} ${to}`;
    }
    else {
        return "Invalid unit conversion.";
    }
}
console.log(massConverter(2, "kg", "g")); // Output: "2000 g"
console.log(massConverter(500, "g", "kg")); // Output: "0.5 kg"
console.log(massConverter(1, "kg", "lb")); // Output: "Invalid unit conversion."
//# sourceMappingURL=index.js.map