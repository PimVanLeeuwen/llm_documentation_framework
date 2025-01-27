#### applyKeyFile()


 Result OnlineUnlockStatus::applyKeyFile ( const String & keyFileContent ) 
 

Attempts to perform an unlock using a block of keyfile data provided.You may wish to use this as a way of allowing a user to unlock your app by draganddropping a file containing the key data, or by letting them select such a file. This is often needed for allowing registration on machines without internet access.You can find the possible string values Result can return in LicenseResult.