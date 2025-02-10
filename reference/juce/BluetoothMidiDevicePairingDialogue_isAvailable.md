#### isAvailable()


 static bool BluetoothMidiDevicePairingDialogue::isAvailable ( ) static 
 

Checks if a Bluetooth MIDI pairing dialogue is available on this platform.On iOS, this will be true for iOS versions 8.0 and higher.On Android, this will be true only for Android SDK versions 23 and higher, and additionally only if the device itself supports MIDI over Bluetooth.On desktop platforms, this will typically be false as the bluetooth pairing is not done inside the app but by other means.Returnstrue if the Bluetooth MIDI pairing dialogue is available, false otherwise.