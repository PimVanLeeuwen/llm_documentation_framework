#### withResourceProvider()


 Options WebBrowserComponent::Options::withResourceProvider ( ResourceProvider provider, std::optional< String > allowedOriginIn = std::nullopt ) const nodiscard 
 

Sets a ResourceProvider object that can complete WebView resource requests and return data without having to issue a network operation.Requests sent to WebBrowserComponent::getResourceProviderRoot() + "resource.path" will invoke the provider with the path "/resource.path".If you call WebBrowserComponent::goToURL with the value returned by WebBrowserComponent::getResourceProviderRoot, your resource provider will receive a request for the resource "/" for which you will typically want to return the contents of your index.html.You can also specify an optional allowedOriginIn parameter that will make your ResourceProvider available to scripts loaded from that origin. E.g. if you specify "http://localhost:3000", then a script loaded from such a local development server will be able to access resources such as getResourceProviderRoot() + "live\_data.bin".Allowing external origins is handy for development, but is a potential security risk in publicly released binaries.References withMember().