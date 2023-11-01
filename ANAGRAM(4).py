def group_anagrams(strs):
    anagrams = {}
    
    for word in strs:
       
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
        result = list(anagrams.values())
    return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(strs)
print(output)
