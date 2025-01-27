#### goToURL()


 void WebBrowserComponent::goToURL ( const String & url, 
 
 const StringArray \* headers = nullptr, 
 const MemoryBlock \* postData = nullptr ) 

Sends the browser to a particular URL.Parameters

 url the URL to go to. 
 
 headers an optional set of parameters to put in the HTTP header. If you supply this, it should be a set of string in the form "HeaderKey: HeaderValue" 
 postData an optional block of data that will be attached to the HTTP POST request