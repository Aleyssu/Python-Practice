def length_of_longest_substring(s: str) -> int:
    chars = set()
    start_index = 0
    curr_index = 0
    maxlen = 0
    currlen = 0
    for c in s:
        # "snip" off the head portion of the substring 
        # that leads up to the first repeating char when 
        # one is found and continue searching
        if c in chars:
            len_to_remove = 0
            for c1 in s[start_index:]:
                len_to_remove += 1
                if c1 == c:
                    break
                else:
                    chars.remove(c1)
            start_index += len_to_remove
            if currlen > maxlen:
                maxlen = currlen
            currlen -= len_to_remove
        else:
            chars.add(c)
        currlen += 1
    if currlen > maxlen:
        return currlen
    else:
        return maxlen
        
print(length_of_longest_substring("1234567890qwertyuiop[]asdfghjkl;'zxcvbnm,./"))