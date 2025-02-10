#### getNextCommandTarget()


 virtual ApplicationCommandTarget \* ApplicationCommandTarget::getNextCommandTarget ( ) pure virtual 
 

This must return the next target to try after this one.When a command is being sent, and the first target can't handle that command, this method is used to determine the next target that should be tried.It may return nullptr if it doesn't know of another target.If your target is a Component, you would usually use the findFirstTargetParentComponent() method to return a parent component that might want to handle it.See alsoinvoke Implemented in CodeEditorComponent, and JUCEApplication.