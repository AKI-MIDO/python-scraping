from selenium import webdriver


'''
ポータルサイトへの自動ログイン
'''

driver_path = "パス"
driver = webdriver.Chrome(driver_path)

#ポータルサイトのログイン画面にアクセス
driver.get("URL")

#ログインID（学籍番号）の入力
id = driver.find_element_by_id("loginId")
id.send_keys("ログイン")

#パスワードの入力
password = driver.find_element_by_id("passwordId")
password.send_keys("パスワード")

#上記でIDとパスワードを入力後にログインのボタンを押すイベントを発生
login_button = driver.find_element_by_id('loginPost')
login_button.click()


'''
ポータルサイトから必要な情報を取得する
'''

#簡易ポータルから通常ポータルへ移動
potal_move = driver.find_element_by_xpath('------')
potal_move.click()

#インフォメーションの項目に移動
imformation = driver.find_element_by_xpath('-----')
imformation.click()

#インフォメーションの項目から最新の情報をゲット！
