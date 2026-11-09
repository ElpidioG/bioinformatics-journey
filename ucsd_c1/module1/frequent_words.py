"""Module 1 challenge: FrequentWords.

Find all most frequent k-mers in Text. Occurrences may overlap, and if several
k-mers tie for the highest count, return all of them.

Example:
    frequent_words("TGGACGTTGGCCCAGCTGGTCCCACGTGGT", 3) -> ["TGG"]   (TGG appears 4 times)

Usage:
    py ucsd_c1/module1/frequent_words.py TGGACGTTGGCCCAGCTGGTCCCACGTGGT 3
"""

import sys
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] += 1      
    return freq


def frequent_words(Text, k):
    words =[]
    freq = FrequencyMap(Text,k)
    m = max(freq.values())


    for key in freq:
        
        if m == freq[key]:
            words.append(key)
        

 
    return words




if __name__ == "__main__":
    text, k = sys.argv[1], int(sys.argv[2])
    print(" ".join(frequent_words(text, k)))
