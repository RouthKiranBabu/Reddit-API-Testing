class Loginpage{
    mkLogin(url, clicklogin, continuexpath, screenShotName = 'reddit'){
        cy.visit(url).screenshot(screenShotName)
        cy.get(clicklogin).click()
        cy.xpath(continuexpath).click()
    }
}
export default Loginpage;