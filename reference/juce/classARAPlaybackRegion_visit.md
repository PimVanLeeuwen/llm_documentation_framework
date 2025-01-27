#### visit()


 void ARAPlaybackRegion::visit ( ARAObjectVisitor & visitor ) overridevirtual 
 

Allows the retrieval of the concrete type of a model object.To use this, create a new class derived from ARAObjectVisitor and override its functions depending on which concrete types you are interested in.Calling this function inside the function passed to ARAObject::traverse() allows you to map the entire ARA model graph.Implements ARAObject.References ARAObjectVisitor::visitPlaybackRegion().