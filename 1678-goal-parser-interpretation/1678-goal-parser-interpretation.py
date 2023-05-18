class Solution:
    def interpret(self, command: str) -> str:
        i=0
        a=""
        while i<len(command):
            if command[i]=="G":
                a+="G"
            elif command[i]=="(" and command[i+1]==")":
                a+="o"
                i+=1
            elif command[i]=="(" and command[i+1]=="a":
                a+="al"
                i+=3
            i+=1
        return a