#### emitEventIfBrowserIsVisible()


 void WebBrowserComponent::emitEventIfBrowserIsVisible ( const Identifier & eventId, 
 
 const var & object ) 

Emits an object on the frontend under the specified eventId.Ids beginning with `__juce` are reserved for the framework implementation.Example for listening to such events on the frontend:// Subscribing
const removalToken = window.\_\_JUCE\_\_.backend.addEventListener(eventId, (objectFromBackend) => {
 console.log(objectFromBackend.message);
});
 
// Unsubscribing
window.\_\_JUCE\_\_.backend.removeEventListener(removalToken);
AccessibilityRole::window@ window