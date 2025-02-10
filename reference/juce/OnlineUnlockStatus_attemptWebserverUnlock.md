#### attemptWebserverUnlock()


 UnlockResult OnlineUnlockStatus::attemptWebserverUnlock ( const String & email, 
 
 const String & password ) 

Contacts the webserver and attempts to perform a registration with the given user details.The return value will either be a success, or a failure with an error message from the server, so you should show this message to your user.Because this method blocks while it contacts the server, you must run it on a background thread, not on the message thread. For an easier way to create a GUI to do the unlocking, see OnlineUnlockForm.