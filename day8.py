# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
contato = dict(input().split() for _ in range(n))
while True:
    try:
        nome = input()
        if nome in contato:
            print("%s=%s"%(nome,contato[nome]))
        else:
            print("Not found")    
    except EOFError:
         break         
        