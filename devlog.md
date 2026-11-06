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

# Nov 6 2:03 PM

I am currently trying to figure how to assign tellers to customers, and print out the statements in conjunction. Currently, I'm planning on having a shared array of avalible tellers, and a another pool of array to show which customer is being served. Customer ID is the index, and Teller ID is the person to be served. 

I added a waiting array as well in case all the tellers are full, and wrote the precursor statemetns for selection and introduction. I have yet to test the code. I may have to change the purpose of the serving array in the future right now, it shows which customerID is being served from the threadID. I having a hard time visualizing when the customer and thread_id would loop back and forth. 

I just noticed an error in my serving code, I am pointing to a nonexisistent index. So for initlizication, I will change it to 3 empty index values to prevent this in the future. 

# Nov 6 2:25 PM

I just realized that there is no point in the waiting array, as .acquire already fufills that purpose. I will need to change the if/else statements.
I remodefied them, and removed the extra .acquire statement in the end since we dont want to two tellers per customer. 

I need to make ready a mutex, since multiple threads could take a open teller at once. 

I decided to make readyTeller and readyCrit separate due to their important roles.

I redid the order of the Teller and Customer acquire+release statements to reflect the changed logic.

I may need to have 3 threads semaphors for customers to keep up with the tellers, as I just found out that threads can be 
non-deterministic. This means that any thread can be awoken with the .release statement. 

I had previously assumed that order was the main factor. I will update this code accordingly.

This feels like a lot of debugging ahead, for now I'll commit these changes to fix them in the next session. 
