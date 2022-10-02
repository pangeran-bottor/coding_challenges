from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        q = deque([[beginWord, 1]])

        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + ch + word[i+1:]                    
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        q.append([next_word, length+1])
        return 0
