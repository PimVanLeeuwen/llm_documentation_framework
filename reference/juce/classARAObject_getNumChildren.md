#### getNumChildren()


 virtual size\_t ARAObject::getNumChildren ( ) const pure virtualnoexcept 
 

Returns the number of ARA model objects aggregated by this object.Objects that are merely referred to, but not aggregated by the current object are not included in this count, e.g. a referenced RegionSequence does not count as a child of the referring PlaybackRegion.See the ARA documentation's ARA Model Graph Overview for more details.Implemented in ARAAudioModification, ARAAudioSource, ARADocument, ARAMusicalContext, ARAPlaybackRegion, and ARARegionSequence.Referenced by traverse().