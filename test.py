print('hello world')

n = "Baby's world"
m = 'Hello ghada'
print(m)
print(n)
print(len(m))
print(m[0])  # character with index 0
print(m[0:5])  # the word from the index 0 to the index 5
print(m[6:])  # the word from the index 6 to the end

print(m.lower())
print(m.upper())
print(m.count('lo'))  # count the occurrence of the syllables
print(m.find('Hello'))
m = m.replace('ghada', 'Universe')
print(m)

greeting = 'hello'
name = 'ghada'
message = greeting +',' + name + 'welcome !'
message2 = '{},{}. Welcome!'.format(greeting,name)
print(message)
print(message2)