describe('2. Search feature', () => {
    it('Search google and get first 10 Posts', () => {
        let search = ["google", "chatgpt"]
        let string = ""
        let screenshotName = ""
        for(let i = 0; i < search.length; i ++){
            string = "https://www.reddit.com/r/" + search.at(i)
            screenshotName = search.at(i) + i.toString()
            // cy.log(string, screenshotName)
            cy.visit(string).screenshot(screenshotName)
            cy.wait(6000)
            cy.scrollTo('0%', '50%')
        }
    });
});