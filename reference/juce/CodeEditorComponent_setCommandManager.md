#### setCommandManager()


 void CodeEditorComponent::setCommandManager ( ApplicationCommandManager \* newManager ) noexcept 
 

Specifies a commandmanager which the editor will notify whenever the state of any of its commands changes.If you're making use of the editor's ApplicationCommandTarget interface, then you should also use this to tell it which command manager it should use. Make sure that the manager does not go out of scope while the editor is using it. You can pass a nullptr here to disable this.