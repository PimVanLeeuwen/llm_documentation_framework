#### solve()


template<typename ElementType > 

 bool dsp::Matrix< ElementType >::solve ( Matrix< ElementType > & b ) const noexcept 
 

Solves a linear system of equations represented by this object and the argument b, using various algorithms depending on the size of the arguments.The matrix must be a square matrix N times N, and b must be a vector N times 1, with the coefficients of b. After the execution of the algorithm, the vector b will contain the solution.Returns true if the linear system of equations was successfully solved.