# Task Definition — Assignment 4.1

The feature I picked: input validation and error handling.

Right now the task tracker crashes or silently does the wrong thing when
you give it bad input. If you add a task with an empty title, it happily
saves a blank task. If tasks.json gets corrupted, you get a wall of red
traceback text. If you try to complete a task id that doesn't exist, it
just prints a message and exits like nothing went wrong. I want to clean
all of that up.

## What I'm asking the AI to do

Add input validation and error handling to task_tracker.py:

1. Don't let someone add a task with an empty or blank title. Print a
   clear message and exit with an error code, and don't write anything
   to tasks.json.
2. If tasks.json is corrupted and can't be read, say so in plain English
   instead of crashing with a traceback.
3. If someone types a task id that doesn't exist, or types something
   that isn't a number at all, give them a normal error message instead
   of a crash.

Rules for the AI: don't touch test_task_tracker.py or test_acceptance.py,
don't change anything unrelated to this, and don't refactor things I
didn't ask about.

## How I'll know it worked

- All 9 of the original tests still pass.
- `add ""` and `add "   "` both get rejected, exit with an error code,
  and leave tasks.json alone.
- A corrupted tasks.json gives a readable error, no traceback, error
  exit code, and the bad file doesn't get overwritten.
- `done abc` and `delete abc` fail cleanly instead of crashing.

## My two tests

I wrote these in test_acceptance.py before handing anything to the AI,
and the AI isn't allowed to change them. If it can only pass them by
editing them, that's cheating, not a fix.

1. `test_add_rejects_empty_title` — add_task should raise a ValueError
   on a blank title and leave the task list untouched.
2. `test_load_tasks_corrupted_file_raises_taskerror` — load_tasks should
   raise its own specific error on bad JSON, not let a raw
   JSONDecodeError escape.

I wrote them against the functions directly instead of just checking
what the CLI prints, so the AI can't satisfy them by wrapping everything
in a try/except in main() and calling it done.

## My checkpoints

1. **Plan approval** — the AI has to show me its plan before it writes
   any code. I'm looking for whether it's staying in scope and whether
   the approach will actually let my tests work.
2. **Full diff review** — I read the whole diff myself before anything
   gets merged. Not the AI's summary of the diff, the actual diff.
