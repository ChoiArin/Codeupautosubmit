import os
from selenium import webdriver
import time
dirname = '폴더입력'
filenames = os.listdir(dirname)

driver = webdriver.Firefox('C:/bin')
driver.implicitly_wait(3)

driver.get('http://codeup.kr/JudgeOnline/loginpage.php')
driver.find_element_by_name('user_id').send_keys('아이디')
driver.find_element_by_name('password').send_keys('비번')
time.sleep(10)
driver.find_element_by_name('submit').click()
i = 0
for filename in filenames:
    full_filename = os.path.join(dirname, filename)
    with open(full_filename, 'r', encoding='utf-8-sig') as f:
        n = full_filename.split('\\')
        n = n[1]
        k = int(n.split('.')[0])
        '''
	제외할 조건을 if에다가 써주세요
	if :
            continue
	'''
        a = f.read()
        i+=1
        driver.get('http://codeup.kr/JudgeOnline/submitpage.php?id='+str(k))
        el = driver.find_element_by_id('language')
        if a.find("<bits/stdc++.h>") != -1 or a.find("using namespace std") != -1 or a.find("bool") != -1 or a.find('#include <algorithm>') != -1:
            driver.find_element_by_xpath("//select/option[@value='1']").click()
        elif a.find("System.out.print") != -1:
            driver.find_element_by_xpath("//select/option[@value='3']").click()
        else:
            driver.find_element_by_xpath("//select/option[@value='0']").click()
        driver.find_element_by_id('edit_area_toggle_checkbox_source').click()
        driver.find_element_by_id('source').clear()
        driver.find_element_by_id('source').send_keys(a)
        driver.find_element_by_id('Submit').click()
        print(k,'번 완료')
        time.sleep(10)