import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class TesterPresent(ServiceBase):
    """
    Service that allows to keep session alive on ECU. 
    Some timeouts can be included on ECU's session that will kick-off user 
    from current session. Sending tester present regularly avoid being kicked.
    """

    def __init__(self, sub_function = 0x80):
        self.service_id   = ServiceID.TESTER_PRESENT
        self.sub_function = sub_function
        
    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1]: Service ID (0X3E)
        [1:2]: Sub function
        """
        b = bytearray()

        b.extend(super(TesterPresent, self).__bytes__())
        b.extend(self.sub_function)

        return b