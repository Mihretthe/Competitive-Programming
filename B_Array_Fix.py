def isOn(num, k):
    number = 1 << k
    return bool(number & num)

def binary(num):
    ans = []
    for i in range(31, -1, -1):
        ans.append(str(num >> i & 1))
    
    return "".join(ans)

def PowerOfTwo(num):
    return not (num & (num - 1))

def toUpper(letter):
    # return chr(ord(letter) & ~ord(" "))
    return chr(ord(letter) & ord("_"))

def toLower(letter):
    return chr(ord(letter) | ord(" "))

def where(letter):
    return ord(letter) & 31

def swap(a, b):
    a = a ^ b
    b = b ^ a
    a = a ^ b

    return (a, b)

def clearLSB(num, i):
    return num & (~((1 << (i + 1)) - 1))

def clearMSB(num, i):
    return num & (1 << (i + 1) - 1)

def changeEveryBit(num):
    return num ^ ((1 << num.bit_length()) - 1)

def extractLastBit(num):
    return num & -num

def removeLastBit(num):
    return num & (num - 1)