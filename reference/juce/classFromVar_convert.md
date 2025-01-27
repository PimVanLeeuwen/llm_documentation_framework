#### convert()


template<typename T > 

 static std::optional< T > FromVar::convert ( const var & v ) static 
 

Attempts to convert a var to an instance of type T.This will return a nonnull optional if conversion succeeds, or nullopt if conversion fails.Referenced by StrictVariantConverter< Type >::fromVar().