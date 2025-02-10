#### translateFragmentShaderToV3()


 static String OpenGLHelpers::translateFragmentShaderToV3 ( const String & ) static 
 

Makes some simple textual changes to a shader program to try to convert old GLSL keywords to their v3 equivalents.Before doing this, the function will check whether the current context is actually using a later version of the language, and if not it will not make any changes. Obviously this is not a real parser, so will only work on simple code!