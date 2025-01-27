#### withUserDataFolder()


 WinWebView2 WebBrowserComponent::Options::WinWebView2::withUserDataFolder ( const File & folder ) const nodiscard 
 

Sets a nondefault location for storing user data for the browser instance.In plugin projects you may find it necessary to use this option and specify a location such as File::SpecialLocationType::tempDirectory. Otherwise WebView2 may function incorrectly due to being denied access to the default user data location.References withMember().