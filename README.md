# Welcome to the Azure Quantum challenge at QCHack 2022!

We are excited to offer this challenge to QC Hack 2022 participants, and we are looking forward to the projects you will come up with!

## Challenge overview

This challenge consists of two parts. In part 1, you will explore simple quantum programming tasks and submitting quantum jobs using Azure Quantum. In part 2, you will use a quantum computer to implement and explore the solution to a problem of your choice!

### Part 1: Warmup tasks
Part 1 of this challenge can be found in the folder [Part1](./Part1). It contains three independent tasks that help you get familiar with the various tools you’ll need in the main part of the challenge.

* [Task 1. Implementing a quantum oracle (Q#)](./Part1/Task1_QuantumOracleQsharp.ipynb) – 1 point
* [Task 2. Submitting Azure Quantum jobs from Q# Jupyter Notebooks (Q# + IonQ simulator)](./Part1/Task2_DeutschAlgorithmQsharpIonQ.ipynb) – 1 point
* [Task 3. Submitting Azure Quantum jobs from Python Jupyter Notebooks (Qiskit + Quantinuum emulator)](./Part1/Task3_QrngQiskitQuantinuum.ipynb) – 1 point

### Part 2: Free-form project

In part 2, you will come up with a problem you’d like to explore using a quantum computer, implement the solution in a quantum programming language, and explore its behavior on a variety of simulator and hardware targets in Azure Quantum.
You can develop your project using any language supported by Azure Quantum: **Q#, Qiskit, or Cirq**.
*You’ll be able to run your code on a real ion trap quantum computer provided by IonQ, as well as on an accurate simulator of the quantum computer H1-2 provided by Quantinuum and a noiseless cloud simulator by IonQ. Remember that current devices are still NISQ, and noise can overtake the computation really fast. We recommend you experiment with circuits that use under a few dozen two-qubit gates.*

Here are a few project ideas to get you started:

* Pick an algorithm and compare algorithm results when running on a noiseless simulation vs a noisy simulation vs a QPU.
* Show how to tweak a general-purpose algorithm implementation that is in general too complicated to run on a QPU (for example, one that uses library routines) to simplify it for a specific problem and run it on QPU. What are the helpful tricks here?
* In the [Introduction to QDK and Azure Quantum](https://www.twitch.tv/videos/1447170150) workshop you saw that you can run Grover’s search for a simple problem with search space of size 4. What is the largest problem instance for your problem which you can solve on a quantum computer and get the correct result without it being overtaken by the noise?
* If you want to use Variational Algorithms for your project (i.e., algorithms that use a classical loop to generate quantum circuits parametrically, such as VQE or QAOA), please keep in mind that this class of programs can take a long time to run, which might not be feasible within the time allocated to the Hackathon. We suggest developing and running your program on a local simulator first, and only running the final iteration on hardware.

Your project for part 2:
* Must include a problem description and instructions on running the project in README.md file.
* Must solve a small instance of the problem without any user input, or with a well-documented user input. If your solution requires an input, its format should be documented in README.md, including an example.
* Must use one or several of the eligible Azure Quantum targets (IonQ simulator, Quantinuum emulator, and IonQ QPU) to solve a small instance of the problem.
* Must produce an output presenting the instance of the problem solved and the solution in human-readable format.
* Must be original, i.e., not previously covered in Quantum Development Kit samples, learning materials, or the Quantum Katas.

Since the project repository is the main deliverable for your project (there are no presentations scheduled during the judging period), we recommend you include everything you want to share with the judges to showcase your work, including the job execution results and your analysis of them.

### Using Azure Quantum

You should have received an invite to join quantum workspace [qchack-2022-b - Microsoft Azure](https://portal.azure.com/#@achocronme.onmicrosoft.com/resource/subscriptions/b0c3bbe3-7123-4ba4-9aa2-57d9845f4a1d/resourceGroups/AzureQuantum/providers/Microsoft.Quantum/Workspaces/qchack-2022-b/overview). Join it, and use that workspace’s information to connect to Azure from the environment you’re using to work with the QDK:

* Subscription ID: b0c3bbe3-7123-4ba4-9aa2-57d9845f4a1d
* Resource group: AzureQuantum
* Workspace name: qchack-2022-b
* Location: eastus

You can use it from Python+Q# environment by using the `azure-quantum` package as follows:

```
from azure.quantum import Workspace
workspace = Workspace (
    subscription_id = "b0c3bbe3-7123-4ba4-9aa2-57d9845f4a1d",
    resource_group = "AzureQuantum",
    name = "qchack-2022-b",
    location = "eastus"
)
```

or from Qiskit environment by using `azure.quantum.qiskit` package as follows:

```
from azure.quantum.qiskit import AzureQuantumProvider
provider = AzureQuantumProvider (
    resource_id = "/subscriptions/b0c3bbe3-7123-4ba4-9aa2-57d9845f4a1d/resourceGroups/AzureQuantum/providers/Microsoft.Quantum/Workspaces/qchack-2022-b",
    location = "eastus"
)
```

Don't wait until the last moment to submit your programs! Both IonQ and Quantinuum systems operate on a queue system. If you submit a program to a QPU, it may take a few hours to complete. If you want to make sure you get your results back by Sunday morning, make sure to submit them by the end of day on Saturday.

The eligible Azure Quantum targets for this project are:

* [IonQ noiseless simulator `ionq.simulator`](https://docs.microsoft.com/azure/quantum/provider-ionq)
* [IonQ QPU `ionq.qpu`](https://docs.microsoft.com/azure/quantum/provider-ionq)
* [Quantinuum H1-2 system emulator `quantinuum.hqs-lt-s2-sim` and API validator for it `quantinuum.hqs-lt-s2-apival`](https://docs.microsoft.com/azure/quantum/provider-quantinuum)

> If you try to submit a job to one of the Quantinuum hardware targets, it will remain in "Waiting" status until the end of the hacking period without being processed.

## Submitting your solutions
To submit your solutions:
1.	Fork (or duplicate) this repository to your GitHub account.
2.	Work on the solutions to the tasks from part 1 and the project from part 2.
3.	Commit your work to your forked repository.  
For part 1 tasks, you should submit the Jupyter Notebooks with your solution (for task 1) or job execution results (for tasks 2 and 3). For part 2 project, commit any files you consider relevant: the project itself, screenshots of results, any visualizations you've done, the project description, and so on.
4.	To submit your project, submit the link to your repository.  
Your repository has to be made public at the time of the Hackathon end for us to be able to judge your solutions. We don't recommend making your work public early during the Hackathon, so as not to tempt other teams to borrow from your work. Let everybody enjoy their exploration!  
*Note that GitHub doesn't allow to change visibility of the forks. You can either fork the repository, keep it public, and push your changes at the last possible moment, or you can duplicate the repository, make it private to work on it during the Hackathon, and make it public at the end of the Hackathon. Your repo is not required to be an actual fork, it just has to follow the folder structure of this repo for Part 1 tasks.*
5.	If your project for part 2 includes a blog post about your project, publish it shortly after the Hackathon end and add a link to it to your GitHub repository.

## Judging
Part 1 tasks will be evaluated based on the correctness of your solution: for task 1, we’ll check that your solution is correct by running the testing harness for it (provided in the same Jupyter Notebook file as the task), and for tasks 2 and 3, we’ll check that the outputs of each code cell in the notebook match the typical outputs of job submission and results retrieval. 

The judging for part 2 of the challenge will be more flexible than for part 1. Since there is no single "right" solution, we'll be evaluating the projects based on several criteria. Here is the list of criteria and example questions we'll consider when evaluating the projects:

* *Technical depth* (6 points). How complicated is the selected problem? How well is it solved? Is the solution to the problem displayed using a clever visualization?
* *Use of Azure Quantum* (6 points). Evaluates the breadth of Azure Quantum targets used in the project. All three eligible Azure Quantum targets are scored here: IonQ simulator, Quantinuum emulator, and IonQ QPU each give 2 points. 
* *Creativity* (4 points). How original is the problem selection? How creative is the output presentation?
* *Educational value* (5 points): Is this project valuable for helping others learn? Did the team write a blog post about the project sharing their learnings with others? Is the project structured as a tutorial?

The highest cumulative team score from parts 1 and 2 is **24 points**.

## Eligibility and prizes

The (5) highest cumulative team scores from parts 1 and 2 of the challenge will receive a **$200 Visa Gift Card** (physical or virtual) for the team. The winning teams will have an opportunity to present their projects to the Microsoft Quantum Team, at a later date and time (to be scheduled after the results announcement).

Government officials and Microsoft employees are not eligible to participate in this challenge.

## Resources
### Microsoft Quantum Development Kit installation
For this Hackathon, you can work entirely within the Azure Quantum hosted Notebooks environment. 

Alternatively, you can set up a local environment for your language of choice and run jobs from it. 

If you choose Q# as your language, you will need to install at least the [standalone QDK](https://docs.microsoft.com/azure/quantum/install-command-line-qdk), and possibly (depending on what kind of project you decide to do) integration with [Q# Jupyter Notebooks](https://docs.microsoft.com/azure/quantum/install-jupyter-qkd) or with [Python](https://docs.microsoft.com/azure/quantum/install-python-qdk).

### Documentation and tutorials

* [Introduction to QDK and Azure Quantum](https://www.twitch.tv/videos/1447170150) workshop at QCHack.
* [Azure Quantum and QDK documentation](https://docs.microsoft.com/quantum).
* [The Quantum Katas](https://github.com/Microsoft/QuantumKatas/) - a collection of tutorials and practice problems.
* Microsoft Learn learning path ["Quantum computing foundations"](https://docs.microsoft.com/learn/paths/quantum-computing-fundamentals/).
* [Q# developer blog](https://devblogs.microsoft.com/qsharp/).
