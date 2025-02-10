#### setName()


 virtual void Component::setName ( const String & newName ) virtual 
 

Sets the name of this component.When the name changes, all registered ComponentListeners will receive a ComponentListener::componentNameChanged() callback.See alsogetName Reimplemented in DocumentWindow.