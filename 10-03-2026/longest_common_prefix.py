def longestCommonPrefix(strs):
    prefix=''
    for chars in zip(*strs):
        if len(set(chars))==1:
            prefix+=chars[0]
        else:
            break
    return prefix