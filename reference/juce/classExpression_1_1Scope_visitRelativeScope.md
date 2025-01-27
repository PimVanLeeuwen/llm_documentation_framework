#### visitRelativeScope()


 virtual void Expression::Scope::visitRelativeScope ( const String & scopeName, Visitor & visitor ) const virtual 
 

Creates a Scope object for a named scope, and then calls a visitor to do some kind of processing with this new scope.If the name is valid, this method must create a suitable (temporary) Scope object to represent it, and must call the Visitor::visit() method with this new scope.Reimplemented in RelativeCoordinatePositionerBase::ComponentScope.