class DoublyNode:
    def __init__(self, val: str, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
      self.firstPage = DoublyNode("")
      self.lastPage = DoublyNode("")
      self.currentPage = DoublyNode(homepage) 

      self.firstPage.next = self.currentPage
      self.currentPage.prev = self.firstPage

      self.currentPage.next = self.lastPage
      self.lastPage.prev = self.currentPage
      

    def visit(self, url: str) -> None:
        newPage = DoublyNode(url)

        curr_page = self.currentPage

        curr_page.next = newPage
        newPage.prev = curr_page

        newPage.next = self.lastPage
        self.lastPage.prev = newPage

        self.currentPage = newPage
        

    def back(self, steps: int) -> str:
        cur_page = self.currentPage
        for _ in range(steps):
            if cur_page.prev == self.firstPage:
                break
            cur_page = cur_page.prev
        self.currentPage = cur_page
        return cur_page.val

    def forward(self, steps: int) -> str:
        cur_page = self.currentPage
        for _ in range(steps):
            if cur_page.next == self.lastPage:
                break
            cur_page = cur_page.next
        self.currentPage = cur_page
        return cur_page.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)