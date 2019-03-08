from appium import webdriver

desired_caps = {}

desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "6.0"
desired_caps["deviceName"] = "huawei"

desired_caps["appPackage"] = "com.tcl.appmarket2"
#desired_caps["appWaitActivity"] = ".player.activity.TVDetailActivity"
desired_caps["appActivity"] = ".newUI.MainActivity"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.install_app("E:\python_work\other\沙发电视助手_1.0.1.apk")
#a = driver.is_app_installed("com.tcl.appmarket2")
#print(a)
#if(a):
#    driver.remove_app("com.shafa.helper")

print("1111")
driver.quit()
