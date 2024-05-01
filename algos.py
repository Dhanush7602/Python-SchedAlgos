def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    return waiting_time, turnaround_time

def sjf(processes):
    processes.sort(key=lambda x: x[1])
    return fcfs(processes)

def sjs(processes):
    processes.sort(key=lambda x: x[1], reverse=True)
    return fcfs(processes)

def priority_scheduling(processes):
    processes.sort(key=lambda x: x[2])
    return fcfs(processes)

def shortest_remaining_time(processes):
    processes.sort(key=lambda x: x[1])
    return sjf(processes)

def round_robin(processes, quantum_time):
    n = len(processes)
    remaining_burst_time = [process[1] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > quantum_time:
                    time += quantum_time
                    remaining_burst_time[i] -= quantum_time
                else:
                    time += remaining_burst_time[i]
                    waiting_time[i] = time - processes[i][1]
                    remaining_burst_time[i] = 0

        if done:
            break

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    return waiting_time, turnaround_time

def calculate_average_waiting_time(waiting_times):
    return sum(waiting_times) / len(waiting_times)

def calculate_average_turnaround_time(turnaround_times):
    return sum(turnaround_times) / len(turnaround_times)

# Example usage:

def main():
    n = int(input("Enter the number of processes: "))

    processes = []
    for i in range(n):
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        priority = int(input(f"Enter priority for process {i + 1}: "))
        processes.append((i + 1, burst_time, arrival_time, priority))

    quantum_time = int(input("Enter the quantum time for Round Robin scheduling: "))

    print("\nFCFS Scheduling:")
    wt_fcfs, tat_fcfs = fcfs(processes)
    print("Waiting Time:", wt_fcfs)
    print("Turnaround Time:", tat_fcfs)

    print("\nSJF Scheduling:")
    wt_sjf, tat_sjf = sjf(processes)
    print("Waiting Time:", wt_sjf)
    print("Turnaround Time:", tat_sjf)

    print("\nSJS Scheduling:")
    wt_sjs, tat_sjs = sjs(processes)
    print("Waiting Time:", wt_sjs)
    print("Turnaround Time:", tat_sjs)

    print("\nPriority Scheduling:")
    wt_priority, tat_priority = priority_scheduling(processes)
    print("Waiting Time:", wt_priority)
    print("Turnaround Time:", tat_priority)

    print("\nShortest Remaining Time Scheduling:")
    wt_srt, tat_srt = shortest_remaining_time(processes)
    print("Waiting Time:", wt_srt)
    print("Turnaround Time:", tat_srt)

    print("\nRound Robin Scheduling:")
    wt_rr, tat_rr = round_robin(processes, quantum_time)
    print("Waiting Time:", wt_rr)
    print("Turnaround Time:", tat_rr)

    avg_waiting_time = calculate_average_waiting_time(wt_fcfs)
    avg_turnaround_time = calculate_average_turnaround_time(tat_fcfs)
    print("\nAverage Waiting Time (FCFS):", avg_waiting_time)
    print("Average Turnaround Time (FCFS):", avg_turnaround_time)

if __name__ == "__main__":
    main()
