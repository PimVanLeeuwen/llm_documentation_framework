#### open()


 static bool BluetoothMidiDevicePairingDialogue::open ( ModalComponentManager::Callback \* exitCallback = nullptr, Rectangle< int > \* btWindowBounds = nullptr ) static 
 

Opens the Bluetooth MIDI pairing dialogue, if it is available.Parameters

 exitCallback A callback which will be called when the modal bluetooth dialog is closed. 
 
 btWindowBounds The bounds of the bluetooth window that will be opened. The dialog itself is opened by the OS so cannot be customised by JUCE. 



Returnstrue if the dialogue was opened, false on error.
See alsoModalComponentManager::Callback