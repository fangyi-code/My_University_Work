n = 5
for i in range(n,0,-1):
    spaces = " "*(n-i)
    stars = "*"*(2*i-1)
    print(spaces+stars+spaces)