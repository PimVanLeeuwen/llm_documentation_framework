#### clipRegionIntersects()


 bool Graphics::clipRegionIntersects ( Rectangle< int > area ) const 
 

Checks whether a rectangle overlaps the context's clipping region.If this returns false, no part of the given area can be drawn onto, so this method can be used to optimise a component's paint() method, by letting it avoid drawing complex objects that aren't within the region being repainted.