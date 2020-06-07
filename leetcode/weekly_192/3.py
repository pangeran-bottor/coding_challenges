# https://leetcode.com/contest/weekly-contest-192/problems/design-browser-history/


class BrowserHistory:
    def __init__(self, homepage: str):
        self.hist_left = []
        self.hist_right = []
        self.cur = homepage
        

    def visit(self, url: str) -> None:
        self.hist_left.append(self.cur)
        self.cur = url
        self.hist_right = []
        

    def back(self, steps: int) -> str:
        valid_back = min(steps, len(self.hist_left))
        while valid_back > 0:
            self.hist_right.append(self.cur)
            self.cur = self.hist_left.pop()
            valid_back -= 1
        return self.cur
        
    def forward(self, steps: int) -> str:
        valid_forward = min(steps, len(self.hist_right))
        while valid_forward > 0:
            self.hist_left.append(self.cur)
            self.cur = self.hist_right.pop()
            valid_forward -= 1
        return self.cur
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
