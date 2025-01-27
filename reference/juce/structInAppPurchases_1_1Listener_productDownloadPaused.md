#### productDownloadPaused()


 virtual void InAppPurchases::Listener::productDownloadPaused ( Download & ) virtual 
 

iOS only: Called when a product download is paused.This may also be called after the application starts, if the download was in a paused state and the application was closed before finishing the download.Only after the download is finished successfully or cancelled you will stop receiving this callback on startup.