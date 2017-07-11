# keypoints: if we pop the min element, then how to find sub-min element
# using auxiliary stack


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # using tuple to store (x, cur_min)
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.getMin()
        if cur_min is None or x < cur_min:
            cur_min = x
        self.data.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        if len(self.data) > 0:
            self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.data) > 0:
            return self.data[-1][0]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.data) > 0:
            return self.data[-1][1]
        return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()