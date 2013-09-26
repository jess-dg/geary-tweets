function LongestWord(sen) { 
  var largestWord = "";
  var splitSen = sen.split();
  for (numOfWord in splitSen) {
    if (splitSen[numOfWord].length > largestWord.length){
    	largestWord = splitSen[numOfWord];
	}
  }

  // code goes here  
  return largestWord; 
         
}
   
// keep this function call here 
// to see how to enter arguments in JavaScript scroll down
print(LongestWord(readline()));                            
 