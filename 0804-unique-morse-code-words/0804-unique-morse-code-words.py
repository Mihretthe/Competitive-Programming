class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s="abcdefghijklmnopqrstuvwxyz"
        b=set()
        for i in words:
            c=""
            for j in i:
                c+=a[s.index(j)]
            b.add(c)       
        return len(b)