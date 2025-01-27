#### attachTo()


 void OpenGLContext::attachTo ( Component & ) 
 

Attaches the context to a target component.If the component is not fully visible, this call will wait until the component is shown before actually creating a native context for it.When a native context is created, a thread is started, and will be used to call the OpenGLRenderer methods. The context will be floated above the target component, and when the target moves, it will track it. If the component is hidden/shown, the context may be deleted and recreated.