#### evaluateJavascript()


 void WebBrowserComponent::evaluateJavascript ( const String & script, 
 
 EvaluationCallback callback = nullptr ) 

Evaluates the specified script in the context of the current state of the WebBrowserComponent.If the optional callback is provided it will be called with the result of the evaluation. The callback will be called on the message thread.