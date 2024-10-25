class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda x : len(x))
        folders = folder

        answer = []
        till = set()
        for i in range(len(folder)):
            folder[i] = tuple(folder[i].split("/")[1:])

        root = TrieNode()

        for a in range(len(folder)):
            path = folder[a]
            pointer = root
            # print(path)
            for i in path:
                if pointer.is_end:
                    break
                # index = ord(i) - 97
                index = 0
                if i not in pointer.children:
                    pointer.children[i] = TrieNode()
                pointer = pointer.children[i]
            else:
                answer.append("/" + "/".join(folders[a]))
            pointer.is_end = True



        return answer