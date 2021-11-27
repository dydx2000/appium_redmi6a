import uiautomator2 as u2
d = u2.connect()
print(d.info)
# print(d.app_current())
# d.app_start('com.android.calendar')
print(d.app_list_running())
print(d.device_info)
d.press('recent')