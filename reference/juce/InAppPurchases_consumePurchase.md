#### consumePurchase()


 void InAppPurchases::consumePurchase ( const String & productIdentifier, 
 
 const String & purchaseToken = {} ) 

Android only: asynchronously sends a request to mark a purchase with given identifier as consumed.To consume a product, provide product identifier as well as a purchase token that was generated when the product was purchased. The purchase token can also be retrieved by using getProductsInformation(). In general if it is available on hand, it is better to use it, because otherwise another async request will be sent to the store, to first retrieve the token.After successful consumption, a product will no longer be returned in getProductsBought() and it will be available for purchase.On iOS consumption happens automatically. If the product was set as consumable, this function is a noop.