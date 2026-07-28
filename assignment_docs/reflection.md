# Reflection

## Where were your checkpoints, and did they catch anything?

I set two checkpoints. Plan approval, where the AI had to show me what it intended to do before writing any code, and a full diff review before anything got merged into main.

The plan checkpoint caught something. The first plan had the AI calling `sys.exit()` inside `add_task()` and `load_tasks()` when it hit bad input. As a sentence that sounds fine, but it would have broken my acceptance tests completely. My tests call those functions directly, so instead of catching an error I could check, the whole test process would have shut down. Catching that took a minute of reading a short plan. Catching it afterward would have meant staring at a test runner that just quits and trying to work out why.

The diff review caught scope creep. The change made `done` and `delete` exit 1 instead of 0 when the id doesn't exist. I had approved that at the plan stage, but I still wanted it written down instead of buried in a bigger diff. There was also a second change I hadn't approved at all. It moved `save_tasks()` inside the `if task:` block so the file stops being rewritten when nothing happened. That's an improvement and I kept it, but nobody told me about it. It was just sitting in the same block of code as the work I did ask for.

## Which module failure modes did you observe, if any?

Of the three failure modes from the module, scope creep is the one I actually saw. I didn't get any confident wrong turns and I didn't see test gaming.

But I can see how test gaming would happen. If my two tests had been written loosely, or if I had only checked whether the tests passed instead of reading the code, the `sys.exit()` version might have gone through and I would have ended up changing my tests to fit the code instead of the other way around.

## How did reviewing AI code feel different from reviewing your own or a classmate's?

It felt different mostly in how much I had to actually ask. With my own code I already know why I did something, so reviewing it is really just proofreading.

Here I had a comment where I genuinely didn't know the answer. `add_task` checks whether the title is None, but argparse makes that impossible from the command line. I couldn't tell if that was on purpose or just habit, so I wrote it down as a question instead of pretending I knew. That's closer to reviewing a classmate's work, except with a classmate I'd have some sense of how they think.

## Would you trust this workflow on a real team, and under what conditions?

Yes, but only with a few things in place. The tests have to exist before the AI starts and stay outside its control. The diffs have to stay small enough that someone actually reads every line. And somebody has to be willing to ask "why is this here" out loud instead of approving it because it looks clean.

Without those, I think the code would look more finished than it really is, and the review would get lazier because of it.
