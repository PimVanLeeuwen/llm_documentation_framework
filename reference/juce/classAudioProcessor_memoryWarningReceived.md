#### memoryWarningReceived()


 virtual void AudioProcessor::memoryWarningReceived ( ) virtual 
 

Called by the host to indicate that you should reduce your memory footprint.You should override this method to free up some memory gracefully, if possible, otherwise the host may forcibly unload your AudioProcessor.At the moment this method is only called when your AudioProcessor is an AUv3 plugin running on iOS.References jassertfalse.