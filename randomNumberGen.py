#linear congruence
#congruencia linear
def Congruencia_Linear (a, m, c, x0, randomNums, N_Random_Numbers):
    randomNums[0] = x0

    for i in range(1, N_Random_Numbers):
        #Xi = Xi - 1 * a + c mod M
        randomNums[i] = ((randomNums[i-1]*a)+c) % m

#normalize
#normalizacao
def normalizeNumbers (max, randomNums):
    for i in range(len(randomNums)):
        randomNums[i] = round((randomNums[i])/(max),4)
    return randomNums

#Every pseudo-random generated numbers
#Todos Numeros Pseudo-Randomicos gerados
class Generated_Numbers:
    def __init__(self, quantity, seed):
        x0 = seed
        a = 167942
        m = 1974658213
        c = 971502
        self.quantity = quantity+1
        randomNumbers = [0] * self.quantity
        Congruencia_Linear (a, m, c, x0, randomNumbers, self.quantity)
        maxNum = max(randomNumbers[1:])
        self.nums = normalizeNumbers(maxNum, randomNumbers[1:])
    
    def getNums(self):
        return self.nums


if __name__ == '__main__':
    #seed
    x0 = 123
    #*
    a = 167942
    #modulo
    m = 1974658213
    #+
    c = 971502

    #0=seed; Resto = n de rand;
    N_Random_Numbers = 10001

    #[]
    random_Numbers = [0] * N_Random_Numbers
    Congruencia_Linear (a, m, c, x0, random_Numbers, N_Random_Numbers)
    maxNum = max(random_Numbers[1:])
    normalized_Numbers = normalizeNumbers(maxNum, random_Numbers[1:])
    arrX=[0]*(N_Random_Numbers-1)
    for i in range(N_Random_Numbers-1):
        arrX[i]=i
    y = normalized_Numbers
    x = arrX