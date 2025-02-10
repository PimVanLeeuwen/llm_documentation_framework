#### withExtraHeaders()


 WebInputStream & WebInputStream::withExtraHeaders ( const String & extraHeaders ) 
 

Add extra headers to the HTTP request.Returns a reference to itself so that several methods can be chained.Parameters

 extraHeaders this string is appended onto the headers that are used for the request. It must therefore be a valid set of HTML header directives, separated by newlines.