#### generateExpiringKeyFile()


 static String JUCE\_CALLTYPE KeyGeneration::generateExpiringKeyFile ( const String & appName, const String & userEmail, const String & userName, const String & machineNumbers, const Time expiryTime, const RSAKey & privateKey ) static 
 

Similar to the above key file generation method but with an expiry time.You must supply a Time after which this key file should no longer be considered as active.N.B. when an app is unlocked with an expiring key file, OnlineUnlockStatus::isUnlocked will still return false. You must then check OnlineUnlockStatus::getExpiryTime to see if this expiring key file is still in date and act accordingly.See alsoOnlineUnlockStatus