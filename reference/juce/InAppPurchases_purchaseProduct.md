#### purchaseProduct()


 void InAppPurchases::purchaseProduct ( const String & productIdentifier, 
 
 const String & upgradeOrDowngradeFromSubscriptionWithProductIdentifier = {}, 
 bool creditForUnusedSubscription = true ) 

Asynchronously requests to buy a product with given id.Parameters

 productIdentifier The product identifier. 
 
 upgradeOrDowngradeFromSubscriptionWithProductIdentifier (Android only) specifies the subscription that will be replaced by the one being purchased now. Used only when buying a subscription that is an upgrade or downgrade from another. 
 creditForUnusedSubscription (Android only) controls whether a user should be credited for any unused subscription time on the product that is being upgraded or downgraded.