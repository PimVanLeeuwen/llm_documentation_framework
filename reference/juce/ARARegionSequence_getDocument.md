#### getDocument()


template<typename Document\_t = ARADocument> 

 Document\_t \* ARARegionSequence::getDocument ( ) const noexcept 
 

Returns the result of ARA::PlugIn::RegionSequence::getDocument() with the pointer cast to ARADocument\*.If you have overridden ARADocumentControllerSpecialisation::doCreateDocument(), then you can use the template parameter to cast the pointers to your subclass of ARADocument.