#### getURLResult()


 URL FileChooser::getURLResult ( ) const 
 

Returns the last document that was chosen by one of the browseFor methods.Use this method if you are using the FileChooser on a mobile platform which may return a URL to a remote document. If a local file is chosen then you can convert this file to a JUCE File class via the URL::getLocalFile method.Note: On iOS you must use the returned URL object directly (you are also allowed to copy or moveconstruct another URL from the returned URL), rather than just storing the path as a String and then creating a new URL from that String. This is because the returned URL contains internally a security bookmark that is required to access the files pointed by it. Then, once you stop dealing with the file pointed by the URL, you should dispose that URL object, so that the security bookmark can be released by the system (only a limited number of such URLs is allowed).See alsogetResult, URL::getLocalFile