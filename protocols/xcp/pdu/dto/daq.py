from xcp.pdu.base import Base
from xcp.pdu.identification import Identification

class Daq(Base):
    
    def __init__(self):
        super(Daq, self).__init__(pid = 0x00)
        self.identification = Identification()
        self.data = b'' 

    def is_correct_pid(self):
        correct = False

        if 0x00 <= self.pid <= 0xFB:
            correct = True

        return correct