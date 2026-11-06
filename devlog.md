# Nov 1 8:54 PM 

Start of the project, I just initilized the github repo and I am considering python for this project. 
For now, my goal is to make a MVP of the customer and Tellers. I am somewhat confused how to begin with this project. 

I am considering making the Teller and Customer are seprate functions, which will be declared from the main function or 
global area. 


# Nov 5 5:32 PM 

I think, I will spend time ideating or seeing what method works. Right now, I don't know what is even possible with this. 
So for basics, I know I will need the threading modules, and the semaphor functions within them. However, I can't identify which particular areas are the particular zones, and in general what should be a semaphor. 

For now, I will write a default system with one teller and one customer just to see what it feels like. 

I did not test anything yet, but wrote some basic code. I'm unsure if it even compiles or if the syntax is correct. I'll commit this for the time being. 


# Nov 6 1:41 PM 

I will try to test the previous code to understand what is going on with threading.Thread() function. I will note if any errors occur after compilation. 
Aside from a few syntax errors, I am able to printout the starting statements of either tellers or customers being avalible for all threads. I tested it with 3 threads 
so far (for each), and it appears to be working. 

Next, I will try to do basic interactions like Teller 1 attending to Customer 0. I predict this will require modifying only the Teller and Customer functions, since 
the external code is primarily to build the threads not control their interactions. 

I will commit this for the time being. 

