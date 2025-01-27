#### createWithoutParsing()


 static URL URL::createWithoutParsing ( const String & url ) static 
 

Returns a URL without attempting to remove any embedded parameters from the string.This may be necessary if you need to create a request that involves both POST parameters and parameters which are embedded in the URL address itself.