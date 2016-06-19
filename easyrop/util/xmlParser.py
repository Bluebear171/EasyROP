import xml.etree.ElementTree
import os

from easyrop.operation import Operation
from easyrop.set import Set
from easyrop.instruction import Instruction


class XmlParser:
    def __init__(self, op):
        path = os.getcwd() + '\easyrop\gadgets\\turingOP.xml'
        self.__file = xml.etree.ElementTree.parse(path).getroot()
        self.__op = op

    def parse(self):
        __operation = Operation(self.__op)
        for operation in self.__file.findall('operation'):
            if operation.get('name') == self.__op:
                for set in operation.iter('set'):
                    s = Set()
                    for ins in set.iter('ins'):
                        i = Instruction(ins.get('mnemonic'), ins.find('src'), ins.find('dst'))
                        s.addIntruction(i)
                    __operation.addSet(s)
        return __operation
