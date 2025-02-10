#### getChild()


 virtual ARAObject \* ARAObject::getChild ( size\_t index ) pure virtual 
 

Returns the child object associated with the given index.The index should be smaller than the value returned by getNumChildren().Note that the index of a particular object may change when the ARA model graph is edited.Implemented in ARAAudioModification, ARAAudioSource, ARADocument, ARAMusicalContext, ARAPlaybackRegion, and ARARegionSequence.Referenced by traverse().