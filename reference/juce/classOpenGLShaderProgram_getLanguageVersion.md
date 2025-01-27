#### getLanguageVersion()


 static double OpenGLShaderProgram::getLanguageVersion ( ) static 
 

Returns the version of GLSL that the current context supports.E.g.if (OpenGLShaderProgram::getLanguageVersion() > 1.199)
{
 // ..do something that requires GLSL 1.2 or above..
}
OpenGLShaderProgram::getLanguageVersionstatic double getLanguageVersion()Returns the version of GLSL that the current context supports.