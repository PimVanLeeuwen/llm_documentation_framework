#### shouldCommandBeIncluded()


 virtual bool KeyMappingEditorComponent::shouldCommandBeIncluded ( CommandID commandID ) virtual 
 

Can be overridden if some commands need to be excluded from the list.By default this will use the KeyPressMappingSet's shouldCommandBeVisibleInEditor() method to decide what to return, but you can override it to handle special cases.