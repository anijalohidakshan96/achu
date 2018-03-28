message="a custom-crafted wetsuit helped Pierre,the African penguin,recover from a bout of baldness"
if message.find('the')==-1:
 print('not present')
else:
 print('present')
l=message.count('the')
print(l)
o=message.capitalize()
print(o)
p=message.split(',')
print(p)
if message.isupper():
 print(message.lower())
else:
 print(message.upper())
