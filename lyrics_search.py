import sys
sys.setrecursionlimit(100000)

class trie():          #트라이 구조 기반
    result = 0
    def __init__(self):
        self.next_word = {}
        self.word_count = {}
        
    def add(self,word,lenw):
        if lenw in self.word_count:
            self.word_count[lenw] += 1
        else :
            self.word_count[lenw] = 1
        
        now = self
        for w in word:                   #트라이 저장을 위해 문자 하나씩 추출
            if w in now.next_word:       #이미 저장되어 있다면
                now = now.next_word[w]   #해당 객체로 이동
                if lenw in now.word_count:     #단어의 길이 별로 개수를 저장해둠
                    now.word_count[lenw] += 1
                else:
                    now.word_count[lenw] = 1
            else:                        #해당 문자의 객체가 없다면성생성
                now.next_word[w] = trie()
                now = now.next_word[w]
                now.word_count[lenw] = 1
    
    def search(self,word):
        lenw = len(word)
        now = self
        
        for w in word:
            if w in now.next_word:
                now = now.next_word[w]          #문자가 있다면 해당 객체로 이동
            elif w == '?':                      #?에 매칭될 시 단어의 길이가 같은 문자들 개수 리턴
                if lenw in now.word_count:
                    return now.word_count[lenw]
                else:              #길이 같은 문자 없음
                    return 0
            else:                  #매치되는 문자 없음
                return 0
        return now.word_count[lenw]

def solution(words, queries):
    answer = []
    nor_trie = trie()
    rev_trie = trie()
    for word in words:
        nor_trie.add(word,len(word))
        rev_trie.add(word[::-1],len(word))        #?가 앞에있는 경우의 트라이 구조
    
    for word in queries:            #각단어의 ?의 위치에따라 해당되는 트라이 선택해서 개수를 리턴받아 저장
        if word[0] == '?':
            word = word[::-1]
            answer.append(rev_trie.search(word))
        else:
            answer.append(nor_trie.search(word))
    return answer
