# https://leetcode.com/contest/weekly-contest-190/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

def is_prefix_word(sentence, searchWord):
    slist = sentence.split()
    for idx, s in enumerate(slist):
        if searchWord in s:
            if s.find(searchWord) == 0:
                return idx+1
    return -1
