describe('Tests', () => {
    it('1. Login', () => {
        cy.visit("https://www.reddit.com/").screenshot('reddit')
        cy.get("#login-button").click()
        cy.xpath("(//div[contains(text(), 'Continue as Routh')])[1]").click()
    });
});
// npx cypress run --spec ./cypress/e2e/01Login.cy.js

/*In cypress.config.js

const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    video: true
  },
});

*/