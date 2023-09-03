z = [1, 3, 2, 4, 'Alice', 'Bob']
z.sort(key=str)
print(z)

print("Hello there!\nHow are you?\nI\'m doing fine.")

multi_line = """Hello there!
How are you?
I'm fine."""
print(multi_line)

spam = 'Hello World'
s = spam.strip()
print(s)

spam = 'Hello World'
s = spam.lstrip('Hel')
print(s)

spam = 'Hello World'
s = spam.rstrip('World')
print(s)

print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))