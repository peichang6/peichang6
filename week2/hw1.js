function calculate(min, max) {
  let sum = 0
  for (i = min; i <= max; i++) {
    sum += i
  }
  console.log(sum)
  return sum
}

calculate(1, 3)
calculate(4, 8)
