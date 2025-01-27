#### getUniqueDeviceID()


 static String SystemStats::getUniqueDeviceID ( ) static 
 

This method returns a machine unique ID unaffected by storage or peripheral changes.This ID will be invalidated by changes to the motherboard and CPU on nonmobile platforms, or performing a system restore on an Android device.There are some extra caveats on iOS: The returned ID is unique to the vendor part of your 'Bundle Identifier' and is stable for all associated apps. The key is invalidated once all associated apps are uninstalled. This function can return an empty string under certain conditions, for example, If the device has not been unlocked since a restart.