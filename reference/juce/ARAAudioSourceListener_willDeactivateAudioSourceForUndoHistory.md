#### willDeactivateAudioSourceForUndoHistory()


 virtual void ARAAudioSourceListener::willDeactivateAudioSourceForUndoHistory ( ARAAudioSource \* audioSource, bool deactivate ) virtual 
 

Called before an audio source is activated or deactivated when being removed / added from the host's undo history.Parameters

 audioSource The audio source that will be activated or deactivated 
 
 deactivate A bool indicating whether `audioSource` was deactivated or activated.