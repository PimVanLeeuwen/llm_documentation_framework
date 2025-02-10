#### restoreProductsBoughtList()


 void InAppPurchases::restoreProductsBoughtList ( bool includeDownloadInfo, 
 
 const juce::String & subscriptionsSharedSecret = {} ) 

Asynchronously asks about a list of products that a user has already bought.Upon completion, Listener::purchasesListRestored() callback will be invoked. The user may be prompted to login first.Parameters

 includeDownloadInfo (iOS only) if true, then after restoration is successful, the downloads array passed to Listener::purchasesListReceived() callback will contain all the download objects corresponding with the purchase. In the opposite case, the downloads array will be empty. 
 
 subscriptionsSharedSecret (iOS only) required when not including download information and when there are autorenewable subscription set up with this app. Refer to InAppPurchase settings in the store.