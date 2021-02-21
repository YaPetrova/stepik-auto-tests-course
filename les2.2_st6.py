from selenium import webdriver
import time

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for= 'robotCheckbox' ]")
    option1.click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("window.scrollBy(0, 70);")
    option2.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



