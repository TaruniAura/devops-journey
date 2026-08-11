What is a Process?

A process is simply a program that is currently running.

Examples:

Chrome → Process
VS Code → Process
Terminal (bash) → Process
sleep 100 → Process

Every running program has a unique PID (Process ID).

1. ps – View Running Processes
What it does

Shows running processes.

Run:

ps

Example:

PID   TTY          TIME CMD
2456  pts/0    00:00:00 bash
2512  pts/0    00:00:00 ps
Meaning
PID → Process ID
TTY → Terminal
TIME → CPU time used
CMD → Command name
Show all processes
ps -e

or

ps -ef

This displays all processes running on your system.

2. top – Live Process Monitor

Run:

top

You'll see:

CPU usage
Memory usage
Running processes
System uptime

Press:

q

to exit.

3. htop – Interactive Process Viewer

First check if it's installed:

htop

If not:

sudo apt update
sudo apt install htop

Run:

htop

You'll get a more user-friendly view than top.

Exit with:

F10

or

q
4. sleep – Create a Test Process

We'll use the sleep command because it's safe and easy to manage.

Run:

sleep 100

The terminal appears to do nothing—but a process is running for 100 seconds.

Press:

Ctrl + C

to stop it.

5. Run a Process in the Background

Normally, a command occupies your terminal.

To run it in the background:

sleep 100 &

The & tells Bash:

"Start this process and immediately give me my terminal back."

You'll see something like:

[1] 3456

where 3456 is the PID.

6. jobs

Check background jobs:

jobs

Example:

[1]+ Running sleep 100 &

This shows background jobs started from your current shell.

7. fg – Bring a Job to the Foreground

If you have a background job:

fg

The process comes back to the foreground.

Stop it with:

Ctrl + C
8. Suspend a Process

Run:

sleep 100

Instead of Ctrl + C, press:

Ctrl + Z

This pauses (suspends) the process.

You'll see something like:

[1]+ Stopped sleep 100
9. bg – Resume in the Background

After suspending it:

bg

Now it's running again, but in the background.

Check:

jobs
10. kill

Find the PID:

ps -ef | grep sleep

Example:

taruni   3456  ... sleep 100

Kill it:

kill 3456

Replace 3456 with the actual PID.

11. pkill

Instead of using the PID, kill by process name:

pkill sleep

This ends all processes named sleep.
