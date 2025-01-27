#### pageAboutToLoad()


 virtual bool WebBrowserComponent::pageAboutToLoad ( const String & newURL ) virtual 
 

This callback is called when the browser is about to navigate to a new location.You can override this method to perform some action when the user tries to go to a particular URL. To allow the operation to carry on, return true, or return false to stop the navigation happening.