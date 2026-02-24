#!/bin/sh
# Step 1: Preprocess
g++ -E main.cpp -o main.i
# Step 2: Compile to assembly
g++ -S main.cpp -o main.s
# Step 3: Assemble to object
g++ -c main.cpp -o main.o
# Step 4: Link to executable and run
g++ main.o -o a.out
timeout 10 ./a.out > result.txt
