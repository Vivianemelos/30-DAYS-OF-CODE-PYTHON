# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    palavra = input()
    print(palavra[::2] + " " + palavra[1::2])