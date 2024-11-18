import Loginpage from "../PageObjects/Login.js";
import Searchpage from "../PageObjects/Search.js"

describe('Contains all the tests.', () => {
    it('1. Login✅', () => {
        let lg = new Loginpage()
        cy.fixture('Userdata').then((data) => {
            lg.mkLogin(data.url, data.clicklogin, data.continuexpath, data.screenShotName)
        })
    });
    it('2. Search✅', () => {
        let sg = new Searchpage()
        cy.fixture('Userdata').then((data) => {
            sg.Search(data.search)
        })
    })
});

// In cypress.config.js
// const { defineConfig } = require("cypress");
// module.exports = defineConfig({
//   e2e: {
//     setupNodeEvents(on, config) {
//       // implement node event listeners here
//     },
//     video: true
//   },
// });

// relative path👉 Cypress\cypress\e2e\Main.cy.js
// 👇Command to get screenShot and Video When Something is Wrong
// npx cypress run --spec ./cypress/e2e/Main.cy.js