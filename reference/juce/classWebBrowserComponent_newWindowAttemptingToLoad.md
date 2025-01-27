#### newWindowAttemptingToLoad()


 virtual void WebBrowserComponent::newWindowAttemptingToLoad ( const String & newURL ) virtual 
 

This callback occurs when the browser attempts to load a URL in a new window.This won't actually load the window but gives you a chance to either launch a new window yourself or just load the URL into the current window with goToURL().