#
print("hello 'word'")
print('hello "word"')
print("'hello' \"word\"")
print("'")

#让转义符失效 （r,repr,\）
print(r"\n")
print("Let \' go")
print(repr("hello \n word"))
print("hello \\ word")
#保持原格式输出
print('''

hello
      word
      ''')
