# a file describing basic data sources
# a data source provides some kind of information - position, car status, wind
# weather. it may have parameters, or it may just output raw data.
from qtpy.QtCore import QObject
from qtpy.QtSerialPort import QSerialPort, QSerialPortInfo
class XBeeDataSource:
    pass


class TekScopeSocket:
    pass


class TekMeterSocket:
    pass


class BKLoadSocket(QObject):
    def __init__(self, device: str):
        self.serial = QSerialPort()
        self.serial.setPort()

