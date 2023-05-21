class Solution:    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        if "!" in paragraph:
            paragraph=paragraph.replace("!"," ")
        if "?" in paragraph:
            paragraph=paragraph.replace("?"," ")
        if "," in paragraph:
            paragraph=paragraph.replace(","," ")
        if ";" in paragraph:
            paragraph=paragraph.replace(";"," ")
        if "." in paragraph:
            paragraph=paragraph.replace("."," ")
        if "'" in paragraph:
            paragraph=paragraph.replace("'"," ")
        paragraph=paragraph.split()
        paragraph=[i for i in paragraph if i not in banned]
        a=[]
        for i in paragraph:
            a.append(paragraph.count(i))
        x=paragraph[a.index(max(a))]
        return x