#### setOpaque()


 void Component::setOpaque ( bool shouldBeOpaque ) 
 

Indicates whether any parts of the component might be transparent.Components that always paint all of their contents with solid colour and thus completely cover any components behind them should use this method to tell the repaint system that they are opaque.This information is used to optimise drawing, because it means that objects underneath opaque windows don't need to be painted.By default, components are considered transparent, unless this is used to make it otherwise.See alsoisOpaque