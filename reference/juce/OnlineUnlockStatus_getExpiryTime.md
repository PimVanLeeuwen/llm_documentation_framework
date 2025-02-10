#### getExpiryTime()


 Time OnlineUnlockStatus::getExpiryTime ( ) const 
 

Returns the Time when the keyfile expires.If a the key file obtained has an expiry time, isUnlocked will return false and this will return a nonzero time. The interpretation of this is up to your app but could be used for subscription based models or trial periods.