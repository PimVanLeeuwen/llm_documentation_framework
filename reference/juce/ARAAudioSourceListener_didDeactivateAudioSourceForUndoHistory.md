#### didDeactivateAudioSourceForUndoHistory()


 virtual void ARAAudioSourceListener::didDeactivateAudioSourceForUndoHistory ( ARAAudioSource \* audioSource, bool deactivate ) virtual 
 

Called after an audio source is activated or deactivated when being removed / added from the host's undo history.Parameters

 audioSource The audio source that was activated or deactivated 
 
 deactivate A bool indicating whether `audioSource` was deactivated or activated.