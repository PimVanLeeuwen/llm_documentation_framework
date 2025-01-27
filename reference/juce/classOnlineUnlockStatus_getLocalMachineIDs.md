#### getLocalMachineIDs()


 virtual StringArray OnlineUnlockStatus::getLocalMachineIDs ( ) virtual 
 

Returns a list of strings, any of which should be unique to this physical computer.When testing whether the user is allowed to use the product on this machine, this list of tokens is compared to the ones that were stored on the webserver.The default implementation of this method will simply call MachineIDUtilities::getLocalMachineIDs(), which provides a default version of this functionality.