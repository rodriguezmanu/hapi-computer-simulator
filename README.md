# Computer simulator 

We ask that you complete the following challenge to evaluate your development skills. Please use the programming language and framework discussed during your interview to accomplish the following task.

## We want you to build a computer simulator that supports executing: 

```
def print_tenten
  print(multiply(101, 10))
end
print(1009)
print_tenten()
```

whose output would be
```
1009 
1010
```

## Instructions 

* `MULT`: Pop the 2 arguments from the stack, multiply them and push the result back to the stack 
* `CALL addr`: Set the program counter (PC) to `addr`
* `RET`: Pop address from stack and set PC to address
* `STOP`: Exit the program 
* `PRINT`: Pop value from stack and print it 
* `PUSH arg`: Push argument to the stack 

## Interface 

The code should execute against: 

```ruby
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
  # Execute the program
  computer.set_address(MAIN_BEGIN).execute()
end
main() 
```

This is what the stack should look like before the program gets executed. 

![Image of The Stack](https://github.com/deviget/backend-test/blob/master/Stack.png)

## API Interface 

The code should execute against these HTTP requests

```bash
# Create new computer with a stack of 100 addresses
curl -XPOST -d'{"stack":100}' you-app-server/v1/computers
# Instructions for the print_tenten function
curl -XPATCH -d'{"addr: 50"}' you-app-server/v1/computers/{computer-id}/stack/pointer
curl -XPOST you-app-server/v1/computers/{computer-id}/stack/insert/MULT
curl -XPOST you-app-server/v1/computers/{computer-id}/stack/insert/PRINT
curl -XPOST you-app-server/v1/computers/{computer-id}/stack/insert/RET
# The start of the main function
curl -XPATCH -d'{"addr: 0"}' you-app-server/v1/computers/{computer-id}/stack/pointer
curl -XPOST -d'{"arg":1009}' you-app-server/v1/computers/{computer-id}/stack/insert/PUSH
curl -XPOST you-app-server/v1/computers/{computer-id}/stack/insert/PRINT
# Return address for when print_tenten function finishes
curl -XPOST -d'{"arg":6}' you-app-server/v1/computers/{computer-id}/stack/insert/PUSH
# Setup arguments and call print_tenten
curl -XPOST -d'{"arg":101}' you-app-server/v1/computers/{computer-id}/stack/insert/PUSH
curl -XPOST -d'{"arg":10}' you-app-server/v1/computers/{computer-id}/stack/insert/PUSH
curl -XPOST -d'{"addr":50}' you-app-server/v1/computers/{computer-id}/stack/insert/CALL
# Stop the program
curl -XPOST you-app-server/v1/computers/{computer-id}/stack/insert/STOP
# Execute the program
curl -XPATCH -d'{"addr":0}' you-app-server/v1/computers/{computer-id}/stack/pointer
curl -XPOST you-app-server/v1/computers/{computer-id}/exec
```

The following is a list of items (prioritized from most important to least important) we wish to see:
* Implement a documented RESTful API for the app
* Implement an SDK client for the API implemented above. Ideally, in a different language, of your preference, to the one used for the API
* Unit Testing

## Forking Procedures

1.  Fork the repo to your own github account
2.  When you have code ready to be review submit a pull request

## Deliverables we expect:

* Pull request with the solution
* URL where the app can be accessed and used (use any platform of your preference: heroku.com, aws.amazon.com, etc)
* README file with the decisions taken and important notes

# Time Spent

You do not need to fully complete the challenge. We suggest not to spend more than 5 hours total, which can be done over the course of 2 days.  Please make commits as often as possible so we can see the time you spent and please do not make one commit.  We will evaluate the code and time spent.
 
What we want to see is how well you handle yourself given the time you spend on the problem, how you think, and how you prioritize when time is insufficient to solve everything.

As soon as you have submitted your solution, we will review the code.
 
Reply to ALL when you are finished. 
