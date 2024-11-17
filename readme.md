# 👉Output View
## Part1 Video
<img alt="Awesome GitHub Profile Readme" src="./p1.gif"> </img>
## Part2 Video
<img alt="Awesome GitHub Profile Readme" src="./p2.gif"> </img>

# Code Section
## Postman Test Script
```javascript
// Testing Status Code
pm.test("Status Code is 200.", () => {
    pm.response.to.have.status(200)
})
pm.test("Got Status Code from [200, 201].", () => {
    pm.expect(pm.response.code).to.be.oneOf([200, 201])
})
pm.test("Status code having OK string.", () => {
    pm.response.to.have.status("OK")
})
pm.test("Content-Type as header.", () => {
    pm.response.to.have.header("Content-Type")
})
pm.test("Is Content-Type == 'application/json'.", () => {
    pm.expect(pm.response.headers.get("Content-Type")).to.eql("application/json");
})

// Testing Response time
pm.test("Response time Below 3 ms.", () => {
    pm.expect(pm.response.responseTime).to.be.below(3)
})

// // Asserting value Types
// let jsonData = pm.response.json()
// pm.test("Is jsonData is Object.", () => {
//     pm.expect(jsonData).to.be.an("object")
// })
// pm.test("Is json id is number.", () => {
//     pm.expect(jsonData.id).to.be.a("number")
// })
// pm.test("Is json title is string.", () => {
//     pm.expect(jsonData.Title).to.be.a("string")
// })
// pm.test("Is json comments is List.", () => {
//     pm.expect(jsonData.Comments).to.be.an("array")
// })
```
