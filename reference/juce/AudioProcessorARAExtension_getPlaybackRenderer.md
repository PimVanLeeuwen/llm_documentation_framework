#### getPlaybackRenderer()


template<typename PlaybackRenderer\_t = ARAPlaybackRenderer> 

 PlaybackRenderer\_t \* AudioProcessorARAExtension::getPlaybackRenderer ( ) const noexcept 
 

Returns the result of ARA::PlugIn::PlugInExtension::getPlaybackRenderer() with the pointer cast to ARAPlaybackRenderer\*.If you have overridden ARADocumentControllerSpecialisation::doCreatePlaybackRenderer(), then you can use the template parameter to cast the pointers to your subclass of ARAPlaybackRenderer.