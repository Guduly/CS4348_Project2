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


# Nov 6 2:59 PM

Since the previous num_Customers was a singular semaphore, I had to add its index value across the code to resolve any future issues with it. 

Right now, I will try to ensure the correct code is able to compile and perform very basic interactions.

Compilation has been successful, there was only a simple formatting error. The output changes across runs, so it looks good. 

Next, I will proceed with the communication process and go till we are able to complete a transaction. 
I made a few remodeling changes like adding acquire and release for append statements for future safety. 

I removed the if ready statement, since it feels unecessary with numTellers keeping track of how many tellers are free by default. 

Previously, I was able to initiate communication between the Teller and Customer. Now, I have to figure out how the comunication will actually occur. 
I am considering making 2 semaphore arrays each hosting 3 threads, so that each customer is able to ask question and teller is able to respond back with a answer. 
Making them a semaphore is important, because they're value can be diluted with multiple threads acting together and it helps maintain a communication order. 

I am having a hardtime seeing where I need to put the acuquire and release statements. I added the random action selection component, but communication feels really hard.

I think i'll stop for now. I'll commit my changes and test them at a later time/day.

# Nov 8 4:42 PM 

I forgot my current progress, but for now I am run my program with 5 -> 10 -> 20 customers just to see if I need to debug anything at this point.

All the tellers seem to be selected across the various test, and the program stalls at the withdraw and deposit stage, since there is nothing there for that component. 
Regardless, current program is debug free for operations. 


Before performing the actual transaction by going to safe or manager, I will handle the timing components for both customer and timer. In addition, I should consider adding entrance component requirements for customers and how many tellers can go the safe on duty. 

I am placing customer wait after "Going to the Bank" text to illustrate travel and follows the project directions. I must now build the door code to allow at max 2 customers to enter at once, this will obviously be a semaphore. 

I wrote some code for that in addition to the manager wait time. I am currently working on the safe entrance component, which should also be a semaphore to prevent race conditions. 
In addition, I am also writing the output text for them as well. 

This code feels very subject to change, since I did not run it yet. Regardless, I will commit these changes and attempt to debug any issues in the next entry. 

# Nov 8 6:02 PM 

While reviewing the sample output pdf given and testing the program, I realized that manager should also be a semaphore since there is only one of them. During a test run, 2 tellers were interacting with the manager at the same time. 

To correct it, I am making manager a semaphore and adding the appropriate acquire + release statements. 

I added the fixes, and no two tellers interacted with the managers at the same time. In addition, I added some print statements to show illustrate the waiting time for customer arrival, safe entering, and other periods for easier debugging. 

For now, the code seems to be working well. I ran it multiple times and did not face any errors except for it stalling for input at the end, which may have occured due to another customer not being selected.

I have festivities right now, so this will be a short entry. Next entry will document the process of a teller selecting a another customer once the job is over.

# Nov 12 10:17 PM 

During lecture, I asked the professor if the exit door is the same as the entrance door. He confirmed it was, I will add this implementation as well. 
Currently, the main tasks left are ensuring the teller can switch properly between customers and also add the above implementation. 

Right now, I am having a hard time seeing how i can switch between customers for the tellers. would a simple array work, or just moving unto the next customer. 

But then, one or more threads may grab the same customer if the one or more tellers are done at the same time. 

In which case, a semaphore would the be the best option. I will run my code a few times, just to see if I can spot any other issues before devlving into debugging or development 

All the program compiles, so I was not able to notice any issues, but for now I will add the semaphore to complete a task.

I made it so that if a the task were done, the customer will leave and pass through the entrance and exit doors. 

Now, the challenge remains in picking the next customer. 

I can't think of anything right now, so I'll commit my changes. But this solution and closing the bank should be the last few changes needded. 
