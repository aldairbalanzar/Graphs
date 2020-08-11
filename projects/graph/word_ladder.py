from queue import Queue

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def get_neighbors(word):
    neighbors = []
    string_word = word[:]
    for i in range(len(string_word)):
        for letter in letters:
            word_copy = string_word[:]
            word_copy[i] = letter
            w = ''.join(word_copy)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors

def find_ladders(begin, end):
    q = Queue()
    q.enqueue([begin])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]
        if current_node not in visited:
            visited.add(current_node)
            if current_node == end:
                return path
            for neighbor in get_neighbors(current_node):
                path_copy = path[:]
                path_copy.append(neighbor)
                q.enqueue(path_copy)