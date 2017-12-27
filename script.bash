# Create new computer with a stack of 100 addresses
printf "\nlocalhost:3000/computers\n"
curl -H "Content-Type: application/json" -X POST -d '{"stack":100}' localhost:3000/computers
# Instructions for the print_tenten function

printf "\nlocalhost:3000/computers/1/stack/pointer\n"
curl -H "Content-Type: application/json" -X PATCH -d '{"addr": 50}' localhost:3000/computers/1/stack/pointer

printf "\nlocalhost:3000/computers/1/stack/insert/MULT\n"
curl -H 'Content-Type: application/x-www-form-urlencoded' -X POST localhost:3000/computers/1/stack/insert/MULT

printf "\nlocalhost:3000/computers/1/stack/insert/PRINT\n"
curl -H 'Content-Type: application/x-www-form-urlencoded' -X POST localhost:3000/computers/1/stack/insert/PRINT

printf "\nlocalhost:3000/computers/1/stack/insert/RET\n"
curl -H 'Content-Type: application/x-www-form-urlencoded' -X POST localhost:3000/computers/1/stack/insert/RET
# The start of the main function

printf "\nlocalhost:3000/computers/1/stack/pointer\n"
curl -H "Content-Type: application/json" -X PATCH -d '{"addr": 0}' localhost:3000/computers/1/stack/pointer

printf "\nlocalhost:3000/computers/1/stack/insert/PUSH\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 1009}' localhost:3000/computers/1/stack/insert/PUSH

printf "\nlocalhost:3000/computers/1/stack/insert/PRINT\n"
curl -H 'Content-Type: application/x-www-form-urlencoded' -X POST localhost:3000/computers/1/stack/insert/PRINT
# Return address for when print_tenten function finishes

printf "\nlocalhost:3000/computers/1/stack/insert/PUSH\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 6}' localhost:3000/computers/1/stack/insert/PUSH
# Setup arguments and call print_tenten

printf "\nlocalhost:3000/computers/1/stack/insert/PUSH\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 101}' localhost:3000/computers/1/stack/insert/PUSH

printf "\nlocalhost:3000/computers/1/stack/insert/PUSH\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 10}' localhost:3000/computers/1/stack/insert/PUSH

printf "\nlocalhost:3000/computers/1/stack/insert/CALL\n"
curl -H 'Content-Type: application/json' -X POST -d '{"arg": 50}' localhost:3000/computers/1/stack/insert/CALL
# Stop the program

printf "\nlocalhost:3000/computers/1/stack/insert/STOP\n"
curl -X POST localhost:3000/computers/1/stack/insert/STOP
# Execute the program

printf "\nlocalhost:3000/computers/1/stack/pointer\n"
curl -H "Content-Type: application/json" -X PATCH -d '{"addr": 0}' localhost:3000/computers/1/stack/pointer

printf "\nlocalhost:3000/computers/1/exec\n"
curl -X POST localhost:3000/computers/1/exec
