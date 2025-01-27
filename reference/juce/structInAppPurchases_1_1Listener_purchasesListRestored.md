#### purchasesListRestored()


 virtual void InAppPurchases::Listener::purchasesListRestored ( const Array< PurchaseInfo > & , bool , const String & ) virtual 
 

Called when a list of all purchases is restored.This can be used to figure out to which products a user is entitled.NOTE: It is possible to receive this callback for the same purchase multiple times. If that happens, only the newest set of downloads and the newest orderId will be valid, the old ones should be not used anymore!