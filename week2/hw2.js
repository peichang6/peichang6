function avg(data) {
  let number = data.count
  let employees = data.employees
  let sum = 0
  for (i = 0; i < number; i++) {
    sum += employees[i].salary;
  }
  let ans = sum / number
  console.log(ans)
  return (ans)
}
avg({
  "count": 3,
  "employees": [
    {
      "name": "John",
      "salary": 30000
    },
    {
      "name": "Bob",
      "salary": 60000
    },
    {
      "name": "Jenny",
      "salary": 50000
    }
  ]
})


