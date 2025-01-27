#### make()


 static MidiDeviceListConnection MidiDeviceListConnection::make ( std::function< void()> ) static 
 

Registers a function to be called whenever the midi device list changes.The callback will only be active for as long as the return MidiDeviceListConnection remains alive. To stop receiving device change notifications, destroy the Connection object, e.g. by allowing it to fall out of scope.