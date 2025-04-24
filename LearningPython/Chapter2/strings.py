from importlib import reload

# SEQUENCE OPERATIONS
print('Sequence Operations')
S = 'Spam'
print(len(S))
print(S[0])
print(S[1])

print(S[-1])
print(S[-2])

print(S)
print(S[1:3])
print(S[0:3])

print(S + ' Blam')

# IMMUTABILITY
print('Immutability')
print(S)

# S[0] = 'z'
S = 'z' + S[1:]
print(S)

#TYPE SPECIFIC METHODS
print("Type-Specific Methods")

print(S.find('pa'))
print(S.replace('pa', 'XYZ'))

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))
S.upper()
print(line.isalpha())
line = line.rstrip() # Remove whitespace characters on the right side

print('%s, eggs, and %s' % ('spam', 'SPAM!'))

# print(dir(S))

#HELP
"""
The dir function simply gives the methods names. To ask what they do, you can pass
them to the help function:
"""
print(help(S.replace))

S = 'A\nB\tC' # \n is end-of-line, \t is tab
len(S) 
print(ord('\n')) # \n is a byte with the binary value 10 in ASCII

msg = """ aaaaaaaaaaaaa
bbb'''bbbbbbbbbb""bbbbbbb'bbbb
cccccccccccccc"""
print(msg)