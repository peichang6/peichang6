def avg(data):
    ppl_count = data["count"]
    employee = data["employees"]
    i = 0
    money = 0

    while i < ppl_count:
        money += employee[i]["salary"]
        i += 1
    print(money/ppl_count)


avg({
    "count": 3, "employees": [
        {
            "name": "John",
            "salary": 30000},
        {
            "name": "Bob",
            "salary": 60000},
        {
            "name": "Jenny",
            "salary": 50000}
    ]
})
