#### addShader()


 bool OpenGLShaderProgram::addShader ( const String & shaderSourceCode, 
 
 GLenum shaderType ) 

Compiles and adds a shader to this program.After adding all your shaders, remember to call link() to link them into a usable program.If your app is built in debug mode, this method will assert if the program fails to compile correctly.The shaderType parameter could be GL\_VERTEX\_SHADER, GL\_FRAGMENT\_SHADER, etc.Returnstrue if the shader compiled successfully. If not, you can call getLastError() to find out what happened.