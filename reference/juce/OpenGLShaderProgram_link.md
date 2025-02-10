#### link()


 bool OpenGLShaderProgram::link ( ) noexcept 
 

Links all the compiled shaders into a usable program.If your app is built in debug mode, this method will assert if the program fails to link correctly.Returnstrue if the program linked successfully. If not, you can call getLastError() to find out what happened.