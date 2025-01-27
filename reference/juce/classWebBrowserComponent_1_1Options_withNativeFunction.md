#### withNativeFunction()


 Options WebBrowserComponent::Options::withNativeFunction ( const Identifier & name, NativeFunction callback ) const nodiscard 
 

Registers a NativeFunction under the given name.To call this function from the frontend, you can import the JUCE frontend helper module or issue a call to the lowlevel frontend API.The callback is always called on the message thread.import { getNativeFunction } from "./juce";
 
function someJavascriptFunction() {
 const myBackendFunction = getNativeFunction("myBackendFunction");
 myBackendFunction (1, 2, "some string");
}
References jassert, and name.