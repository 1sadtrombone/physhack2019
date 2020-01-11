# physhack2019
a bunch of random walk sims

You need python 3 with matplotlib and numpy.
A few things: some of these plots are animated, so they pop back up when you close them. Just hold q to close the plot and hit ^C quickly.
Also, the colour scales adjust automatically.
Mess with the parameters all you want if you can decipher their purposes.

Here's the menu: (in suggested viewing order)

feedback_walk -- poorly named (it was like 3am). No feedback, just a vanilla 1d random walk, 
where brighter colour means more particles at that spot (or equivalently more likely to see a 
single particle at that spot, if it walked along unseen until then). Scrolls down until tmax time
steps (default 1000), then shows you the whole walk.

feedback_walk_iter -- like feedback_walk but the probability to move right from a location is
proportional to the particle density (brightness) at that location. Observe the predictability!

feedback_walk_pmove -- like feedback_walk but the probability to move at all (left or right)
from a location is proportional to the particle density (brightness) at that location.
It's still a 50/50 left/right split if a particle decides to move.

feedback_walk_skip -- like feedback_walk but the step length from a location is
proportional to the particle density (brightness) at that location.

2d_feedback_walk -- Again poorly named 2d version of feedback_walk. Crashes after tmax time steps.

2d_feedback_walk_avg -- like 2d_feedback_walk but pright (which I think it turns out governs the 
probability to move down) at a location depends on the particle density at the location in the 
previous step. Observe the upwards drift!

2d_feedback_walk_sink -- same as 2d_feedback_walk_avg except there is a horizontal strip where I've set the
density (brightness) to zero. Observe how the particles spread out along that "barrier"!

2d_feedback_walk_skip -- same as 2d_feedback_walk except step length from a location is proportional to density at that location

--- This concludes the main section --
Here are some complete but unrelated ideas

sticks -- you're walking along one misty night and you look up at the branches of a tree, lit from behind by the full moon.
You notice circular patterns in the branches, centred on the moon. You suppose this is because the branches that are more tangential
to the moon reflect more. This is an attempt to recreate that experience, except the branches are now randomly distributed rotating
lines, to show the circular pattern remains, no matter which sticks participate in it.

icon -- a cool thing I made that uses basically the same code as sticks.

--- This concludes the stuff I'm proud of ---
The rest are unfinished or uninteresting scripts that I've added only for completeness.
Delve at your own risk.
