def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        map_brackets = {
            '{':'}',
            '(':')',
            '[':']'
        }
        chars = list(s)
        
        stack = []
        for c in chars:
            if c in map_brackets.keys():
                stack.append(c)
            elif  len(stack)>0 and map_brackets[stack[len(stack)-1]] == c:
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        return False

print isValid('()')