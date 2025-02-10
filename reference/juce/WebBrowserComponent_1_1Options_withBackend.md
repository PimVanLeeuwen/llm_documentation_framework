#### withBackend()


 Options WebBrowserComponent::Options::withBackend ( Backend backend ) const nodiscard 
 

Use a particular backend to create the WebViewBrowserComponent.JUCE will silently fallback to the default backend if the selected backend is not supported. To check if a specific backend is supported on your platform or not, use WebBrowserComponent::areOptionsSupported.References withMember().