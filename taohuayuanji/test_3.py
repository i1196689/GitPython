

import win32gui 
import win32api 
classname = 'TrayNotifyWnd'
titlename = '微信'
hwnd = win32gui.FindWindow(classname,titlename)

left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left,top,right,bottom)

