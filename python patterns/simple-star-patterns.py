# sqaure pattern
n = 5
#SQAURE
print("PATTERN #1: SQAURE PATTERN")
for i in range(n): 
    for j in range(n): 
        print("*", end=' ')
    print()
#INCREASING TRIANGLE
print("")
print("PATTERN #2: INCREASING TRIANGLE")
for i in range(n): 
    for j in range(i+1):
        print("*", end=' ')
    print()
print("")
# DECREASING TRIANGLE
print("PATTERN #3: DECREASING TRIANGLE")
for i in range(n):
    for j in range(i, n):
        print("*", end=' ')
    print()

print("")
# RIGHT SIDED TRIANGLE
print("PATTERN #4: RIGHT SIDED TRIANGLE")
for i in range(n):
    for j in range(i, n):
        print('', end='')
    
    for k in range(i+1):
        print("*", end=' ')
    print()
print("")
# DOWNWARD RIGHT SIDED TRIANGLE
print("PATTERN #5: DOWNWARD RIGHT SIDED TRIANGLE")
for i in range(n):
    for j in range(i+1):
        print('', end='')
    for k in range(i, n):
        print('*', end=' ')
    print()
print("")
# HILL PATTERN
print("PATTERN #6: HILL PATTERN")
for i in range(n): 
   for j in range(i, n): 
      print(' ', end=' ') 
   for k in range(i):
      print('*', end=' ')
   for l in range(i+1):
      print('*', end=' ')
   print()
print("")
# REVERSE HILL PATTERN
print("PATTERN #7: REVERSE HILL PATTERN")
for i in range(n): 
   for j in range(i+1): 
      print(' ', end=' ') 
   for k in range(i, n-1):
      print('*', end=' ')
   for l in range(i, n):
      print('*', end=' ')
   print()
print("")
# DIAMOND PATTERN
print("PATTERN #7: DIAMOND PATTERN")
for i in range(n-1): 
   for j in range(i, n): 
      print(' ', end=' ') 
   for k in range(i):
      print('*', end=' ')
   for l in range(i+1): 
      print('*', end=' ')
   print() 
for i in range(n): 
   for j in range(i+1): 
      print(' ', end=' ') 
   for k in range(i, n-1):
      print('*', end=' ')
   for l in range(i, n):
      print('*', end=' ')
   print()
print("")
