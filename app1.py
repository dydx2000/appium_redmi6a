from appium import webdriver

desired_caps = {
  "platformVersion": '9',
  "deviceName": "10.10.10.29:5555",
  "automationName": "UiAutomator2",
  "noReset": True,
  # "appPackage": "com.android.calendar",
  "appActivity": "com.android.calendar.homepage.AllInOneActivity",
  "platformName": "Android",
  # "skipDeviceInitialization": True,
  # "skipServerInstallation": True,
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_id('com.android.calendar:id/settings_button').click()
driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.ImageView').click()
driver.find_element_by_id('android:id/button1').click()


driver.quit()
 