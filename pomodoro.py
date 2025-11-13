
import time
import sys

def format_time(seconds):
    m = seconds // 60
    s = seconds % 60
    return f"{int(m):02d}:{int(s):02d}"

def countdown(total_seconds, label="Time"):
    try:
        start = time.perf_counter()
        end = start + total_seconds
        while True:
            now = time.perf_counter()
            remaining = int(round(end - now))
            if remaining < 0:
                break
            print(f"\r{label} - {format_time(remaining)}", end="", flush=True)
            # sleep a bit but responsive
            time.sleep(0.2)
        print(f"\r{label} - 00:00")
        # beep if possible
        try:
            print("\a", end="", flush=True)
        except Exception:
            pass
    except KeyboardInterrupt:
        print("\nTimer cancelled.")
        return False
    return True

def run_pomodoro(work_min=25, break_min=5, cycles=4):
    print(f"Starting Pomodoro: {cycles} cycles of {work_min}m work + {break_min}m break.")
    for i in range(1, cycles + 1):
        print(f"\nCycle {i} — Work for {work_min} minutes.")
        finished = countdown(work_min * 60, label=f"Work {i}")
        if not finished:
            break
        print("Work session complete. Take a break!")
        countdown(break_min * 60, label=f"Break {i}")
    print("\nPomodoro finished. Great job!")

def main():
    print("Pomodoro / Countdown Timer")
    mode = input("Choose mode: (1) Countdown (2) Pomodoro [default 2]: ").strip() or "2"
    if mode == "1":
        try:
            mins = float(input("Enter minutes to count down (e.g. 1.5 for 90s): ").strip())
            if mins <= 0:
                print("Minutes must be positive.")
                return
        except ValueError:
            print("Invalid number.")
            return
        print(f"Starting countdown for {mins} minutes.")
        countdown(int(round(mins * 60)), label="Countdown")
        print("Time's up!")
    else:
        try:
            work = int(input("Work minutes (default 25): ").strip() or "25")
            brk = int(input("Break minutes (default 5): ").strip() or "5")
            cycles = int(input("Number of cycles (default 4): ").strip() or "4")
        except ValueError:
            print("Invalid integer.")
            return
        run_pomodoro(work, brk, cycles)

if __name__ == "__main__":
    main()
