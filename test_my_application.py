

def test_click(page):
    page.goto("http://www.uitestingplayground.com")
    page.click("text=Click")
    page.click("#badButton")

def test_input(page):
    page.goto("http://www.uitestingplayground.com/textinput")
    page.fill("#newButtonName", "Test Name")
    page.click("#updatingButton")
    assert page.inner_text("#updatingButton") == "Test Name"

def test_scrollbars(page):
    page.goto("http://www.uitestingplayground.com/scrollbars")
    page.click("#hidingButton")


def test_login_logout(page):
    # login
    page.goto("http://www.uitestingplayground.com/sampleapp")
    page.fill('//input[@placeholder="User Name"]', 'Naz')
    page.fill('//input[@name="Password"]', 'pwd')
    page.click("#login")
    assert page.inner_text("#loginstatus") == "Welcome, Naz!"

    # logout
    page.click("#login")
    assert page.inner_text("#loginstatus") == "User logged out."


def test_login_fail(page):
    page.goto("http://www.uitestingplayground.com/sampleapp")
    page.fill('//input[@placeholder="User Name"]', 'Tim')
    page.click("#login")
    assert page.inner_text("#loginstatus") == "Invalid username/password"


def test_nonbreakingspace(page):
    page.goto("http://www.uitestingplayground.com/nbsp")
    page.click("text=My Button")

def test_progress_bar(page):
    page.goto("http://www.uitestingplayground.com/progressbar")
    page.click("#startButton")
    page.inner_text("#progressBar[aria-valuenow='75']")
    page.click("#stopButton")
    assert "Result: 0" in page.inner_text("#result")


