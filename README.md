# The role of modes in nonlinear fiber optical computing

This repo includes Jupyter notebooks that are used for nonlinearly propagating input datasets and applying mode decomposition on the output speckle fields.

* ```BPM_breast_mnist.ipynb``` is an example beam propagation method (BPM) simulation that implements generalized nonlinear Schrödinger equation (GNLSE). The complex fields resulting from the simulation are saved for further use in ridge classification.
* ```MD.ipynb``` is used for mode decomposition in the Sinc regression task.
* ```MD_breast_mnist.ipynb``` is used for mode decomposition in the Breast MNIST classification task. By changing the path information to a different dataset, you can work with datasets like CIFAR-10.
* ```ridge_classification.ipynb``` can be used to load complex fields from BPM simulations and to perform ridge classification on intensity patterns.
* ```calc_entropy.py``` details entropy and mode power distribution calculations that are used in generating Fig. 4 of the manuscript.


Supported modes of the multimode fiber (MMF) were calculated using the mode solver in [1].

## References

[1] Thomas Murphy (2025). Waveguide Mode Solver (https://www.mathworks.com/matlabcentral/fileexchange/12734-waveguide-mode-solver), MATLAB Central File Exchange. Retrieved December 1, 2025.