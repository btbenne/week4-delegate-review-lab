# Checkpoint Records

## Checkpoint 1 — Plan approval (before any code)

I told the AI to show me a plan and not write anything until I approved it.

### The plan it came back with

1. Add a `TaskTrackerError` exception class.
2. In `add_task()`, if the title is empty or whitespace, call `sys.exit(1)` with an error message printed from inside the function.
3. In `load_tasks()`, on bad JSON, call `sys.exit(1)` with an error message printed from inside the function.
4. In `main()`, for `done`/`delete` on a missing id, print a message and exit 1.
5. Write the acceptance tests.

### What I corrected

I rejected steps 2 and 3, and I told it not to write my acceptance tests since those were already written and off limits.

The problem with `sys.exit()` inside `add_task()` and `load_tasks()` is that my tests call those functions directly. If the function exits the process, my test can't catch anything, the whole test run just dies. There's also no reason for those functions to know they're being called from a command line at all. If someone later put a web interface or a different front end on this, they'd want to catch the error and handle it their own way, not have the program quit on them.

So I asked for the normal split instead. The core functions raise exceptions (`ValueError` for a bad title, `TaskTrackerError` for a corrupted file), and only `main()` catches them and decides what to print and what exit code to use.

### Two things I decided at this checkpoint

**Missing id exit code.** Right now `done 99` prints a message but exits 0, which means it reports success when nothing happened. I approved changing that to exit 1. I knew going in this was a fourth thing on top of my three requirements, so I decided up front it had to be named in the commit message rather than slipped in quietly.

**Non-integer id.** I asked whether `done abc` needed custom handling. It doesn't. Argparse already rejects it with a clear usage message and exit code 2, no traceback, so my acceptance criterion was already met with zero new code. I told it not to add anything there. Writing a custom handler would have been duplicate code doing a job something else already does.

### Did it catch anything?

Yes. The `sys.exit()` problem would have made my acceptance tests impossible to write, and I would have found that out by watching my test runner quit for no obvious reason. Reading a five step plan took about a minute. Debugging that afterward would have taken a lot longer.

## Checkpoint 2 — Full diff review (before merge)

I ran `git diff` and read every line myself rather than trusting the AI's summary of what it did. I also ran the tests on my own machine instead of taking its word that they passed.

Results: 9 baseline tests passed, both of my acceptance tests passed, and six manual command line checks all behaved correctly. The corrupted file was still sitting on disk untouched afterward, which was one of my acceptance criteria.

The six comments that came out of this review are in `code_review.md`. The two that mattered most were the missing-id exit code change (scope creep I had approved but wanted written down) and the `save_tasks()` move that got bundled into the same block of code without anyone mentioning it.

I approved the merge on the condition that the exit code change was named in the commit message. It was.
