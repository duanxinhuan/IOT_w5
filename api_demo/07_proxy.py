# Reference: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_proxy.htm
import time

class Image:
    def __init__(self, filename):
        self._filename = filename

    def load_image_from_disk(self):
        print("Loading... " + self._filename + "... ", end = "", flush = True)
        time.sleep(3)
        print("Done.")

    def display_image(self):
        self.load_image_from_disk()
        print("Display " + self._filename)

class Proxy:
    def __init__(self, subject):
        self._subject = subject
        self._proxystate = None

class ProxyImage(Proxy):
    def display_image(self):
        if(self._proxystate == None):
            self._subject.load_image_from_disk()
            self._proxystate = 1
        print("Display " + self._subject._filename)

image1 = Image("HiRes_10Mb_Photo1")
image1.display_image()
image1.display_image()
image1.display_image()

print("---")

proxy_image1 = ProxyImage(Image("HiRes_10Mb_Photo1"))
proxy_image2 = ProxyImage(Image("HiRes_50Mb_Photo2"))

proxy_image1.display_image() # Loading necessary.
proxy_image1.display_image() # Loading unnecessary.
proxy_image2.display_image() # Loading necessary.
proxy_image2.display_image() # Loading unnecessary.
proxy_image2.display_image() # Loading unnecessary.
proxy_image1.display_image() # Loading unnecessary.
