# 👉 Output View
<img alt="Awesome GitHub Profile Readme" src="./day_1.gif"> </img>

# Questions
<details>
<summary>Click to Open</summary>

| Question Number | Questions | Answers |
|-----:|-----------|------------|
|     `1`| `What is the scope of the project? Why did you choose the same?` | `To reduce the human effort while testing the website again and again in the future days.` |
|     2| Can you walk me through the most challenging technical problem you encountered in your project and how you resolved it? | Yes, I have encountered a technical problem regarding understanding about the project So Team member given a some questions to answer. This given me a vision to approach project. |
|     `3`| `What specific technologies did you use, and why did you choose them for this project?` | `Cypress for automation.` |

</details>

# Table of Content
  - Cypress
      - Defination
      - Features
      - Advantages and Disadvantages

# Cypress
For more information 👉 [documentation](https://docs.cypress.io/app/get-started/why-cypress).
## Defination
- Cypress is a open Source, Java-script based testing Framework, and used for end to end testing of web application.
- Cypress directly operates in the browser, it also allows network request.
- `According to Documentation`
    - Cypress is a next generation front end testing tool built for the modern web. We address the key pain points teams face when testing modern applications and maintaining test suites.
    - Our users are typically developers, QA engineers, and teams looking to build web applications and increase the quality of their existing applications.
## Features
  - `Time Travel`: Cypress takes snapshots as your tests run. Hover over commands in the Command Log to see exactly what happened at each step.
  - `Debuggability`: Stop guessing why your tests are failing. Debug directly from familiar tools like Developer Tools. Our readable errors and stack traces make debugging lightning fast.
  - `Automatic Waiting`: Never add waits or sleeps to your tests. Cypress automatically waits for commands and assertions before moving on. No more async hell.
  - `Spies, Stubs, and Clocks`: Verify and control the behavior of functions, server responses, or timers. The same functionality you love from unit testing is right at your fingertips.
  - `Network Traffic Control`: Easily control, stub, and test edge cases without involving your server. You can stub network traffic however you like.
  - `Consistent Results`: Our architecture doesn't use Selenium or WebDriver. Say hello to fast, consistent and reliable tests that are flake-free.
  - `Cross Browser Testing`: Run tests within Firefox and Chrome-family browsers (including Edge and Electron) locally and in a Continuous Integration pipeline.
## Advantages and Disadvantages
| Feature | Advantages | Disadvantages |
| :----: | :----- | ------: |
| Real-time Reloads | Provides instant feedback by re-running tests on code changes, improving development efficiency. | Can increase CPU usage, which may slow down the development environment in large projects. |
| Automatic Waiting | Reduces need for manually setting wait times, making tests faster and more reliable. | Limited control over fine-grained waits; may fail in some cases where customized waits are required. |
| Time-travel Debugging | Allows users to view each test step with snapshots, simplifying troubleshooting and debugging. | Debugging features are browser-based, so they may not work as smoothly with headless or CI environments. |
| Network Request Control | Enables manipulation of HTTP requests and responses, useful for testing various scenarios easily. | Limited to JavaScript-based applications; does not support cross-origin requests as freely as Selenium. |
| Integrated Test Runner | Runs tests in a real browser environment, giving a realistic end-user perspective. | Only supports Chrome-family and Firefox browsers for now, limiting cross-browser compatibility. |
| Built-in Assertions | Comes with built-in assertions, simplifying the test-writing process and making it more readable. | Limited flexibility with built-in assertions; complex assertions may require additional libraries. |
| Active Community and Support | Large, active community with many tutorials and resources, making it easier to learn and troubleshoot. | Limited support for mobile and multi-tab testing, which can restrict testing scope in some projects. |

# Code
```JavaScript
describe('Tests', () => {
    it('1. Login', () => {
        cy.visit("https://www.reddit.com/").screenshot('reddit')
        cy.get("#login-button").click()
        cy.xpath("(//div[contains(text(), 'Continue as Routh')])[1]").click()
    });
});
```
## ScreenShot ⬅️
<img alt="Awesome GitHub Profile Readme" src="./day_1.gif"> </img>
