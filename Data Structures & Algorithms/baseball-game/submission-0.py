class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def is_int(val):
            try:
                int(val)
                return True
            except:
                return False

        scores = []

        for i, operation in enumerate(operations):
            if is_int(operation):
                scores.append(int(operation))
            elif operation == '+':
                scores.append(scores[-1]+scores[-2])
            elif operation == 'D':
                scores.append(2*scores[-1])
            elif operation == 'C':
                scores.pop()
        return sum(scores)