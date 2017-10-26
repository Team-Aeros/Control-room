
class stringNames():
    info_title = ""
    info_text = ""

    manual_title = ""
    manual_text = ""

    settings_title = ""
    settings_text_light = ""
    settings_text_temp = ""

    def setInfoText(self,title, text):
        self.info_title = title
        self.info_text = text

    def getInfoText(self):
        return self.info_title + ";" + self.info_text

    def setManualText(self, title, text):
        self.manual_title = title
        self.manual_text = text

    def getManualText(self):
        return self.manual_title + ";" + self.manual_text

    def setSettingsText(self, title, light, temp):
        self.settings_title = title
        self.settings_text_light = light
        self.settings_text_temp = temp

    def getSettingsText(self):
        return self.settings_title + ";" + self.settings_text_light + ";" + self.settings_text_temp
