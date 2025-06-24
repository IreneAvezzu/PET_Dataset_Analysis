In addition to the constraint models provided above, there are others:

- alternate-succession(A,B): Between any two A events, there must be exactly one B. So, B must occur after each A, but no two As without a B in between. A and B alternate.
	1. Some examples satisfying this constraint:
		- Each request (A) must be followed by a decision (B), and you can’t make another request until a decision is made.
		- The assistant submits a report (A), which is immediately approved by the manager (B), and then another report is submitted (A) and approved (B).
		- After a submission (A), there's a timely approval (B), followed by archiving.
		- The process involves submitting (A) → approval (B) → submission (A) → approval (B), with no skipped approvals.
	2. Some examples violating this constraint:
		- Two submissions (A) occur in a row before any approval (B) is given.
		- A submission (A) happens, then a discussion takes place, and another submission (A) occurs without any approval (B) in between.
		- A report is submitted (A), approved (B), then submitted again (A), but no second approval (B) follows.

- Init(a): A must be the first event in every process of execution. The process starts with A.
	1. Some examples satisfying this constraint:
		- A login (A) must be the first action in a session.
		- The user first starts a session (A), then proceeds to log in and access the dashboard.
		- The workflow begins when the system starts a session (A) before allowing the user to browse products.
		- A session is initiated (A), followed by profile viewing and editing.
	2. Some examples violating this constraint:
		- The user logs in (B) before the session is started (A).
		- Dashboard access occurs first (B), and the session start (A) is recorded later.
		- The flow begins with product browsing, not with session start (A) as required.

- not-responded-existence(A,B): If A occurs, then B must not occur anywhere in the process. The presence of A excludes B.
	1. Some examples satisfying this constraint:
		- If an emergency shutdown (A) occurs, then no restart (B) can happen in the same trace.
		- The fraud detection tool flags the account (A), and the team proceeds to suspend it without unlocking (B).
		- After an audit, the system flags an account (A), and a report is generated - no unlocking (B) happens.
		- The agent flags the account (A), which leads directly to closure (C), bypassing any unlock (B). 
	2. Some examples violating this constraint:
		- The system flags the account (A) and then later unlocks it (B) after user verification.
		- Following a flagging (A), the account is temporarily unlocked (B) to retrieve data.
		- The sequence B → A → C violates the constraint because both A and B happen within the same process.
		- The account is flagged (A) during review, and later unlocked (B) for continued use.

- not-response(A,B): If A happens, then B must not happen afterward. B is not allowed after A.
	1. Some examples satisfying this constraint:
		- If an invoice is canceled (A), no payment (B) should happen after.
		- The technician closes the ticket (A) and archives it without any further action.
		- After closing the ticket (A), the system logs the case as resolved with no reopening (B).
		- A ticket is closed (A) and followed by a feedback request, with no reopen (B) in the workflow.
		- The sequence B  A  C is allowed
	2. Some examples violating this constraint:
		- The ticket is closed (A) and then later reopened (B) due to a missed issue.
		- Closing (A) is followed by a user complaint, leading to a reopen (B).
		- After a ticket is closed (A), a second-level agent reopens it (B) for escalation.

- not-precedence(A,B): If B occurs, then A must not have occurred before. A must not precede B.
	1. Some examples satisfying this constraint:
		- If a refund is issued (B), it must not be preceded by a delivery (A).
		- The system issues a refund (B) automatically based on transaction failure, without any complaint submission (A) from the user.
		- A refund (B) is provided proactively during a recall process, with no customer complaints (A) involved.
		- The support team issues a refund (B) before any chance of submitting a complaint (A) by the user.
	2. Some examples violating this constraint:
		- The customer submits a complaint (A), and then the company issues a refund (B) in response.
		- After several complaint submissions (A), a refund (B) is processed.
		- A ticket involving a complaint (A) leads directly to a refund (B) approval.

- not-chain-response(A,B): It is forbidden that B occurs immediately after A. B must not directly follow A.
	1. Some examples satisfying this constraint:
		- After submitting a form (A), an approval (B) must not happen immediately.
		- The user saves a draft (A), reviews the data (C), and then submits the form (B).
		- After saving the draft (A), the document is edited (C) and only then submitted (B).
		- The process includes draft saving (A), a peer review, and finally form submission (B).
	2. Some examples violating this constraint:
		- The user saves the draft (A) and immediately submits the form (B).
		- Save draft (A) is followed directly by submission (B) without any checks.
		- A and B occur consecutively with no intermediate validation step.

- not-chain-precedence(A,B): If B occurs, it must not have been immediately preceded by A. A must not be directly before B.
	1. Some examples satisfying this constraint:
		- If a task is marked complete (B), it must not come right after a comment (A).
		- The system checks account balance (C), then grants access (B) - identity validation (A) was done earlier or skipped.
		- After completing a background check (C), the system grants access (B), not immediately after identity validation (A).
		- Access is granted (B) following a security questionnaire (C), with no direct preceding validation (A).
	2. Some examples violating this constraint:
		- The system validates identity (A) and immediately grants access (B).
		- A user passes identity check (A) and access is granted (B) right after, violating the constraint.
	
- succession(A,B): If A occurs, then B must also occur (at some point later), and vice versa: if B occurs, then A must have occurred before. A and B are connected; one implies the other, in order.
	1. Some examples satisfying this constraint:
		- If a customer places an order (A), then an invoice must be issued (B) and if an invoice is issued, the order must have been placed
		- The process begins with (A) requesting creation, followed by (B) requesting approval, then proceeding to C and D for execution.
		- Workflow starts with C, followed by A for initial check, then d, and finally B for final approval.
	2. Some examples violating this constraint:
		- The process starts with A, then goes to C and D, but B is never executed.
		- B occurs early in the process, followed by C, but A never takes place beforehand.
		- The workflow has A at the beginning, C in the middle, and ends with D - B is completely missing.

- choice(A,B): A or B have to occur at least once.
	1. Some examples satisfying this constraint:
		- The process begins with A for document review, followed by C, and ends with D. B never occurs.
		- The workflow includes B for data approval after C, but A is not present.
		- The trace includes both A and B, with A occurring before C, and B happening after D.
	2. Some examples violating this constraint:
		- The trace includes only C, D, and E - neither A nor B are present.
		- Workflow starts with C, then moves to D, and ends with E. No trace of A or B.
		- The entire process involves only repeated executions of C and D, excluding both A and B.

- exclusive-choice(A,B): A or B have to occur at least once but not both.
	1. Some examples satisfying this constraint:
		- The process starts with A for submission, continues with C, and ends with D - B never appears.
		- Only B for manual override occurs midway through the trace; A is never executed.
		- The process starts with C then reaches a step where a condition is either verified of not, based on the condition result the process proceeds with A or B, only one is chosen
	2. Some examples violating this constraint:
		- The process includes A for creation, followed by B for confirmation later in the trace.
		- After C, both A and B are executed as part of A dual-check process.
		- The workflow loops through both A and B multiple times before finalizing with D.

- not-exclusive-choice(A,B): It is not allowed that only one of A or B occurs; if one happens, the other must also occur. Both A and B must either happen together or not at all.
	1. Some examples satisfying this constraint:
		- If A contract is signed (A), then onboarding (B) must also occur, and vice versa.
		- The process includes A for creation, followed by B for confirmation later in the trace.
		- After C, both A and B are executed as part of a dual-check process.
		- The workflow loops through both A and B multiple times before finalizing with D.
	2. Some examples violating this constraint:
		- Only A is executed in the trace, without A corresponding B.
		- The workflow contains B for approval but skips A entirely.
		- A appears early in the process, but B never occurs, violating the required pairing.

- not-chain-succession(A,B): It is forbidden that B directly follows A (i.e., with no events in between). B can happen after A, but not immediately after.
	1. Some examples satisfying this constraint:
		- A system check (B) must not follow a reboot (A) immediately.
		- The process starts with A, followed by C, and only then B for validation.
		- A initiates the workflow, followed by D, E, and then B appears toward the end.
		- B appears early, then A occurs, and later C finishes the trace. At no point does B directly follow A.
	2. Some examples violating this constraint:
		- The trace begins with A, and B occurs immediately after as the second event.
		- A is executed, followed directly by B, with no intermediary steps.
		- A mid-process A is followed instantly by B without interruption.

- chain-succession(A,B): A and B occur in the process instance if and only if the latter immediately follows the former.
	1. Some examples satisfying this constraint:
		- After scanning a product (A), the system must immediately log the scan result (B).
		- The trace is A → B → C → D. Every A is immediately followed by B, and every B has A just before it.
		- The process includes C, then A → B, and then D. 
		- A single A → B pair appears, with no other instances of A or B elsewhere in the trace.
		- A sequence like C → A → B → A → B → C is allowed by this constraint
	2. Some examples violating this constraint:
		- A is followed by C, with B appearing later - B does not directly follow A.
		- B appears without A preceding A.
		- One A is followed by B, but another B shows up without any prior A.
		- Sequences like B → C → A → A → C and B → C → A → A → B → C are not allowed.

- chain-response(A,B): Each time A occurs in the process instance, then B occurs immediately afterwards, with no other action in between.
	1. Some examples satisfying this constraint:
		- A → B → C → D: every A is directly followed by B.
		- C → B → D: B can occur even without A prior.
		- The trace has one A → B sequence; any B not preceded by A is still allowed.
	2. Some examples violating this constraint:
		- A → C → B: B does not immediately follow A.
		- A appears but is followed by D, not B.
		- Multiple A events occur, but none are immediately followed by B.

- chain-precedence(A,B): Each time B occurs in the process instance, then A occurs immediately beforehand.
	1. Some examples satisfying this constraint:
		- A → B → C → D: B occurs immediately after A and nowhere else.
		- C → A → B → D: B is always and only right after A.
		- A → C → D: A can occur even without B
	2. Some examples violating this constraint:
		- B occurs first without any A before it.
		- A → C → B: B is not immediately after A.
		- B appears multiple times, but not every instance is preceded by A directly.

- alternate-response(A,B): If A occurs, then B must eventually follow without any other A in between.
	1. Some examples satisfying this constraint:
		- A → B → A → B → C: every A is followed by B before another A occurs.
		- C → A → B → D: only one A, and it’s followed by B.
		- A → B → C → D: A single instance of A followed by B, with no second A.
	2. Some examples violating this constraint:
		- A → A → B: second A occurs before B appears.
		- A → C → A → B: B doesn’t follow the first A before the second A.
		- A → D → A → C → B: multiple As without Bs in between.

- alternate-precedence(A,B): B can occur only if A has occurred before, without any other B in between.
	1. Some examples satisfying this constraint:
		- The employee submits the report (A) before the manager approves it (B), and then the document is finalized.
		- The analyst submits one report (A) and gets it approved (B), then submits another (A) which is also approved (B).
	2. Some examples violating this constraint:
		- The manager approves the report (B) even though it was never submitted (A) beforehand.
		- The employee submits a report (A), gets it approved (B), and then a second approval (B) happens without a new submission (A).
		- The system logs an approval (B) first, then a submission (A) - violating the required order.