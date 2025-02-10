#### iterate()


template<class EdgeTableIterationCallback > 

 void EdgeTable::iterate ( EdgeTableIterationCallback & iterationCallback ) const noexcept 
 

Iterates the lines in the table, for rendering.This function will iterate each line in the table, and call a userdefined class to render each pixel or continuous line of pixels that the table contains.Parameters

 iterationCallback this templated class must contain the following methods: inline void setEdgeTableYPos (int y); inline void handleEdgeTablePixel (int x, int alphaLevel) const; inline void handleEdgeTablePixelFull (int x) const; inline void handleEdgeTableLine (int x, int width, int alphaLevel) const; inline void handleEdgeTableLineFull (int x, int width) const; xfloat xDefinition juce\_UnityPluginInterface.h:200 yfloat float yDefinition juce\_UnityPluginInterface.h:200 (these don't necessarily have to be 'const', but it might help it go faster) 
 


References isPositiveAndBelow(), jassert, table, x, and y.