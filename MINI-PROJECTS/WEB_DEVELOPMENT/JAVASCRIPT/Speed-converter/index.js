function speedConverter(speed, from, to) {
  if (from === 'm/s' && to === 'km/h') {
    return `${speed*18/5} ${to}`;
  } else {
    return  `${speed*5/18} ${to}`
  }
}

console.log(speedConverter(10, 'm/s', 'km/h')); // 36 km/h
console.log(speedConverter(36, 'km/h', 'm/s')); // 10 m/s