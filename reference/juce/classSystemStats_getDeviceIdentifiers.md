#### getDeviceIdentifiers()


 static StringArray SystemStats::getDeviceIdentifiers ( ) static 
 

This method calculates some IDs to uniquely identify the device.The first choice for an ID is a filesystem ID for the user's home folder or windows directory. If that fails then this function returns the MAC addresses.