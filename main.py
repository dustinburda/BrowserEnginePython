
from url import *
from browser import *

WIDTH: int = 800
HEIGHT: int = 600

if __name__ == "__main__":
    # my_url = URL.new_url("https://browser.engineering/examples/example1-simple.html")
    my_url = URL.new_url("http://example.org")
    # my_url = URL.new_url("https://browser.engineering/examples/xiyouji.html")

    my_browser = Browser()
    my_browser.load(my_url)





    tk.mainloop()
