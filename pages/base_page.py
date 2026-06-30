class BasePage:

    def __init__(self,page):
     self.page=page

    def open(self,url):
     self.page.goto(url)

    def refresh(self):
     self.page.reload()

    def back(self):
     self.page.go_back()

    def forward(self):
     self.page.go_forward()

    def get_title(self):
     return self.page.title()