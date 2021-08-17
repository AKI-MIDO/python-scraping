from selenium import webdriver


'''
ポータルサイトへの自動ログイン
'''

driver_path = "/Users/endouakira/Desktop/chromedriver"
driver = webdriver.Chrome(driver_path)

#ポータルサイトのログイン画面にアクセス
driver.get("https://t-portal.main.teikyo-u.ac.jp/start/auth/login?error=L00002")

#ログインID（学籍番号）の入力
id = driver.find_element_by_id("loginId")
id.send_keys("19E122009")

#パスワードの入力
password = driver.find_element_by_id("passwordId")
password.send_keys("1Endoakira.")

#上記でIDとパスワードを入力後にログインのボタンを押すイベントを発生
login_button = driver.find_element_by_id('loginPost')
login_button.click()


'''
ポータルサイトから必要な情報を取得する
'''

#簡易ポータルから通常ポータルへ移動
potal_move = driver.find_element_by_xpath('//a[@href="/start/auth/after/notice"]')
potal_move.click()

#インフォメーションの項目に移動
imformation = driver.find_element_by_id('quick')
imformation.click()