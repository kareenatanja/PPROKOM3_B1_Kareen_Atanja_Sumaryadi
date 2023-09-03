def main():
    name = "Hello World!"
    print(name.startswith('Hello'))
    print(name.endswith('World!'))
    
    name = "abc123"
    print(name.startswith('abcdef'))
    print(name.endswith('12'))
    
    name = 'Hello world!'
    print(name.startswith('Hello world!'))
    print(name.endswith('Hello world!'))
if __name__ == "__main__":
    main()

print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '=')) 