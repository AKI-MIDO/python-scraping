from selenium import webdriver
import requests
import time

#----------------------------
# ポータルサイトへの自動ログイン -
#----------------------------

driver_path = "/Users/endouakira/Desktop/chromedriver2"
driver = webdriver.Chrome(driver_path)

#ポータルサイトのログイン画面にアクセス
driver.get("https://t-portal.main.teikyo-u.ac.jp/start/auth/login?error=L00002")


#ログインID（学籍番号）の入力
id = driver.find_element_by_id("loginId")
id.send_keys("19E122009")

#パスワードの入力
password = driver.find_element_by_id("passwordId")
password.send_keys("1Endoakira.")

#ログインidとパスワードを確実に入力させる
time.sleep(0.5)

#上記でIDとパスワードを入力後にログインのボタンを押すイベントを発生
login_button = driver.find_element_by_id('loginPost')
login_button.click()


#------------------------------------
#  ポータルサイトから必要な情報を取得する　-
#------------------------------------

#簡易ポータルから通常ポータルへ移動
potal_move = driver.find_element_by_xpath('//a[@href="/start/auth/after/notice"]')
potal_move.click()


#インフォメーションの項目に移動
imformation = driver.find_element_by_xpath('//*[@id="standard"]/dl[6]/dt/div/figure/a')
imformation.click()

#ここで一旦時間をおかないとxpathが取れない。
time.sleep(5.0)

cur_url=driver.current_url
#print(cur_url)
detail_info = driver.find_element_by_css_selector('#searchTbody > tr:nth-child(1) > td:nth-child(5)')
txt=detail_info.text
print(detail_info.text)

#-----------------
#LINE Notifyと連携
#-----------------

notify_url = 'https://notify-api.line.me/api/notify'
notify_token = 'R8xBcHMw6iuTdvpkZH189GjVFrTgeeIrQ6cnI3DREZw'

def main():
    #line notifyの設定
    method="POST"
    headers = {"Authorization" : "Bearer "+ notify_token}

    #現在保存されている情報を確認
    f1=open("/Users/endouakira/Desktop/大学の研究発表/test.txt","r",encoding="UTF-8")
    last_text=f1.read()
    f1.close()
    
    #以前の情報と新たに取得した情報を比較。
    if txt==last_text:
        
        #同じならドライバーを閉じる
        driver.quit()

    #情報が一致しなかったらその情報をlineで通知
    else:    
        #通知するべき情報の設定
        notify="\n「"+txt+"」\n"+"というお知らせが届いています"
        payload = {"message":notify}
        requests.post(notify_url, headers = headers, params = payload)
        
        #保存する情報を更新
        f1=open("/Users/endouakira/Desktop/大学の研究発表/test.txt","w",encoding="UTF-8")
        f1.write(txt)
        f1.close()
        driver.quit()


if __name__ == "__main__":
    main()
