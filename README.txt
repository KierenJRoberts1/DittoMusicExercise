How to Run -

Run pytest in the terminal. The pytest.ini file provides the default configuration, running the tests headlessly while retaining traces and screenshots on failure.

Assumptions -

Browser Scope: Set to Chromium (Chrome); as the most common browser, this gives us the highest coverage for a short exercise.

Test Data: No test data was provided, which was expected. I used the Faker library to generate dynamic, but valid, data for the happy path. 
Invalid data was hardcoded and deterministic, ensuring we get the exact same results on each iteration of the negative tests.

Environment: Assumed to be the production environment https://dittomusic.com/en/login as provided.

Test Completion: Upon triggering the CAPTCHA, the sign-up flow is considered successfully validated. 
This was confirmed via manual testing (creating a personal account) and follows the exercise documentation.

Approach, Trade-offs, & Future Improvements -

Approach: The goal was to create a lightweight framework that demonstrates core functionality quickly and effectively. 
While these tests could be highly complex, a clean sanity run covering the core requirements was best due to time constraints.

Trade-off (Error Messages): Currently, we assert that the invalid email/password message is visible, but we are assuming the text currently in production is correct. 
Without a Product Owner to provide the exact intended copy, we are validating the message against itself.

Trade-off (Pseudo-elements): The invalid email/password messages are rendered using CSS pseudo-elements (::before, ::after). For this exercise, visibility and structural presence were checked. 
In the future, JavaScript execution can be added to read and strictly validate the exact text content inside these pseudo-elements.

Improvement (Event Firing): A future addition would intercept network requests to ensure that clicking the Call to Action (CTA) with invalid data does not fire a backend API or analytics event.

Improvement (Visual Debugging): Adding visual highlighting for locators right before they are clicked or asserted to make trace-viewing and debugging easier.

Improvement (External Links): Adding checks to ensure the Terms & Conditions link successfully opens the correct URL in a new tab with the expected content.

Improvement (CAPTCHA Bypass): Understanding how Ditto Music handles automated sign-ups internally. 
I assume the pipeline wouldn't stop at the CAPTCHA in a real CI/CD environment, and there would be a testing API or token used to bypass it.

Improvement (Checkbox States): Expanding the test suite to sign up with the marketing checkbox ticked vs. unticked, and verifying the CTA is disabled or blocks submission entirely if the Terms checkbox is left unchecked.