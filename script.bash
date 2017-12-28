# Create new computer with a stack of 100 addresses
# printf "\nhttps://app-computer-simulator.herokuapp.com/computers\n"
curl -H "Content-Type: application/json" -X POST -d '{"stack":100}' https://app-computer-simulator.herokuapp.com/computers
# Instructions for the print_tenten function

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/pointer\n"
curl -H "Content-Type: application/json" -X PATCH -d '{"addr": 50}' https://app-computer-simulator.herokuapp.com/computers/1/stack/pointer

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/MULT\n"
curl -H 'Content-Type: application/x-www-form-urlencoded' -X POST https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/MULT

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PRINT\n"
curl -H 'Content-Type: application/x-www-form-urlencoded' -X POST https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PRINT

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/RET\n"
curl -H 'Content-Type: application/x-www-form-urlencoded' -X POST https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/RET
# The start of the main function

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/pointer\n"
curl -H "Content-Type: application/json" -X PATCH -d '{"addr": 0}' https://app-computer-simulator.herokuapp.com/computers/1/stack/pointer

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PUSH\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 1009}' https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PUSH

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PRINT\n"
curl -H 'Content-Type: application/x-www-form-urlencoded' -X POST https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PRINT
# Return address for when print_tenten function finishes

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PUSH\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 6}' https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PUSH
# Setup arguments and call print_tenten

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PUSH\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 101}' https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PUSH

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PUSH\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 10}' https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/PUSH

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/CALL\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 50}' https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/CALL
# Stop the program

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/insert/STOP\n"
curl -H 'Content-Type: application/x-www-form-urlencoded' -X POST https://app-computer-simulator.herokuapp.com/computers/1/stack/insert/STOP
# Execute the program

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/stack/pointer\n"
curl -H "Content-Type: application/json" -X PATCH -d '{"addr": 0}' https://app-computer-simulator.herokuapp.com/computers/1/stack/pointer

# printf "\nhttps://app-computer-simulator.herokuapp.com/computers/1/exec\n"
curl -X POST https://app-computer-simulator.herokuapp.com/computers/1/exec
