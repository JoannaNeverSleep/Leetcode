'''844. Backspace String Compare'''


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def get_valid_pointer(string, pointer, cnt):
            while pointer >= 0:
                if string[pointer] == '#': # s[pointer_s] == '#' -> increase count by 1 + move pointer
                    cnt += 1
                    pointer -= 1
                elif cnt > 0: # s[pointer_s] != '#' and cnt_s >0 -> decrease count by 1 + move pointer(delete a letter)
                    cnt -= 1
                    pointer -= 1
                else:
                    break
            return pointer
        
        pointer_s, pointer_t = len(s) - 1, len(t) - 1
        cnt_s, cnt_t = 0, 0 # count for "#"
        while pointer_s >= 0 or pointer_t >= 0:
            pointer_s = get_valid_pointer(s, pointer_s, cnt_s)
            pointer_t = get_valid_pointer(t, pointer_t, cnt_t)
            
            if pointer_s >=0 and pointer_t >= 0:
                if s[pointer_s] != t[pointer_t]:
                    return False
            elif pointer_s >=0 or pointer_t>=0:
                return False
            pointer_s -= 1
            pointer_t -= 1
        return True
