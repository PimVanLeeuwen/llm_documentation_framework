#### generateKeyFile()


 static String JUCE\_CALLTYPE KeyGeneration::generateKeyFile ( const String & appName, const String & userEmail, const String & userName, const String & machineNumbers, const RSAKey & privateKey ) static 
 

Generates the content of a keyfile which can be sent to a user's machine to unlock a product.The returned value is a block of text containing an RSAencoded block, followed by some humanreadable details. If you pass this block of text to OnlineUnlockStatus::applyKeyFile(), it will decrypt it, and if the key matches and the machine numbers match, it will unlock that machine.Typically the way you'd use this on a server would be to build a small executable that simply calls this method and prints the result, so that the webserver can use this as a reply to the product's autoregistration mechanism. The keyGenerationAppMain() function is an example of how to build such a function.See alsoOnlineUnlockStatus