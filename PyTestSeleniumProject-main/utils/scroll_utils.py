def scroll_element_into_view(browser, element):
    browser.execute_script('return arguments[0].scrollIntoView(true);', element)
