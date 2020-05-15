from selenium import webdriver
import time
driverPath = "D:\\chromedriver.exe" #Webdriver 路徑
browser = webdriver.Chrome(driverPath)
browser.get("https://www.com.tw/cross/uncontinuequery109.html") #批次查詢網址
time.sleep(7) #等待驗證延遲

#print(browser.title)
stulist = open("stuids.txt", encoding="utf-8").readlines() #欲查詢的學生准考證序號名單

students = len(stulist)
count_per_query = 50 #每次查詢筆數
#print(len(stulist))

count = 0

for j in range( int(students/count_per_query)+1 ):
    if j >= 1:
        browser.get("https://www.com.tw/cross/uncontinuequery109.html")
        time.sleep(1)
    stuid = ""
    for i in range(count_per_query):
        if count < students-1:
            count += 1
            stuid += str(stulist[count])
        else:
            break
    #print(stuid)

    testid = browser.find_element_by_id("testids")
    testid.send_keys(stuid)
    captcha = browser.find_element_by_id("captcha")
    valicode = input("請手動輸入驗證碼->")
    captcha.send_keys(valicode)
    submitbtn = browser.find_element_by_id("submit")
    submitbtn.click()

    time.sleep(1)
    with open('pages\\page'+str(j)+'.html', 'w', encoding="utf-8") as f:
        f.write(browser.page_source)

    if count >= students:
        break
