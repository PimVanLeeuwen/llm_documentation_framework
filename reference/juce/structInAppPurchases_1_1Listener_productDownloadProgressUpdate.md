#### productDownloadProgressUpdate()


 virtual void InAppPurchases::Listener::productDownloadProgressUpdate ( Download & , float , RelativeTime ) virtual 
 

iOS only: Called when a product download progress gets updated.If the download was interrupted in the last application session, this callback may be called after the application starts.If the download was in progress and the application was closed, the download may happily continue in the background by OS. If you open the app and the download is still in progress, you will receive this callback. If the download finishes in the background before you start the app again, you will receive productDownloadFinished callback instead. The download will only stop when it is explicitly cancelled or when it is finished.