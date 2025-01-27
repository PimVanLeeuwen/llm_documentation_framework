#### withDisabledAcceptsFirstMouse()


 AppleWkWebView WebBrowserComponent::Options::AppleWkWebView::withDisabledAcceptsFirstMouse ( ) const nodiscard 
 

If this options is specified, the underlying WebView will return NO from its acceptsFirstMouse method.This disables the clickthrough behaviour, meaning that clicking a previously unfocused application window only makes the window focused, but will not pass on the click to whichever control inside the WebView is under the mouse.References withMember().