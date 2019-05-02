# The Boy or Girl Paradox
A small program to run a simulation of the "Boy or Girl Paradox" in a Graphic User Interface.

------ DESCRIPTION ------

The Boy or Girl Paradox (https://en.wikipedia.org/wiki/Boy_or_Girl_paradox) is an apparent paradox of statistics.

The premise is that, if a stranger told you that he has two children, of which at least one is female, the probabilities of this girl having a male brother are 66%. Now, a lot of people would have guessed 50%, but the fact of the matter is that there are three possibilitites to select from: girl/boy, boy/girl, girl/girl. Seen in this light, 66.6..% of probabilities appears very reasonable.

But this is not the core of the paradox. The extremely counterintuitive thing is, if the stranger then tells you the name of his female child, the odds of her having a male sibling drop down to the intuitively expected 50%!

I could have spent some time trying to wrap my head around the explanation of why this is the case, but instead I wrote a program to simulate a lot of pairs of children (each child randomly male or female, the girls randomly named) and then sum and divide the outcomes of dirt-tech counting.

Then, seeing as I was in the flow, I also added a slick GUI. Have fun.

# Run
The easyest way to run this little program is to double click on the Linux_executable file. A version for windows is coming as well.
Users may also decide to edit the file and run it from terminal or commnad line.

# Requirements
To run the program, you will need Python3 installed on your machine. Seeing as I only used packages from the Python Standard Library, you shouldn't need anything else.
