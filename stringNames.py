
class stringNames():
    info_title = ""
    info_text = ""

    def __init__(self):
        self.setInfoText("Aeros dev is cool.", "Like really, really cool")

    def setInfoText(self,title, text):
        self.info_title = title
        self.info_text = text

    def getInfoText(self):
        return self.info_title + ";" + self.info_text
