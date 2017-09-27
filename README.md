# backend-test

Purpose 
The assignment is deliberately not very precise and does not have a single correct solution. We're not looking for you to come up with any specific solution but are more interested to see how you interpret the assignment, what simplifying assumptions you make given the short time you have to work on it, how you architect your app, and what your coding style is. If in doubt as to which direction you should go, send us a quick note and ask (big bonus points for clarifying before jumping into coding!). Bonus points for doing proper error handling, adding unit tests, and commenting your code. The app should run and solve the problem, but no need to finish everything. Add TODOs and FIXMEs in places where you cut a corner for expediency but know a production ready version would need refactoring, additional tests or handling of certain edge cases that you know or suspect to exist but don't handle yet. Or, after you finish your first implementation and realize the architecture is not what it should have been. In that case don't waste time refactoring, but explain to us the problems you see and your proposed fix. 

Submission of Solution 
Please implement your solution as a simple app using the main technology* common for the position you're applying for and submit your code in a Git repository on GitHub, Bitbucket or similar. Bonus points for having a clean commit history (and other things one usually expects in clean repository) and sending us the last change as a pull request. 
*Android devs would write an Android app in Java or Kotlin, iOS devs an app in Objective-C or Swift, server-backend devs a Ruby on Rails app, and so forth. 

Code Review Interview 
After you submit your solution, we'll invite you to visit us at TenTen for a code review interview. Please bring your laptop as we'll ask you to walk us through your code and explain how it works. TenTen engineers will ask you questions about your code, so be ready. Remember that the code review is not just a chance for us to see how well you communicate technical ideas and how solid your computer science background is, but at the same time, a great chance for you to meet the engineers you'll be working with, what we care about, and whether we're smart enough for you to want to work with us. So test us back! 

# Computer simulator 
We want you to build a computer simulator that supports executing: 
def print_tenten
print(multiply(101, 10))
end
print(1009)
print_tenten()
# 1009 # 1010 

# Instructions 
- `MULT`: Pop the 2 arguments from the stack, multiply them and push the result back to the stack - `CALL addr`: Set the program counter (PC) to `addr`
- `RET`: Pop address from stack and set PC to address
- `STOP`: Exit the program 
- `PRINT`: Pop value from stack and print it - `PUSH arg`: Push argument to the stack 

# Interface 
The code should execute against: 
PRINT_TENTEN_BEGIN = 50
MAIN_BEGIN = 0
def main
# Create new computer with a stack of 100 addresses
computer = Computer.new(100)
# Instructions for the print_tenten function
computer.set_address(PRINT_TENTEN_BEGIN).insert("MULT").insert("PRINT").insert("RET")
# The start of the main function
computer.set_address(MAIN_BEGIN).insert("PUSH", 1009).insert("PRINT")
# Return address for when print_tenten function finishes
computer.insert("PUSH", 6)
# Setup arguments and call print_tenten
computer.insert("PUSH", 101).insert("PUSH", 10).insert("CALL", PRINT_TENTEN_BEGIN)
# Stop the program
computer.insert("STOP")
computer.set_address(MAIN_BEGIN).execute()
end
main() 

#The Stack 
This is what the stack should look like before the program gets executed. 

![Image of The Stack]
(https://github.com/deviget/backend-test/blob/master/Stack.png)
  
