#### setValue()


 virtual void AudioProcessorParameter::setValue ( float newValue ) pure virtual 
 

The host will call this method to change the value of a parameter.The host may call this at any time, including during the audio processing callback, so your implementation has to process this very efficiently and avoid any kind of locking.If you want to set the value of a parameter internally, e.g. from your editor component, then don't call this directly instead, use the setValueNotifyingHost() method, which will also send a message to the host telling it about the change. If the message isn't sent, the host won't be able to automate your parameters properly.The value passed will be between 0 and 1.0.