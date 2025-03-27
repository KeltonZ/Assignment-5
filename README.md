# Assignment-5 Functions and unit testing- Comp 1327

## Description

throughout this assignment I'll be demonstrating and practicing my understanding of functions and unit testing modules

## Author

Kelton Zinn

## Reflection

### 1. Identify any challenges or issues you encountered while writing your functions.

- It was difficult to figure out how to code things using functions in general, took a lot of research and slowly I
learned how the scope of variables worked, local versus global. I often struggle to remember things when I don't
experience the results first hand.
- There were times where I was asked to process certain errors as a TypeError when the system declares it as a value error, 
I solved this by raising that exception as a ValueError then a TypeError.
- I also encountered issues in understanding how arguments and calling functions from within other functions worked, at one point I accidentally created a call
stack that seemingly infinitely called the chatbot. Not sure how that happened but It confused me greatly. I resolved this later when I realized I was accidentally 
running functions multiple times due to the logic of my code.

### 2. Discuss the benefits and challenges of developing and using unit tests.

- I found unit testing complicated and didn't really understand it at first, I think I had written my first few tests somewhat improperly,
but they did function regardless. later on I feel I understood both the importance and was writing them closer to the expected standard.
- sometimes when writing code I would use a manual call to learn how my code was working or not, however this proved to be problematic as 
I once or twice forgot to remove that code, and so the test would call the call and require me to make inputs and other unforeseen consequences.
- Learning that excepting exceptions can cause an exception to not be detected as raised, which makes sense.