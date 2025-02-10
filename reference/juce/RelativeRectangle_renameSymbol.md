#### renameSymbol()


 void RelativeRectangle::renameSymbol ( const Expression::Symbol & oldSymbol, 
 
 const String & newName, 
 const Expression::Scope & scope ) 

Renames a symbol if it is used by any of the coordinates.This calls Expression::withRenamedSymbol() on the rectangle's coordinates.