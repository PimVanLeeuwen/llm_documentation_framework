#### addNewComponentFromState()


 virtual Component \* ComponentBuilder::TypeHandler::addNewComponentFromState ( const ValueTree & state, Component \* parent ) pure virtual 
 

This method must create a new component from the given state, add it to the specified parent component (which may be null), and return it.The ValueTree will have been prechecked to make sure that its type matches the type that this handler supports.There's no need to set the new Component's ID to match that of the state the builder will take care of that itself.