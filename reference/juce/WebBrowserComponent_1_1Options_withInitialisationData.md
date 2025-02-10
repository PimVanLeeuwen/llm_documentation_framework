#### withInitialisationData()


 Options WebBrowserComponent::Options::withInitialisationData ( StringRef name, const var & value ) const nodiscard 
 

Ensures that there will be a Javascript Array under `window.__JUCE__.initialisationData.name` and that it will contain the value provided here.The initialisation data is injected prior to loading any resource. Multiple values added for the same name will all be available in the Array.References name.