#### addSection()


 void PropertyPanel::addSection ( const String & sectionTitle, 
 
 const Array< PropertyComponent \* > & newPropertyComponents, 
 bool shouldSectionInitiallyBeOpen = true, 
 int indexToInsertAt = 1, 
 int extraPaddingBetweenComponents = 0 ) 

Adds a set of properties to the panel.These properties are added under a section heading with a plus/minus button that allows it to be opened and closed. If indexToInsertAt is < 0 then it will be added at the end of the list, or before the given index if the index is nonzero.The components in the list will be owned by this object and will be automatically deleted later on when no longer needed.To add properties without them being in a section, use addProperties().