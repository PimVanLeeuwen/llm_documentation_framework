#### getRegionSequences()


template<typename RegionSequence\_t = ARARegionSequence> 

 const std::vector< RegionSequence\_t \* > & ARADocument::getRegionSequences ( ) const noexcept 
 

Returns the result of ARA::PlugIn::Document::getRegionSequences() with the pointers within cast to ARARegionSequence\*.If you have overridden ARADocumentControllerSpecialisation::doCreateRegionSequence(), then you can use the template parameter to cast the pointers to your subclass of ARARegionSequence.