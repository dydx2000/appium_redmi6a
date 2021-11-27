import uiautomator2 as u2

# d = u2.connect('12dd6e53') # connect to device
d = u2.connect('10.10.10.29')
print(d.info)
d.implicitly_wait(10.0)

# d.click(0.695, 0.35)
# d(resourceId="com.android.calendar:id/settings_button").click()
# d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
# d(resourceId="android:id/button1").click()
# # d.app_stop_all()

# tex = d(resourceId="com.autel.autelsky:id/tv_left_title", text="APP版本").sibling(resourceId="com.autel.autelsky:id/tv_right_desc").get_text()
# tex = d(resourceId="com.autel.autelsky:id/tv_left_title", text="APP版本").right(resourceId="com.autel.autelsky:id/tv_right_desc").get_text()
# tex = d(resourceId="com.autel.autelsky:id/tv_left_title", text="APP版本").right().get_text()
# print(tex)
# d(resourceId="com.android.calendar:id/lunar_day").click()