#### isCommandReadOnly()


 virtual bool KeyMappingEditorComponent::isCommandReadOnly ( CommandID commandID ) virtual 
 

Can be overridden to indicate that some commands are shown as readonly.By default this will use the KeyPressMappingSet's shouldCommandBeReadOnlyInEditor() method to decide what to return, but you can override it to handle special cases.