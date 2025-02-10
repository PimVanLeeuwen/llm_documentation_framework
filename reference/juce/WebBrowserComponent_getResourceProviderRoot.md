#### getResourceProviderRoot()


 static const String & WebBrowserComponent::getResourceProviderRoot ( ) static 
 

Returns a platform specific string that represents the root address for resources served by the ResourceProvider.If you pass this value to goToURL the ResourceProvider will receive a request with the "/" path parameter. In response to this request the provider may typically want to return the contents of the "index.html" file.See alsoResourceProvider, Options::withResourceProvider, goToURL