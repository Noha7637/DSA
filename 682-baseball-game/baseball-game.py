class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        y = []
        for operation in operations:
            if operation == "+":
                if len(y)==0:
                    pass
                if len(y)==1:
                    y.append(y[0])
                else:
                    y.append(y[len(y)-1] + y[len(y)-2])
            elif operation == "D":
                y.append(y[len(y)-1] * 2)
            elif operation == "C":
                y.pop()
            else:
                y.append(int(operation))
        return sum(y)

        