How to run:

Run pytest in the terminal, pytest.ini is providing the headless aspect with retaining traces and screenshots on failure

Assumptions:

Browser scope was set to Chrome; the most common browser, therefore, for such a small test exercise gives us the biggest audience.

Test data was not provided, which was expected. Use of faker for fake dynamic data, but notably valid data. 
Invalid data was hardcoded and deterministic, we should expect the same results on each iteration with the invalid data.

Environemnt was provided as production, dittomusic.com/en/login

Upon completion of captcha sign-up would have been completed, confirmed with manual testing (my personal account sign-up)
and from the exercise document itself.

Approach/Trade-offs/Improvements/Additions:

The approach was to create a quick framework which demonstrates basic functionality, i.e. invalid email address, etc in
the quickest way. These tests could be more complex, however, for this exercise, a quick sanity run over the requirements
was the best due to time constraints.

However, the trade-offs of the above are that we only know that the invalid email/password message is visible but not what it should be
another assumption would need to be made, what is in production is correct then validate that message against itself. This
would provide a test that would pass regardless of if the message was correct; can't ask a PO.

Validating that upon invalid email or password upon CTA didn't fire an event, again complexity and time constraints.
The invalid email/password messages are behind pesudo-elements ::before ::after. Javascript can be written to read
the pesudo-element and validate.

Adding checks on the terms & contitions tab opening to the correct URL and with expected content.

Understanding how Ditto Music handles logins/sign-ups for their production environment; my assumption is that the journey
wouldn't stop at captcha and there is some tooling/api to get past this.

Signing up with a marketing checkbox ticked and unticked. Following this, making sure the CTA doesn't fire an event upon
clicking sign-up with terms not checked.

There are a lot of additions that could be made but these would be the most important additions.