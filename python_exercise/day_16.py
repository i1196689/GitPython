#使用 Python 实现：一些功能
# coding="utf-8"
# -*- coding:utf-8 -*-
import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone()as source:
    print("Say something!")
    audio=r.listen(source)

print("Shinx thinks you said: "+r.recognize_sphinx(audio,language="zh-CN"))
