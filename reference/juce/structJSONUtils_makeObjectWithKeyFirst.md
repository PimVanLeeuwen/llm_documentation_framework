#### makeObjectWithKeyFirst()


 static var JSONUtils::makeObjectWithKeyFirst ( const std::map< Identifier, var > & source, Identifier key ) static 
 

Converts the provided key/value pairs into a JSON object with the provided key at the first position in the object.This is useful because the MIDICI spec requires that certain fields (e.g. status) should be placed at the beginning of a MIDICI header.