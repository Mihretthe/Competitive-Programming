class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = "+-*/"
        def arthimetic(op1, op2, op):
            if op == "+":
                return op1 + op2
            elif op == "-":
                return op2 - op1
            elif op == "*":
                return op1 * op2
            else:                
                div = op2 / op1
                if div < 0:
                    return ceil(div)
                else:
                    return floor(div) 
            

        for token in tokens:
            if token in operations:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(arthimetic(operand1, operand2, token))
            else:
                stack.append(int(token))

        return stack[0]
        
        
