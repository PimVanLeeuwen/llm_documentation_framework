#### shutdownOpenGL()


 void OpenGLAppComponent::shutdownOpenGL ( ) 
 

This must be called from your subclass's destructor, to shut down the GL system and stop it calling render() before your class is destroyed.