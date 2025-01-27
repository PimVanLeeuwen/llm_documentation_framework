#### withNativeIntegrationEnabled()


 Options WebBrowserComponent::Options::withNativeIntegrationEnabled ( bool enabled = true ) const nodiscard 
 

Enables native integration features for the code running inside the WebBrowserComponent.This injects data and function objects under `window.__JUCE__.backend` through which scripts running in the WebBrowserComponent can send events to the backend and call registered native functions.You should only enable native integrations if you have full control over the content loaded into the component. Navigating to 3rd party websites with these integrations enabled may expose the application and the computer to security risks.See alsowithNativeFunction, withEventListener References withMember().