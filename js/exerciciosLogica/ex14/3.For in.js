const user = {
    name: "Rodolfo",
    age: 33,
    city: "São Paulo"
}

for (let keys in user) {
    console.log(`${keys}: ${user[keys]}`)
}