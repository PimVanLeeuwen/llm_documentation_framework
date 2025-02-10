#### updateComponentFromState()


 virtual void ComponentBuilder::TypeHandler::updateComponentFromState ( Component \* component, const ValueTree & state ) pure virtual 
 

This method must update an existing component from a new ValueTree state.A component that has been created with addNewComponentFromState() may need to be updated if the ValueTree changes, so this method is used to do that. Your implementation must do whatever's necessary to update the component from the new state provided.The ValueTree will have been prechecked to make sure that its type matches the type that this handler supports, and the component will have been created by this type's addNewComponentFromState() method.

Member Data Documentation