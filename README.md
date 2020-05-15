# 申請入學榜單查詢爬蟲
透過准考證號碼名單批次查詢並抓取在 http://www.com.tw 上的放榜資料。

## 前置需求
* Chrome Webdriver
* 可透過`requirement.txt`進行自動安裝:
    * Selenium
    * BeautifulSoup

## 使用說明

### 準備
請先確定*get_data.py*中的`driverPath`有正確對應至Chrome Webdriver的路徑。
(預設為`D:\chromedriver.exe`)

### get_data.py 抓取榜單資料
執行該程式，並手動輸入所需驗證碼。

你可以透過修改程式內每次查詢筆數，來減少驗證碼輸入次數。
但請注意，越高的單次查詢筆數，越容易造成無法獲取正確資料。

每次查詢資料的檔案，將會儲存於*pages*資料夾。
如果查詢時意外中斷，建議手動清空該資料夾內的所有檔案，以確保資料不重複寫入。

### filter_all.py 篩選出所需榜單資料並整合輸出
該程式將會讀取*pages*資料夾內的所有資料檔案，在經過篩選後，整合輸出為*output.html*檔。
