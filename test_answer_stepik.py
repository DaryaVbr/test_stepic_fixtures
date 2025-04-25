import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


@pytest.mark.parametrize("url", ['https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                 'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'
                                ])
class TestAnswerStep():
    def test_login_stepic(self, browser, url):
        browser.implicitly_wait(10)
        link_ans = url
        browser.get(link_ans)
        enter_button = browser.find_element(By.ID, 'ember466')
        enter_button.click()

        print("началась авторизация")
        login_input = browser.find_element(By.CSS_SELECTOR, '[placeholder = "E-mail"]')
        login_input.send_keys('вставить логин')
        password_input = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Пароль"]')
        password_input.send_keys('вставить пароль')
        login_button = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn')
        login_button.click()
        print("авторизация успех")

        time.sleep(8)
        # WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area")))
        input_ans = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
        input_ans.send_keys(math.log(int(time.time())))
        print("ответ вставлен в поле")
        time.sleep(8)
        # WebDriverWait(browser, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        # )
        button_ans = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button_ans.click()
        print(
            "кнопка нажата"
        )

        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))).text
        correct_ans = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        print(f"text of mistake: {correct_ans.text}")
        assert 'Correct!' in correct_ans.text









