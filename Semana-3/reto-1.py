import random
import math

class vector:
    def __init__(self,n):
        self.n = n
        self.V = [0] * (n+1)
    
    def construyeVector(self, m, r):
        self.V[0] = m
        for i in range(1, m+1):
            self.V[i] = random.randint(1,r)
            
    def imprimeVector(self, mensaje = "vector sin nombre: \t"):
        print("\n", mensaje, end="")
        for i in range(1, self.V[0] + 1):
            print(self.V[i], end=",")
        print()
        
    def retornaDato(self, i):
        return self.V[i]
        
    
def primo(num):
    if num < 4:
        return True
    else:
        half_num = num // 2
        for i in range(2, half_num + 1):
            r = num % i
            if r == 0:
                return False
        return True
        
def impar(num):
    str_num = str(num)
    d1_num = int(str_num[0])
    if d1_num % 2 == 0:
        return False
    return True

def solucion():
    vec_mod = []
    n = random.randint(15,31)
    vec5 = vector(n)
    vec5.construyeVector(n,10000)
    # vec5 = [30, 23, 19, 18, 7, 21, 31, 12, 41, 9]
    s = 0
    for i in range(1, n+1):
    # for i in range(len(vec5)):
        dato = vec5.retornaDato(i)
        # dato = vec5[i]
        if primo(dato) or impar(dato):
            s = s + dato
            # vec_mod.append(dato)

    return vec5, s
    
vec,s= solucion()
print(s)
# print(vec)
# print(vec2)
print(vec.imprimeVector())


#method_list = [method for method in dir(vector) if method.startswith('__') is False]
#print(method_list)