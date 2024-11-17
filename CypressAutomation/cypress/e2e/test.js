let lst = ["first", "second"]
let str = ""
for (let i = 0; i < lst.length; i ++){
    str = lst.at(i) + i.toString()
    console.log(lst.at(i), typeof lst.at(i) == "string")
    console.log(str)
}