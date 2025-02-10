#### parameterValueChanged()


 virtual void AudioProcessorParameter::Listener::parameterValueChanged ( int parameterIndex, float newValue ) pure virtual 
 

Receives a callback when a parameter has been changed.IMPORTANT NOTE: This will be called synchronously when a parameter changes, and many audio processors will change their parameter during their audio callback. This means that not only has your handler code got to be completely threadsafe, but it's also got to be VERY fast, and avoid blocking. If you need to handle this event on your message thread, use this callback to trigger an AsyncUpdater or ChangeBroadcaster which you can respond to on the message thread.