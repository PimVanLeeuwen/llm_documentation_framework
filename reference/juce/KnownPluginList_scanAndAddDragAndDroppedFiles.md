#### scanAndAddDragAndDroppedFiles()


 void KnownPluginList::scanAndAddDragAndDroppedFiles ( AudioPluginFormatManager & formatManager, 
 
 const StringArray & filenames, 
 OwnedArray< PluginDescription > & typesFound ) 

Scans and adds a bunch of files that might have been draggedanddropped.If any types are found in the files, their descriptions are returned in the array.