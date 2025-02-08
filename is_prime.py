from math import isqrt

def isPrime(num):
    """
        param: num
        Checks if 'num' is Prime Number  
    """
    
    sq = isqrt(num) + 1
    
    for i in range(2, sq):
        if num % i == 0:
            return False
    
    return True

def listPrimeNumbers(num):    
    """
        param: num
        List Prime Numbers that are less than 'num'
    """
    
    theList = []
    
    for i in range(2, num):
        if isPrime(i):
            theList.append(i)
        
    return theList


def isPrimitiveRoot(num, to):
    """
        param1: num
        param2: to
        Checks if 'num' is Primitive Root to 'to'
    """
    
    numbers = set()
    
    for i in range(1, to):
        numbers.add(pow(num, i, to))
    
    return len(numbers) == to - 1
        
    


def findPrimitiveRoot(num):    
    """
        param: num
        List out all Primitive Roots of 'num' 
    """
    
    primeNumbersTill = listPrimeNumbers(num)
    collectedPrimitiveRoots = []
    
    for n in primeNumbersTill:
        if isPrimitiveRoot(n, num):
            collectedPrimitiveRoots.append(n)
    
    return collectedPrimitiveRoots



def findPublicKey(x, p):
    """
        param1: x
        param2: p
        Give the Public Key with the Choosen value 'x' and the large prime number 'p'
    """
    
    g = findPrimitiveRoot(p)
    print(g)
    if g:
        g = g[0]
    else:
        return "Can't Find"
    
    return pow(g, x, p)


def findSharedKey(x, publicKey, p):
    """
        param1: x
        param2: publicKey
        param3: p
        Returns the Shared Key
    """
    
    return pow(publicKey, x, p)

X = 11
Y = 18
P = 137

sendersPublicKey = findPublicKey(X, P)
receiversPublicKey = findPublicKey(Y, P)


print(f"Sender's Public Key: {sendersPublicKey}")
print(f"Receiver's Public Key: {receiversPublicKey}")

sharedKey = findSharedKey(X, receiversPublicKey, P)
sharedKey1 = findSharedKey(Y, sendersPublicKey, P)

print(f"Shared Key: {sharedKey} == {sharedKey1}")



