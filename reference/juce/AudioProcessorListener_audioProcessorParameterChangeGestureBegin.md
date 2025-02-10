#### audioProcessorParameterChangeGestureBegin()


 virtual void AudioProcessorListener::audioProcessorParameterChangeGestureBegin ( AudioProcessor \* processor, int parameterIndex ) virtual 
 

Indicates that a parameter change gesture has started.E.g. if the user is dragging a slider, this would be called when they first press the mouse button, and audioProcessorParameterChangeGestureEnd would be called when they release it.IMPORTANT NOTE: This will be called synchronously, and many audio processors will call it during their audio callback. This means that not only has your handler code got to be completely threadsafe, but it's also got to be VERY fast, and avoid blocking. If you need to handle this event on your message thread, use this callback to trigger an AsyncUpdater or ChangeBroadcaster which you can respond to later on the message thread.See alsoaudioProcessorParameterChangeGestureEnd