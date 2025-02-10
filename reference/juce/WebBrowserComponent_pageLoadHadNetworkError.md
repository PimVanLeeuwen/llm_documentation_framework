#### pageLoadHadNetworkError()


 virtual bool WebBrowserComponent::pageLoadHadNetworkError ( const String & errorInfo ) virtual 
 

This callback happens when a network error was encountered while trying to load a page.You can override this method to show some other error page by calling goToURL. Return true to allow the browser to carry on to the internal browser error page.The errorInfo contains some platform dependent string describing the error.Calling goToURL() inside this callback can encounter further network errors, potentially causing an infinite loop.