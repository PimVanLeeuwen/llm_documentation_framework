#### setFallback()


 void LocalisedStrings::setFallback ( LocalisedStrings \* fallbackStrings ) 
 

Gives this object a set of strings to use as a fallback if a string isn't found.The object that is passedin will be owned and deleted by this object when no longer needed. It can be nullptr to clear the existing fallback object.