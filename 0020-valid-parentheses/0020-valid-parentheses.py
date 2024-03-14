class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        start_chars = ['[', '(', '{']

        for char in s:
            if char in start_chars:
                stack.append(char)
            elif stack and char == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and char == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
