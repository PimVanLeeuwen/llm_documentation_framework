#### getMusicalContexts()


template<typename MusicalContext\_t = ARAMusicalContext> 

 const std::vector< MusicalContext\_t \* > & ARADocument::getMusicalContexts ( ) const noexcept 
 

Returns the result of ARA::PlugIn::Document::getMusicalContexts() with the pointers within cast to ARAMusicalContext\*.If you have overridden ARADocumentControllerSpecialisation::doCreateMusicalContext(), then you can use the template parameter to cast the pointers to your subclass of ARAMusicalContext.