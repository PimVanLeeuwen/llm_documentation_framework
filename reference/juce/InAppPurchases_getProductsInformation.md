#### getProductsInformation()


 void InAppPurchases::getProductsInformation ( const StringArray & productIdentifiers ) 
 

Asynchronously requests information for products with given ids.Upon completion, for each enquired product there is going to be a corresponding Product object. If there is no information available for the given product identifier, it will be ignored.