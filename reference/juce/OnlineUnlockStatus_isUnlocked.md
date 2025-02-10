#### isUnlocked()


 var OnlineUnlockStatus::isUnlocked ( ) const 
 

Returns true if the product has been successfully authorised for this machine.The reason it returns a variant rather than a bool is just to make it marginally more tedious for crackers to work around. Hopefully if this method gets inlined they'll need to hack all the places where you call it, rather than just the function itself.Bear in mind that each place where you check this return value will need to be changed by a cracker in order to unlock your app, so the more places you call this method, the more hassle it will be for them to find and crack them all.