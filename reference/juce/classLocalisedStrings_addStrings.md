#### addStrings()


 void LocalisedStrings::addStrings ( const LocalisedStrings & ) 
 

Adds and merges another set of translations into this set.Note that the language name and country codes of the new LocalisedStrings object must match that of this object an assertion will be thrown if they don't match.Any existing values will have their mappings overwritten by the new ones.