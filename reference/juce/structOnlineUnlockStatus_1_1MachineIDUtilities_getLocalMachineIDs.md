#### getLocalMachineIDs()


 static StringArray OnlineUnlockStatus::MachineIDUtilities::getLocalMachineIDs ( ) static 
 

This method calculates some machine IDs based on things like network MAC addresses, harddisk IDs, etc, but if you want, you can overload it to generate your own list of IDs.The IDs that are returned should be short alphanumeric strings without any punctuation characters. Since users may need to type them, case is ignored when comparing them.Note that the first item in the list is considered to be the "main" ID, and this will be the one that is displayed to the user and registered with the marketplace webserver. Subsequent IDs are just used as fallback to avoid false negatives when checking for registration on machines which have had hardware added/removed since the product was first registered.