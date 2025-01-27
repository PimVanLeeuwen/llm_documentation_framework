#### addProperties()


 void PropertyPanel::addProperties ( const Array< PropertyComponent \* > & newPropertyComponents, 
 
 int extraPaddingBetweenComponents = 0 ) 

Adds a set of properties to the panel.The components in the list will be owned by this object and will be automatically deleted later on when no longer needed.These properties are added without them being inside a named section. If you want them to be kept together in a collapsible section, use addSection() instead.