from appium import webdriver

#import uiautomator2 as u2
import time
#server启动参数
desired_caps = {}
desired_caps["platformVersion"] = "6.0.1"
desired_caps['unicodeKeyboard'] = True
desired_caps["deviceName"] = "huawei"
desired_caps["platformName"] = "Android"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".GridSettings"
#desired_caps["'appWaitActivity'"] = ".player.activity.TVDetailActivity"
#desired_caps["newCommandTimeout"]="180"
#desired_caps["keep_alive"]="true"
#解决设备经常断开连接重新启动问题cap.setCapability("noReset", true);newCommandTimeout:180
#desired_caps["noSign"]="true"
#desired_caps["noReset"]="true"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

try:
    #定位一个元素
    # driver.find_element_by_id("com.android.settings:id/icon").click()
    # time.sleep(2)
    #定位一组元素
    ele_list = driver.find_elements_by_id("android:id/title")
    for i in ele_list:
        print(i.text)
        if i.text == '蓝牙':
            i.click()

except Exception as e:
    print(e)
finally:
    driver.quit()
