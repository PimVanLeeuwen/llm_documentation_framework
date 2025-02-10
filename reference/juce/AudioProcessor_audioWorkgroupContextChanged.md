#### audioWorkgroupContextChanged()


 virtual void AudioProcessor::audioWorkgroupContextChanged ( const AudioWorkgroup & workgroup ) virtual 
 

This is called by the host when the thread workgroup context has changed.This will only be called on the audio thread, so you can join the audio workgroup in your implementation of this function.You can use this workgroup id to synchronise any realtime threads you have. Note: This is currently only called on Apple devices.