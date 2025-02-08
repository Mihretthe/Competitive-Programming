import sys
input = sys.stdin.read

def main():
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        r = int(data[index + 2])
        c = int(data[index + 3])
        result = (n - r) * (m - 1) + n * m - (r - 1) * m - c
        results.append(result)
        index += 4
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
