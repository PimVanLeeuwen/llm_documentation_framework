#### setTextureMagnificationFilter()


 void OpenGLContext::setTextureMagnificationFilter ( TextureMagnificationFilter magFilterMode ) noexcept 
 

Sets the texture magnification filter.By default the texture magnification filter is linear. However, for faster rendering you may want to use the 'nearest' magnification filter. This option will not affect any textures created before this function was called.