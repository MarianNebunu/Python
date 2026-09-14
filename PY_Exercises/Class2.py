class Device:
    def __init__(self, name, connected_by): 
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    def __str__(self):
        return  f"Device {self.name!r} ({self.connected_by})"
    def disconnect(self):
        self.connected = False
        print("Disconnected.")
    def connect(self):
        self.connected = True
        print("Connected.")    
        
MyPC = Device("My PC", "USB")   
MyPC.disconnect()   
print(MyPC.connected)
MyPC.connect()
print(MyPC.connected)