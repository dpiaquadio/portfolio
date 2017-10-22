/* 
Author: Dominick Piaquadio
Purpose: To Load Multiple JS Files with a single function
*/

function loadScripts(){
	var directory = 'js/';
	var extension = '.js';
	$.get("requirements.txt", function(data){
		var files = data.split(",");
		for (i=0; i < files.length; ++i){
			var path = directory + files[i] + extension; 

			$.getScript(path, function(){
				main();
			});	
		};
	}, 'text');
};

/* 

Instructions
------------

Step 1: Create a 'requirements.txt' file in the root of your web directory (this is where your index.html file is located)
Step 2: Create / Add to your js/ directory all .js files used in your project
Step 3: When creating js files, ensure you have a main() function or this code won't work

      function helloWorld(){
        alert("Hello World!");
      }
      
      function main(){
        helloWorld();
      }
      
      For the code to work with any js file, a common function (main()) was created. As the loadScripts() function gets a script,
      it needs to call a function (or else the functions will have to be called within an unnecessary <script> section).
      
Step 4: As you create more js files, record them into your 'requirements.txt' as follows:
      
      llamas,donkeys,pizza,tacos,
      
      OR
      
      llamas,
      donkeys,
      pizza,
      tacos,
      
      Each function name is separated by a comma as a means of splitting each name up.
      
I hope this helps you in your projects. This is Open-Source and anyone can use this code. If there are questions or logical fallacies
in this code and/or my explanation, please feel free to let me know. Enjoy!

*/
