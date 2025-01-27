#### productPurchaseFinished()


 virtual void InAppPurchases::Listener::productPurchaseFinished ( const PurchaseInfo & , bool , const String & ) virtual 
 

Called whenever a purchase is complete, with additional state whether the purchase completed successfully.For hosted content (iOS only), the downloads array within PurchaseInfo will contain all download objects corresponding with the purchase. For nonhosted content, the downloads array will be empty.InAppPurchases class will own downloads and will delete them as soon as they are finished.NOTE: It is possible to receive this callback for the same purchase multiple times. If that happens, only the newest set of downloads and the newest orderId will be valid, the old ones should be not used anymore!