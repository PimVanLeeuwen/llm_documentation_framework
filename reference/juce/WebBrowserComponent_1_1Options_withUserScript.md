#### withUserScript()


 Options WebBrowserComponent::Options::withUserScript ( StringRef script ) const nodiscard 
 

Adds a Javascript code that will be evaluated before any other resource is loaded but after the JUCE backend definitions become available, hence the specified script can rely on the presence of `window.__JUCE__.backend`.This script will be evaluated after all goToUrl() calls.