# Paper-only to Harbor task

Use this reference when the starting input is a paper, paper link/PDF, or a paper plus incomplete code rather than an existing runnable Harbor repository. The outcome is a measurable task package and launch evidence, not a reproduction of the entire paper.

## 1. Intake and evidence boundary

Record the paper title, authors, canonical link or local PDF, code/data links, licenses, and any missing assets. Read enough of the paper and supplementary material to identify:

- the concrete research problem and the input/output objects;
- the part of the method that can become an editable optimization surface;
- the metric, direction, evaluation unit, and likely runtime;
- data or pretrained assets that may be redistributed, mounted, or generated;
- claims that require a real-data check versus claims that can be tested synthetically.

Do not treat a reported paper score as a task score. Preserve the paper as source evidence and record any interpretation or missing detail.

## 2. Slice a runnable task

Choose one bounded question that an Agent can improve through code and experiments. Define in `instruction.md`:

- the objective and score direction;
- the editable files and interfaces;
- fixed data, seeds, splits, and prohibited shortcuts;
- public/dev data and the independent/private evaluation boundary;
- CPU/GPU/memory/time limits and case/bundle timeouts;
- the expected solution handoff and the exact scoring command.

Reject or narrow a paper-only proposal when the result would depend on unavailable proprietary data, subjective judging, an unbounded reproduction, or a metric that cannot be run independently.

## 3. Build the minimum repository

Create the Harbor layout required by the live tutorial and current QA contract. At minimum, establish:

1. `instruction.md` with the task contract;
2. `environment/` and its Dockerfile or equivalent runtime definition;
3. a clean editable `solution/` Starter;
4. public/dev assets and a deterministic evaluator;
5. independent verifier/private assets or a documented safe injection path;
6. `tests/` and task metadata that transfer the submitted solution to the verifier;
7. an evidence directory outside the Agent-visible workspace.

Keep hidden assets, reference methods, and expert-only calibration outside the Agent-visible mount. Do not put the paper's complete solution, private test data, or provider credentials in the research workspace.

## 4. Establish Baseline and Reference

Run the untouched Starter in a clean Agent environment and save its command, version, resource use, raw outputs, and aggregate score. Then implement only the minimum expert Reference needed to show that the task is real and improvable. Use the same public protocol, seeds, and resources for paired comparisons; repeat enough times to characterize variation.

The Reference is a launch gate and calibration artifact. Stop expert exploration once the task is runnable, measurable, and has a stable improvement signal. Leave literature search, method design, ablations, failure analysis, and final selection to the independent research Agents.

## 5. Launch gates

Before starting the two long runs, verify all of the following:

- a clean Starter produces a real nontrivial public score;
- the Reference improves under the same protocol without saturating the task;
- a fresh process can run the evaluator after the solution handoff;
- public and private/verifier inputs are isolated;
- the two Agent workspaces, trajectories, sessions, Goal/SQLite state, and observers are separate;
- the requested model, API budget, resource limits, effective-time target, absolute deadline, and submission fields are recorded.

If any gate is missing, keep the work in preparation and do not count it as Agent research time. Once all gates pass, use [launch-and-effective-time.md](launch-and-effective-time.md) and continue through the main skill workflow.

## 6. Paper-specific handoff

Keep a local intake record containing the source hashes, task-slicing decision, license/asset notes, Baseline/Reference receipts, and unresolved interpretation risks. Include it in expert evidence or optimization evidence only where the live submission contract allows. Never give one Agent the other Agent's trajectory, private result, or hidden feedback.
