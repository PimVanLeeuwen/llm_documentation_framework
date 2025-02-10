#### sendFullSyncCallback()


 void ValueTreeSynchroniser::sendFullSyncCallback ( ) 
 

Forces the sending of a full state message, which may be large, as it encodes the entire ValueTree.This will internally invoke stateChanged() with the encoded version of the state.