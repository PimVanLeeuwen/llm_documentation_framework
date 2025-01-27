#### willDeactivateAudioModificationForUndoHistory()


 virtual void ARAAudioModificationListener::willDeactivateAudioModificationForUndoHistory ( ARAAudioModification \* audioModification, bool deactivate ) virtual 
 

Called before an audio modification is activated or deactivated when being removed / added from the host's undo history.Parameters

 audioModification The audio modification that was activated or deactivated 
 
 deactivate A bool indicating whether `audioModification` was deactivated or activated.