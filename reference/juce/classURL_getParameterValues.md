#### getParameterValues()


 const StringArray & URL::getParameterValues ( ) const noexcept 
 

Returns an array of the values of all the URL's parameters.e.g. for the url "www.fish.com?type=haddock&amount=some+fish", this array would contain two items: "haddock" and "some fish".The values returned will have been cleaned up to remove any escape characters.You can call getParameterNames() to get the corresponding name of each parameter. Note that the list can contain multiple parameters with the same name.See alsogetParameterNames, withParameter