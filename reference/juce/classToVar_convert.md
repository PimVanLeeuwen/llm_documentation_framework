#### convert()


template<typename T > 

 static std::optional< var > ToVar::convert ( const T & t, const Options & options = {} ) static 
 

Attempts to convert the argument to a var using the serialisation utilities specified for that type.This will return a nonnull optional if conversion succeeds, or nullopt if conversion fails.Referenced by StrictVariantConverter< Type >::toVar().