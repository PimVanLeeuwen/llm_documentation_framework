#### addFileIDToList()


 static bool OnlineUnlockStatus::MachineIDUtilities::addFileIDToList ( StringArray & result, const File & file ) static 
 

Utility function that you may want to use in your machineID generation code.This adds an ID string to the given array which is a hash of the filesystem ID of the given file.