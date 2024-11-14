describe('Tests', () => {
    it('1. Login', () => {
        cy.visit("https://www.reddit.com/")
        cy.get("#login-button").click()
        cy.xpath("(//div[contains(text(), 'Continue as Routh')])[1]").click()
    });
});