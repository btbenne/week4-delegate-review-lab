@ -0,0 +1,31 @@
# Code Review — Checkpoint 2

## 1. I agree with separating "file missing" from "file corrupted"

`load_tasks()` still returns an empty list when tasks.json doesn't exist, and only raises when the file is there but unreadable. I agree with the separation of "file missing" and "file corrupted". A missing file is normal on a first run but a corrupted one isn't. I agree with the AI's decision to make this change.

## 2. The exit code changed on a missing id and that is scope creep

`done 99` and `delete 99` used to exit 0. Now they exit 1. I did approve this at the plan checkpoint and I still think it's the right call, because saying you succeeded when nothing happened is a bug. But I asked for three things and this was a fourth. If something was running this tool in a script it could be checking that exit code. I want it named in the commit message so it isn't a silent change.

## 3. A second change got hidden inside the same block of code

The diff also moved `save_tasks()` inside the `if task:` block for `done`, so it stops rewriting the file when nothing actually changed. I think that's an improvement. What I don't like is that it's a separate change tucked inside the "friendly errors" work without being mentioned anywhere. This is how unrelated changes slip past a reviewer. It should have been its own commit, or at minimum the AI should have told me it did this.

## 4. I want to know if the None check on the title was on purpose

`add_task` does `title.strip() if title else ""`. Argparse requires the title argument, so title can never actually be None when it comes from the command line. That branch can't be reached. It's not wrong, and it does protect the function if something else ever calls it. But I'd want to ask whether that was deliberate or just habit, because code that can't run tends to pile up over time.

## 5. The error message gives away more than a user needs

The corrupted file message includes the exact line and column from the JSON parser. For a local tool like this one it doesn't matter. But if someone copied this pattern into something that reads files from a source you don't control, that's more internal detail than a user should see. I'm not asking for a change here, I just want it noted.

## 6. Raising errors instead of exiting was the right decision

The AI's first plan had `sys.exit()` inside `add_task()` and `load_tasks()`. I rejected that at the plan checkpoint. It would have made my acceptance tests impossible to write, because the test process itself would have exited instead of letting me catch anything. The version that got written raises exceptions and lets `main()` decide what to print and what exit code to use. That's testable and it keeps the command line stuff out of the core functions. I wanted to note the good decision too, not just the problems.

