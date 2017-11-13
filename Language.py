class Language():
    def __init__(self, type):
        self.setLang(type)

    def setLang(self, type):
        if type == 0:
            self.load_english()
        elif type == 1:
            self.load_dutch()

    def load_english(self):
        #naming: first part says what type of text it is, but is for button, lab for label, pop for popup
        #pages
        self.but_AddADevice = "Add a Device"
        self.lab_Name = "Name"
        self.lab_MinVal = "Minimum value"
        self.lab_MaxRollLength = "Max roll out length in meters"
        self.lab_PortNum = "Port number"
        self.lab_SensorType = "Sensor type"
        self.but_AddDevice = "Add Device"
        self.but_Ok = "Ok"
        self.selBox_light = "Light"
        self.selBox_temp = "Temperature"

        self.but_Manual = "Manual"
        self.but_StartRoll = "Roll out/up"
        self.but_StartRollOut = "Roll out"
        self.but_startRollUp = "Roll up"

        self.but_Graphs = "Graphs"

        self.but_Update = "update"

        self.but_Settings = "Settings"
        self.but_ChgMinVal = "Change the minimum value"

        self.but_Info = "Info"

        self.lab_Sky = "Sky: "
        self.lab_Temp = "Temp: "

        #popups
        self.pop_TitleEasterEgg = "Yes thats us!"
        self.pop_TextEasterEgg = "But seriously you need to enter a number"

        self.pop_TitleNotValidNumber = "Not a valid number"
        self.pop_TextNotValidNumber = "You have to enter a valid number!"

        self.pop_TitleDevNotAttached = "Error: No device attached"
        self.pop_TextDevNotAttached = "There is no device connected, add a device first!"

        self.pop_TitleRollOut = "Rolling Out!"
        self.pop_TextRollOut = " is rolling out"

        self.pop_TitleRollUp = "Rolling Up!"
        self.pop_TextRollUp = " is rolling "

        self.pop_TitleNotValidName = "Not a valid name!"
        self.pop_TextNotValidName = "name has to be text"

        self.pop_TitleNotValidPort = "Not a valid port!"
        self.pop_TextNotValidPort = "Port has to be COM + number"

        self.pop_TitleNoName = "Error: No name"
        self.pop_TextNoName = "New device can not be created without a name."

        self.pop_TitleDupNames = "Error: Duplicate names"
        self.pop_TextDupNames = "There already is a device with this name."

        self.pop_TitleNewDevice = "New Device"
        self.pop_TextNewDevice_1 = "Device with name: "
        self.pop_TextNewDevice_2 = " has been added!"

        self.pop_TitleNoNewDevice = "Could not add device!"
        self.pop_TextNoNewDevice = "An error has occurred"

        self.pop_TitleInfo = "Aeros Development"
        self.pop_TextInfo = "Members: Robert Monden, Michel Glazenborg, Willem Slager and Jelmer Haarman"

    def load_dutch(self):
        self.but_AddADevice = "Voeg apparaat\ntoe"
        self.lab_Name = "Naam"
        self.lab_MinVal = "Minimale waarde"
        self.lab_MaxRollLength = "Maximale uitrollengte in meters"
        self.lab_PortNum = "Poortnummer"
        self.lab_SensorType = "Sensortype"
        self.but_AddDevice = "Apparaat toevoegen"
        self.but_Ok = "Akkoord"
        self.selBox_light = "Licht"
        self.selBox_temp = "Temperatuur"

        self.but_Manual = "Handmatig"
        self.but_StartRoll = "In-/uitrollen"

        self.but_Graphs = "Grafieken"

        self.but_Update = "bijwerken"

        self.but_Settings = "Instellingen"
        self.but_ChgMinVal = "Verander minimale waarde"

        self.but_Info = "Informatie"

        self.lab_Sky = "Lucht: "
        self.lab_Temp = "Temp: "

        # popups
        self.pop_TitleEasterEgg = "Ja, dat zijn wij!"
        self.pop_TextEasterEgg = "Maar echt, je moet een nummer invullen"

        self.pop_TitleNotValidNumber = "Onjuiste invoer"
        self.pop_TextNotValidNumber = "Je dient een correct nummer in te vullen!"

        self.pop_TitleDevNotAttached = "Fout: er is geen apparaat verbonden"
        self.pop_TextDevNotAttached = "Er is geen apparaat verbonden, dus voeg er eerst een toe!"

        self.pop_TitleRollOut = "Aan het uitrollen"
        self.pop_TextRollOut = " is aan het uitrollen"

        self.pop_TitleRollUp = "Aan het oprollen!"
        self.pop_TextRollUp = " is aan het oprollen "

        self.pop_TitleNotValidName = "Onjuiste naam!"
        self.pop_TextNotValidName = "de naam dient een tekstformaat te hebben"

        self.pop_TitleNotValidPort = "Onjuist poortnummer!"
        self.pop_TextNotValidPort = "Het poortnummer dient het volgende formaat te hebben: COM + nummer"

        self.pop_TitleNoName = "Fout: geen naam"
        self.pop_TextNoName = "Er kunnen geen apparaten zonder naam toegevoegd worden."

        self.pop_TitleDupNames = "Fout: naam al in gebruik"
        self.pop_TextDupNames = "De gekozen naam wordt al gebruikt voor een ander apparaat."

        self.pop_TitleNewDevice = "Nieuw apparaat"
        self.pop_TextNewDevice_1 = "Apparaat met naam: "
        self.pop_TextNewDevice_2 = " is toegevoegd!"

        self.pop_TitleNoNewDevice = "Er is een fout opgetreden"
        self.pop_TextNoNewDevice = "Het apparaat kon, om onbekende reden, niet toegevoegd worden"

        self.pop_TitleInfo = "Aeros Development"
        self.pop_TextInfo = "Teamleden: Robert Monden, Michel Glazenborg, Willem Slager en Jelmer Haarman"
