#### getCommandCategories()


 StringArray ApplicationCommandManager::getCommandCategories ( ) const 
 

Returns the list of categories.This will go through all registered commands, and return a list of all the distinct categoryName values from their ApplicationCommandInfo structure.See alsogetCommandsInCategory()