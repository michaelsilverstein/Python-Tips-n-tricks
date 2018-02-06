# if __name__ == '__main__' tutorial
Created by: Michael Silverstein

I've found this to be one of the most unnecessarily difficult concepts to understand about python scripting. You see the 
`if __name__ == '__main__':` condition at the end of python scripts all over the internet, but wtf is it talking about?

In essence, `__name__` is a special variable - it exists when a python script is run. Let's say we have two scripts, 
`scriptA` and `scriptB`. If we run `scriptA` directly, the `__name__` is automatically set to `__main__`, however,
if we import `scriptA` into `scriptB` to use a function from `scriptA`, during this import within the world of `scriptA`,
 `__name__` will not equal `__main__`. This is because `scriptA` is being called from another script. 
 
 This is convenient because we may want `scriptA` to do one thing if we call it directly, but we may want `scriptA` to 
 do something else if functions from `scriptA` are called from `scriptB`.
 
 Hmm... not sure if that was very clear. Hopefully the tutorial will make things clearer. 
 
 **Start off by running the following scripts:**
1. [script1](): Read the contents of this script and then run it. `script1` contains some functions that we use in one way
in `script1`, but may be useful to call from another script. The contents of the `if __name__ == '__main__'` will only 
run when `script1` is called directly.

2. [script2](): Read the contents and then run it. `script2` will call some functions from `script1` without running any
of the contents within the `if __name__ == '__main__'` clause.