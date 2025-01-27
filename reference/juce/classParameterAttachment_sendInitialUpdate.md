#### sendInitialUpdate()


 void ParameterAttachment::sendInitialUpdate ( ) 
 

Calls the parameterChangedCallback function that was registered in the constructor, making the UI reflect the current parameter state.This function should be called after doing any necessary setup on the UI control that is being managed (e.g. adding ComboBox entries, making buttons toggleable).