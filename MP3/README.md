## ECE598SG (Special Topics in Robot Learning)
### Programming Assignment 3
In this programming assignment you will implement basic behavior cloning for
discrete (`CartPole`) and continuous control tasks (`DoubleIntegrator` and
`PendulumBalance`). You will also implement DAgger ([1](#references)) for controlling the cartpole
from images (`VisualCartPole`). We have provided expert data / policies. 
You have to use these to train policies to solve these tasks. 

1. **Behavior Cloning from States [15 pts]**. Using the expert data as supervision,
   implement behavior cloning for the 3 environments. For the discrete task,
   you can use a cross entropy loss, and for the continuous task you can use a
   mean-squared error loss. We have provided code for loading in the expert
   data (see [run_behavior_cloning.py](run_behavior_cloning.py)), and a 
   simple feed-forward policy (see [policies.py](policies.py)). You need to 
   implement the training loop. You will measure performance of your policies, 
   by running it in 100 validation episodes.
   1. **Implementation [10pts].** Get your implementation to work and solve the
      3 tasks. You may have to play around with hyper-parameters for training
      the network. You can also tweak the policy architecture if you'd like.
      Report the design choices, hyper-parameters, average reward, and the 
      metrics that your policy is able to achieve on the 3 environments. You 
      can get started by running the following command: 
      `python run_behavior_cloning.py --logdir LOGDIR --env_name CartPole-v2`.
   2. **Data efficiency of learning [5pts].** Study the performance of your
      policy as a function of the number of expert demonstrations. You should
      vary the number of expert episodes on a log scale (so, keep halving them
      from however many there are in total). Make sure you train the network to
      convergence for each run. Plot the rewards and the metrics for the 3
      environments as a function of the number of expert demonstrations.

 2. **Control from Images using DAGGER [15pts].** Next, we will use imitation 
    learning to train visual policies for cart pole (`VisualCartPole`). We will
    train a CNN based policy to imitate an expert that uses state information. Our
    behavior cloning implementation failed at this, as the visual policy starts
    experiencing states that are missing from the demonstration dataset. Thus, we
    will experiment with the DAgger algorithm ([1](#references)).  We've provided a
    state-based expert policy, and your task is to implement the DAgger algorithm
    to learn policies for VisualCartPole. 
    
    You can run the starter code with `python ./run_dagger.py`.
    It shows how to load and query the expert policy. 
    Your policy should get a mean reward above 130 with 200 length episodes.
    
    In your report:
      1. Note any modifications you make to the starter policy or training loop, and
      document implementation specifics of your DAGGER implementation (i.e.  how
      you choose to set Beta, trajectory length, etc.). 
      2. Include a plot showing test-time performance of your visual policy 
      as a function of the number of expert-labelled environment steps. 

    Notes: 
      1. Our naive implementation is able to get mean reward > 130 in less than 15
      minutes on GPU. You may be able to train far faster than this. 
      2. To load the expert policy, you need to install the `stable_baselines3`
      package, included in `requirements.txt`.  This has been tested with python
      3.8.5, and `stable_baselines3==1.2.0`. If you encounter issues loading the
      policy, consider switching to these versions. If you're running headless on
      a remote server you may encounter an error like
      `pyglet.canvas.xlib.NoSuchDisplayException: Cannot connect to "None"`. To
      resolve this you need to use something like `xvfb` for rendering. You can
      try something like `xvfb-run -a -s "-screen 0 1400x900x24" python
      ./run_dagger.py`

#### Instructions
1. Assignment is due at 11:59PM on Tuesday October 18, 2022.
2. Please see
[policies](http://saurabhg.web.illinois.edu/teaching/ece598sg/fa2022/policies.html)
on [course website](http://saurabhg.web.illinois.edu/teaching/ece598sg/fa2022/index.html).
3. Submission instructions:
   1. A single report for all questions in PDF format, to be submitted to
      gradescope (under assignment `MP3-report`).  This report
      should contain all that you want us to look at. Please also tag your PDF
      with locations for each question in the gradescope interface.
   2. You also need to submit code as `.py` files for all questions in the form 
      of a single `.zip` file. Please submit this under `MP3-code` on gradescope.
   3. We reserve the right to take off points for not following submission
      instructions.
4. You should be able to work on problem 1 even without a GPU, though you will
likely need a GPU for training visual policies for part 2.
You can use GPUs through Google Colab. Instructions to use Google Colab can be found in
[MP1](../MP1).
5. Lastly, be careful not to work of a public fork of this repo. Make a *private*
clone to work on your assignment. 

#### References
1. Stephane Ross Geoffrey J. Gordon J. Andrew Bagnell. [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf). In AISTATS 2011.