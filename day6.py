# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    palavra = input()
    print(palavra[::2] + " " + palavra[1::2])
    
    ''' Nova versão '''
    
if __name__ == '__main__':
    N = int(input().strip())
    for _ in range(N):
        palavra = input()
        print(palavra[::2] + " " + palavra[1::2])
