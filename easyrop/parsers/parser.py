from easyrop.parsers.xmlParser import XmlParser


class Parser:
    def __init__(self, op):
        self.__file = None

        try:
            self.__file = XmlParser(op)
        except:
            print("[Error] Can't read form gadget source")
            return None

    def get_all_ops(self):
        return self.__file.get_all_ops()

    def parse(self):
        return self.__file.parse()
