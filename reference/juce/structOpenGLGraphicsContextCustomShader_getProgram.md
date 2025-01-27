#### getProgram()


 OpenGLShaderProgram \* OpenGLGraphicsContextCustomShader::getProgram ( LowLevelGraphicsContext & ) const 
 

Returns the program, if it has been linked and is active.This can be called when you're about to use fillRect, to set up any uniforms/textures that the program may require.