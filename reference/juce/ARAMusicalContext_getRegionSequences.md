#### getRegionSequences()


template<typename RegionSequence\_t = ARARegionSequence> 

 const std::vector< RegionSequence\_t \* > & ARAMusicalContext::getRegionSequences ( ) const noexcept 
 

Returns the result of ARA::PlugIn::MusicalContext::getRegionSequences() with the pointers within cast to ARARegionSequence\*.If you have overridden ARADocumentControllerSpecialisation::doCreateRegionSequence(), then you can use the template parameter to cast the pointers to your subclass of ARARegionSequence.