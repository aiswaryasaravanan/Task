let input = [
    {
        "id": 1,
        "first_name": "Jeffree",
        "last_name": "Lee",
        "occupation": "Engineer",
        "age": 56
    },
    {
        "id": 2,
        "first_name": "Jeffin",
        "last_name": "James",
        "occupation": "Network Engineer",
        "age":36
    },
    {
        "id": 3,
        "first_name": "John",
        "last_name": "Cena",
        "occupation": "Wrestler",
        "age": 51
    },
    {
        "id": 4,
        "first_name": "Swathy",
        "last_name": "Nahr",
        "occupation": "Professor",
        "age": 28
    }
]

for(let i=0; i<input.length; i++){
    input[i]["name"] = input[i]["first_name"] + " " + input[i]["last_name"]
    delete input[i]["first_name"]
    delete input[i]["last_name"]
}
console.log(input)