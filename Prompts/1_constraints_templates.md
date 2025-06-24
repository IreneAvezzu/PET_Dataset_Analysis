Process discovery is a type of process mining aiming to represent the process model explaining how the process is executed. Our focus is on the discovery of an imperative process model. Recently, we developed
a framework that allows for some declarative constraints as input to discover better imperative models. Declarative models are close to the natural language, however for a domain expert, they might not be familiar.
Therefore, we need your help to translate the process description given as a text to the declarative constraints we need for the discovery of imperative process models.
Consider only the following declarative constraint definitions where a, b, c, and d are activities and template example-template(x,y) specifies a template named "example-template" and x and y can be on of the activities from the set of all activities. Do not reason based on the template names and only use explanations to understand the meaning of specific templates:

- at-most(A): A occurs at most once. 
	1.	Some examples satisfying this constraint:
		- The process starts with activity B for setup, followed by A for approval, then C for data collection, and ends with D for implementation. Optional execution of B can occur again before C.
		- The workflow begins with C for initial data collection, followed by D for setup, then A for mandatory approval, and concludes with B for detailed planning.
		- The process initiates with D for setup, followed by B for planning, C for data analysis, and finally A for essential approval. Optional execution of C may occur again after B. 
	2.	Some examples violating this constraint:
		- The process starts with A for initial approval, followed by B for planning, then loops back to A for re-approval, and ends with C for data analysis and D for implementation.
		- Begin with C for data collection, followed by A for approval, then B for planning, another A for re-approval, and ends with D for execution.
		- The workflow involves D for setup, followed by parallel execution of A for initial approval and B for planning, then A second occurrence of A for final approval, and C for final data analysis.

- existence(A): A occurs at least once, which means the existence of activity A is mandatory.
	1. Some examples satisfying this constraint:
		- The process starts with activity B for initial setup, followed by A for mandatory approval, then C for data collection, and finally D for implementation. Optional execution of C can occur again before d.
		- The workflow begins with D for setup, followed by A for critical approval, then parallel execution of B for planning and C for analysis, and concludes with D for finalization.
		- Activity C starts with data gathering, then loops to B for planning, followed by A for essential approval, and ends with D for implementation.
		- all the customers start the process with activity A.
	2. Some examples violating this constraint:
		- The process starts with B for initial tasks, followed by C for data analysis, and concludes with D for implementation. Optional execution of C can occur again before D.
		- Begin with D for setup, followed by B for detailed planning, then C for further analysis, and ends with D for final execution. 
		- The workflow involves C for initial data collection, followed by parallel execution of B for planning and D for implementation, and ends with another round of C.
		- Either one of the activities A or B occurs. Each trace can only have A or B.

- response(A,B): If A occurs, then B occurs after A.
	1. Some examples satisfying this constraint:
		- The process starts with C for data collection, then A for approval, followed by B for planning, and finally D for implementation. Optional execution of C may occur again before D.
		- Activity D begins with preliminary tasks, then A for approval, followed by parallel execution of B for planning and C for analysis, ending with D for finalization.
		- The workflow initiates with A for approval, loops back to A second approval if needed, then proceeds to B for detailed planning, and concludes with C for execution.
		- All the occurrences of activity A should be followed by activity B.
	2. Some examples violating this constraint:
		- The process starts with B for initial setup, followed by C for data analysis, then A for approval, and ends with D for implementation.
		- Begin with C for data gathering, followed by A for approval, then D for execution, and optionally B for post-implementation review.
		- The process involves D for setup, followed by A for approval, and then C for analysis. An optional activity B for final planning may or may not occur.

- precedence(A,B): B occurs only if preceded by A.
	1. Some examples satisfying this constraint:
		- The process begins with activity A for approval, followed by C for data collection, and then B for planning. Optional execution of D can occur anytime before or after B.
		- Activity D initiates the setup, then A for mandatory approval, followed by parallel execution of C for analysis and B for planning, and concludes with D for finalization.
		- The workflow starts with C for initial tasks, followed by A for approval, then B for detailed planning, and ends with A loop back to C for further analysis if needed.
		- After execution of activity A, some cases will continue with activity B and some cases will continue with activity C.
	2. Some examples violating this constraint:
		- The process starts with C for data gathering, followed by B for planning, then A for approval, and ends with D for implementation.
		- Begin with D for initial setup, followed by parallel execution of B for planning and C for analysis, and finally A for approval.
		- The workflow involves D for setup, followed by C for data collection, B for planning, and ends with an optional activity A for final approval.

- co-existence(A,B): A and B occur together. 
	1. Some examples satisfying this constraint:
		- The process starts with B for initial setup, followed by A for approval, then C for data collection, and ends with D for implementation. Optional execution of B can occur again before C.
		- Activity A begins with approval, followed by parallel execution of B for planning and C for data analysis, and concludes with D for finalization.
		- The workflow starts with D for setup, followed by A for approval, B for planning, and ends with C for execution. Optional execution of C may occur again after B.
	2. Some examples violating this constraint:
		- The process begins with C for data collection, followed by D for setup, then B for planning, and ends with another round of C.
		- Start with D for setup, followed by C for data analysis, then A for approval, and ends with C for final review.
		- The workflow involves C for initial data gathering, followed by parallel execution of D for setup and B for planning, and concludes with C for finalization.

- not-co-existence(A,B): A and B never occur together.
	1. Some examples satisfying this constraint:
		- The process starts with A for approval, followed by C for data collection, then D for implementation. Optional execution of C can occur again before D.
		- Begin with B for initial setup, followed by C for analysis, then D for execution. An optional activity C can repeat after D.
		- The workflow starts with C for data gathering, then moves to D for setup, followed by optional repetitions of C.
		- In our process activities A and B cannot occur together.
		- Some cases have activity A and the other cases have activity B.
		- If activity A does not occur, then activity B will occur.
	2. Some examples violating this constraint:
		- The process begins with A for approval, followed by B for planning, then C for data collection, and ends with D for implementation.
		- Start with C for data analysis, then A for approval, followed by D for execution, and ends with B for final review.
		- The workflow involves D for setup, followed by parallel execution of A for approval and B for planning, and concludes with C for finalization.

- not-succession(A,B): B cannot occur after A.
	1. Some examples satisfying this constraint:
		- The process starts with A for approval, followed by C for data collection, and ends with D for implementation. Optional execution of C can occur again before D.
		- Begin with B for initial setup, followed by D for setup, then A for approval, and finally C for analysis.
		- The workflow starts with C for data gathering, followed by A for approval, then D for execution, and optional repetitions of C.
	2. Some examples violating this constraint:
		- The process begins with A for approval, followed by B for planning, then C for data collection, and ends with D for implementation.
		- Start with C for data analysis, then A for approval, followed by D for execution, and ends with B for final review.
		- The workflow involves D for setup, followed by parallel execution of A for approval and C for analysis, then B for planning, and concludes with C for finalization.

- responded-existence(A,B): If A occurs in the trace, then B occurs as well.
	1. Some examples satisfying this constraint:
		- The process starts with B for initial setup, followed by A for approval, then C for datA collection, and ends with D for implementation. Optional execution of B can occur again before c.
		- Begin with A for initial approval, followed by D for setup, then B for planning, and finally C for analysis.
		- The workflow starts with C for data gathering, followed by A for approval, then D for execution, and optional repetitions of B for planning.
	2. Some examples violating this constraint:
		- The process begins with A for approval, followed by C for data collection, then D for implementation. Optional execution of C can occur again before d.
		- Start with C for data analysis, followed by A for approval, then D for execution, and ends with C for final review.
		- The workflow involves D for setup, followed by A for approval, then parallel execution of C for analysis and B for planning, and concludes with C for finalization.

Some more instructions:
- It is not possible to generate constraints like response(a, (b or c)). The first and second elements must be a single activity

For each task, I provide the set of activity labels that exist in the process with a short description. Then, I present a text written by a process expert and want you to translate it to declarative constraints and write it in a plaintext block.