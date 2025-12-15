# Python: script 언어(소스코드를 한 줄씩 읽어 바로 실행하는 Interpreter방식)
'''
interpreter 방식을 사용하기 위해서 REPL이라는 도구를 사용합니다.
ReadEvaluationPrintLoop
'''

print("print의 속성 : self, *args, sep='', end='\n', file=None")

print('Hello World') # self
print(True, 3.14, 'Python') # *args
print("\\,\t, \', \", \n ") # 특수기호
print("hello\tworld\t!")
print() # 한줄 내려쓰기
print("파이썬은 정말 쉬운 언어에요'컨셉이 쉽기 때문'")
print('문이 열리고 "배달 왔어요"')
print('''
"hello " world ' " ' hello'"'
''')
print("""해 뜨는 동해에서
해지는 서해까지
뜨거운 남도에서
광활한 만주벌판
""")
print("="*20)
# print("="+20)
print("문자열은 문자열끼리만 "+str(20))

for i in range(10):
  print(i, end=", ")
print()
print(1,2,3,4,5, sep='🚀')

with open('test.txt','w') as f:
  print("hello \n python", file=f)

f = open('test.txt','r')
lines = f.readlines()
for line in lines: print(line, end="🚩")

