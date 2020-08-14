## WWCode DFW Interviewing session
Actually I lost my notes from this so going from memory

Had interview Q+A with tips/tricks from two WWCode members
- Check out the book "The why"..? (was it *Start with Why?* I think so)
- Use your experience to weave a narrative, how you take skills from past and expand on them

# Whiteboarding problems
1. FizzBuzz
  - Can be solved in a for loop, or forEach
  - Ask interviewer if you're taking an array as input or not.
  - Can make a function which returns/handles each number to give the correct output
  - Few ways to solve it

2. Product Sense Problem "How would you determine if price of netflix subscription is truly the deciding factor for a consumer?"
  1. State your assumptions:
    - What is a consumer? US-based or interntional? Veteran users? New user adoption? How long they stay a user?
    - What is "truly"? Do competitors affect? Are there any competitors? Seasonality?
    - What price? Is it $1 change? $10 change? Free?
  2. Design your experiment:
    - A/B testing
    - Population and sample size: need to be large and broad enough
    - Control for outside factors: how do you make sure populations dont leak? How can you control for competitors?
    - Survey (this is not strictly an experiment but observation)
  3. Build data requirements
    - What kind of data? Qualitative or quantitative? Structured or unstructured?
    - How do you join your tables - pricing/billing data, usage data - how do you combine there?
    - Data quality? How can you quality check some sample data?
  4. Address reproducibility and followup
    - Is it reproducible - why or why not
    - How would you test for other factors
    - Most importantly, what is the business impact?

  3. Tic-tac-toe
  "Explain the game of tic tac toe to an alien"
    - What are the rules?
    - Where do you play?
    - How many players?
    - What happens next - strategy?

  4. Find single item in an array
    - This was an interesting leetcode problem. Given an array of numbers, each nubmer is in there twice except for one, find that one. Use linear time, can you do it without extra memeory?
    EX `find([2,3,5,3,2]) => 5`
    Solution 1: Use a dictionary, add each item to the dictionary as you go through the array. If it is already in there, do not add it.
    Solution 2: XOR - need to look into this one.
