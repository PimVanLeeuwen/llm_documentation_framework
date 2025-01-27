#### audioProcessorChanged()


 virtual void AudioProcessorListener::audioProcessorChanged ( AudioProcessor \* processor, const ChangeDetails & details ) pure virtual 
 

Called to indicate that something else in the plugin has changed, like its program, number of parameters, etc.IMPORTANT NOTE: This will be called synchronously, and many audio processors will call it during their audio callback. This means that not only has your handler code got to be completely threadsafe, but it's also got to be VERY fast, and avoid blocking. If you need to handle this event on your message thread, use this callback to trigger an AsyncUpdater or ChangeBroadcaster which you can respond to later on the message thread.