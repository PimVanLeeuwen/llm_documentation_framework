#### getMusicalContext()


template<typename MusicalContext\_t = ARAMusicalContext> 

 MusicalContext\_t \* ARARegionSequence::getMusicalContext ( ) const noexcept 
 

Returns the result of ARA::PlugIn::RegionSequence::getMusicalContext() with the pointer cast to ARAMusicalContext\*.If you have overridden ARADocumentControllerSpecialisation::doCreateMusicalContext(), then you can use the template parameter to cast the pointers to your subclass of ARAMusicalContext.