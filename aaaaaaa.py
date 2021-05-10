import datetime, random, time, click
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support import expected_conditions as EC
from time import gmtime, strftime
from selenium.webdriver.common.by import By

links = [] #리스트 
Ahref = [] #리스트 
ca = 10 #스크롤 마지막으로 내리는 수
nom = 1 #리스트에 따라 스크롤 내리기 
Userid = ''
Userpw = ''

def dri_click(nextFeed):
    ac = ActionChains(driver)   
    ac.move_to_element(nextFeed) 
    ac.click() 
    ac.perform()

cur_time =strftime("%Y-%m-%d %H:%M:%S", gmtime())
print('시작 시간 : ',cur_time)

driver = webdriver.Chrome('C:/VScode/wcbscraping_basic/chromedriver.exe') #"./chromedriver.exe"
driver.maximize_window() #윈도우 최대
driver.get('https://instagram.com') 
time.sleep(random.uniform(2,4))

#pass popup - 로그인 후 피드 페이지에서 팝업창
def pass_popup():
    try:
        popup = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        popup.send_keys(Keys.ENTER) 
        time.sleep(random.uniform(6,8))
        popup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]') 
        popup.send_keys(Keys.ENTER)
        time.sleep(random.uniform(3,5))
        profi()
    except ImportError:
        profi()

#프로필로 이동 클릭
def profi():
    clname = driver.find_element_by_class_name('gmFkV')         
    clname.send_keys(Keys.ENTER)
    time.sleep(random.uniform(3,5))

def end_qu():
    driver.quit()
    print('종료 시간 : ',cur_time)

#login 
login_id = driver.find_element_by_name('username') 
login_id.send_keys(Userid) 
login_pw = driver.find_element_by_name('password') 
login_pw.send_keys(Userpw) 
login_pw.send_keys(Keys.RETURN)

#로그인 오류 처리
try:
    emsg = driver.find_element_by_id('slfErrorAlert').text
    print('로그인 오류 : 몇 분 후에 다시 시도해주세요.')
    end_qu()
except:
    time.sleep(random.uniform(5,7))
    pass_popup()

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').click()
time.sleep(random.uniform(3,5))

for a in range(ca):
    if a >= 1:
        FollPanel = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for a in range(nom):
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', FollPanel)
            time.sleep(random.uniform(2,4))
    nom += 1
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    Ahref = soup.select('span.Jv7Aj.mArmR.MqpiF > a.FPmhX.notranslate._0imsa')
    for i in Ahref:             
        userDivId = i.get('title')
        i_tag = i
        print(userDivId)
        time.sleep(random.uniform(2,4))
        soup_2 = BeautifulSoup(driver.page_source, 'html.parser')
        Ahref_2 = soup_2.select('span.Jv7Aj.mArmR.MqpiF > a.FPmhX.notranslate._0imsa')
        
        if i_tag not in Ahref_2:
            scr_num = 120
            FollPanel_1 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            driver.execute_script('arguments[0].scrollTo(0, 0)', FollPanel_1)
            while i_tag not in Ahref_2:
                FollPanel_2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
                driver.execute_script('arguments[0].scrollTo(0, {})'.format(scr_num), FollPanel_2)
                time.sleep(random.uniform(2,3))
                soup_3 = BeautifulSoup(driver.page_source, 'html.parser')
                Ahref_2 = soup_3.select('span.Jv7Aj.mArmR.MqpiF > a.FPmhX.notranslate._0imsa')
                scr_num += 80

        btn_userCl = driver.find_element_by_link_text('{}'.format(userDivId))
        btn_userCl.click()
        time.sleep(random.uniform(3,5))

        g_count = int(driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(1) > span > span').text.replace(",", ""))
        if g_count >= 1:
            driver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a").click()
            time.sleep(random.uniform(3,5))
            yyyymmdd = driver.find_element_by_class_name('_1o9PC.Nzb55').get_attribute('title')
            yyyymmdd_1 = int(yyyymmdd[0:4])

            if g_count <= 3 or yyyymmdd_1 <= 2019: 
                btn_pass = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button')
                btn_pass.click()
                time.sleep(random.uniform(2,4))

                driver.find_element_by_class_name('_5f5mN.-fzfL._6VtSN.yZn4P').click()
                time.sleep(random.uniform(2,4))
                driver.find_element_by_class_name('aOOlW.-Cab_').click()
                time.sleep(random.uniform(2,4))
            else:
                btn_pass = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button')
                btn_pass.click()
                time.sleep(random.uniform(3,5))
                driver.find_element_by_class_name('_2dbep.qNELH').click()
                time.sleep(random.uniform(3,5))
        else:
            btn_pass = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button')
            btn_pass.click()
            time.sleep(random.uniform(2,4))

            driver.find_element_by_class_name('_5f5mN.-fzfL._6VtSN.yZn4P').click()
            time.sleep(random.uniform(2,4))
            driver.find_element_by_class_name('aOOlW.-Cab_').click()
            time.sleep(random.uniform(2,4))

        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]').click() 
        time.sleep(random.uniform(3,5))                
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').click()
        time.sleep(random.uniform(3,5))
            


