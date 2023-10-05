def isAnagram01(s: str, t: str) -> bool:
    s = "".join(sorted(s, key=str.lower))
    t = "".join(sorted(t, key=str.lower))
    return s == t

def isAnagram02(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def isAnagram03(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True

def isAnagram04(s: str, t: str) -> bool:
    from collections import Counter
    return Counter(s) == Counter(t)


def main():
    s = "anagram"
    t = "nagaram"
    print(s, t)
    print(isAnagram01(s, t))
    print(isAnagram02(s, t))
    print(isAnagram03(s, t))
    print(isAnagram04(s, t))
    
    print("----------")

    s = "rat"
    t = "car"
    print(s, t)
    print(isAnagram01(s, t))
    print(isAnagram02(s, t))
    print(isAnagram03(s, t))
    print(isAnagram04(s, t))

if __name__ == "__main__":
    main()
