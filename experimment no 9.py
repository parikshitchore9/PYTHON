#question no 1

import simpy
import random
import statistics

# Simulation parameters
RANDOM_SEED = 42
ARRIVAL_RATE = 1 / 5      # Average 1 customer every 5 minutes
SERVICE_RATE = 1 / 4      # Average service time = 4 minutes
SIM_TIME = 500            # Total simulation time

# Lists to store statistics
waiting_times = []
system_times = []

random.seed(RANDOM_SEED)


def customer(env, name, server):
    """Customer process."""
    arrival_time = env.now

    # Request the server
    with server.request() as request:
        yield request

        # Calculate waiting time
        wait = env.now - arrival_time
        waiting_times.append(wait)

        # Service time
        service_time = random.expovariate(SERVICE_RATE)
        yield env.timeout(service_time)

        # Total time in system
        total_time = env.now - arrival_time
        system_times.append(total_time)

        print(
            f"{name} arrived at {arrival_time:.2f}, "
            f"waited {wait:.2f}, "
            f"departed at {env.now:.2f}"
        )


def customer_generator(env, server):
    """Generate customers."""
    customer_id = 0

    while True:
        interarrival = random.expovariate(ARRIVAL_RATE)
        yield env.timeout(interarrival)

        customer_id += 1
        env.process(customer(env, f"Customer {customer_id}", server))


# Create environment
env = simpy.Environment()

# Single server
server = simpy.Resource(env, capacity=1)

# Start customer arrivals
env.process(customer_generator(env, server))

# Run simulation
env.run(until=SIM_TIME)

#question no 2
import simpy
import random
import statistics

# Common parameters
RANDOM_SEED = 42
ARRIVAL_RATE = 1 / 5      # Average arrival every 5 minutes
SERVICE_RATE = 1 / 4      # Average service time = 4 minutes
SIM_TIME = 500


def customer(env, name, server, waiting_times, system_times):
    """Customer process."""
    arrival_time = env.now

    with server.request() as request:
        yield request

        # Waiting time in queue
        wait = env.now - arrival_time
        waiting_times.append(wait)

        # Service
        service_time = random.expovariate(SERVICE_RATE)
        yield env.timeout(service_time)

        # Total time in system
        system_times.append(env.now - arrival_time)


def customer_generator(env, server, waiting_times, system_times):
    """Generate customers."""
    customer_id = 0

    while True:
        interarrival = random.expovariate(ARRIVAL_RATE)
        yield env.timeout(interarrival)

        customer_id += 1
        env.process(
            customer(
                env,
                f"Customer {customer_id}",
                server,
                waiting_times,
                system_times
            )
        )


def run_simulation(num_servers):
    """Run queue simulation with specified number of servers."""
    random.seed(RANDOM_SEED)

    env = simpy.Environment()

    waiting_times = []
    system_times = []

    server = simpy.Resource(env, capacity=num_servers)

    env.process(
        customer_generator(
            env,
            server,
            waiting_times,
            system_times
        )
    )

    env.run(until=SIM_TIME)

    return {
        "servers": num_servers,
        "customers": len(waiting_times),
        "avg_wait": statistics.mean(waiting_times),
        "avg_system": statistics.mean(system_times),
        "max_wait": max(waiting_times)
    }


# Run simulations
single_server = run_simulation(1)
two_servers = run_simulation(2)

# Display results
print("QUEUE COMPARISON")
print("-" * 50)

print("\nSingle-Server System (M/M/1)")
print(f"Customers served : {single_server['customers']}")
print(f"Average wait     : {single_server['avg_wait']:.2f} min")
print(f"Average system   : {single_server['avg_system']:.2f} min")
print(f"Maximum wait     : {single_server['max_wait']:.2f} min")

print("\nTwo-Server System (M/M/2)")
print(f"Customers served : {two_servers['customers']}")
print(f"Average wait     : {two_servers['avg_wait']:.2f} min")
print(f"Average system   : {two_servers['avg_system']:.2f} min")
print(f"Maximum wait     : {two_servers['max_wait']:.2f} min")

print("\nImprovement")
improvement = (
    (single_server['avg_wait'] - two_servers['avg_wait'])
    / single_server['avg_wait']
) * 100

print(f"Reduction in average waiting time: {improvement:.2f}%")

#question no 3
import simpy
import random
import statistics

# Simulation settings
SIM_TIME = 500
RANDOM_SEED = 42
NUM_SERVERS = 2


def run_simulation(mean_interarrival, mean_service, num_servers=2):
    """
    Simulates a queueing system and returns performance metrics.
    """

    arrival_rate = 1 / mean_interarrival
    service_rate = 1 / mean_service

    random.seed(RANDOM_SEED)

    env = simpy.Environment()

    waiting_times = []
    system_times = []

    server = simpy.Resource(env, capacity=num_servers)

    def customer(env, name):
        arrival_time = env.now

        with server.request() as request:
            yield request

            # Waiting time in queue
            wait = env.now - arrival_time
            waiting_times.append(wait)

            # Service time
            service_time = random.expovariate(service_rate)
            yield env.timeout(service_time)

            # Total time in system
            total_time = env.now - arrival_time
            system_times.append(total_time)

    def customer_generator(env):
        customer_id = 0

        while True:
            interarrival = random.expovariate(arrival_rate)
            yield env.timeout(interarrival)

            customer_id += 1
            env.process(customer(env, f"Customer {customer_id}"))

    env.process(customer_generator(env))
    env.run(until=SIM_TIME)

    return {
        "customers_served": len(waiting_times),
        "avg_wait": statistics.mean(waiting_times),
        "avg_system": statistics.mean(system_times),
        "max_wait": max(waiting_times),
    }


# Different scenarios to study
scenarios = [
    ("Base Case", 5, 4),
    ("Higher Arrival Rate", 3, 4),
    ("Lower Arrival Rate", 8, 4),
    ("Faster Service", 5, 2),
    ("Slower Service", 5, 6)
]

print("=" * 70)
print("SIMPY QUEUE PERFORMANCE ANALYSIS (TWO-SERVER SYSTEM)")
print("=" * 70)

for name, interarrival, service in scenarios:

    results = run_simulation(
        mean_interarrival=interarrival,
        mean_service=service,
        num_servers=NUM_SERVERS
    )

    print(f"\nScenario: {name}")
    print("-" * 50)
    print(f"Mean Interarrival Time : {interarrival} min")
    print(f"Mean Service Time      : {service} min")
    print(f"Customers Served       : {results['customers_served']}")
    print(f"Average Waiting Time   : {results['avg_wait']:.2f} min")
    print(f"Average System Time    : {results['avg_system']:.2f} min")
    print(f"Maximum Waiting Time   : {results['max_wait']:.2f} min")

print("\n" + "=" * 70)
print("ANALYSIS")
print("=" * 70)
print("1. Shorter interarrival times increase congestion and waiting.")
print("2. Longer service times increase queue length and delay.")
print("3. Faster service reduces waiting and total system time.")
print("4. Lower arrival rates lead to minimal queueing.")
print("5. System performance worsens as server utilization increases.")

# Question no 4
import simpy
import random
import statistics

# Simulation Parameters
RANDOM_SEED = 42
SIM_TIME = 500
NUM_SERVERS = 2

# Mean times (in minutes)
MEAN_INTERARRIVAL = 5
MEAN_SERVICE = 4

ARRIVAL_RATE = 1 / MEAN_INTERARRIVAL
SERVICE_RATE = 1 / MEAN_SERVICE

# Store waiting times
waiting_times = []


def customer(env, name, server):
    """Customer process."""
    arrival_time = env.now

    # Request a server
    with server.request() as request:
        yield request

        # Calculate waiting time
        waiting_time = env.now - arrival_time
        waiting_times.append(waiting_time)

        print(f"{name} arrived at {arrival_time:.2f}, "
              f"waited {waiting_time:.2f} minutes")

        # Service time
        service_time = random.expovariate(SERVICE_RATE)
        yield env.timeout(service_time)


def customer_generator(env, server):
    """Generate customers."""
    customer_id = 0

    while True:
        interarrival_time = random.expovariate(ARRIVAL_RATE)
        yield env.timeout(interarrival_time)

        customer_id += 1
        env.process(customer(env, f"Customer {customer_id}", server))


# Set random seed
random.seed(RANDOM_SEED)

# Create simulation environment
env = simpy.Environment()

# Create a two-server resource
server = simpy.Resource(env, capacity=NUM_SERVERS)

# Start customer arrivals
env.process(customer_generator(env, server))

# Run simulation
env.run(until=SIM_TIME)

# Calculate and display average waiting time
print("\n" + "=" * 50)
print("SIMULATION RESULTS")
print("=" * 50)

if waiting_times:
    avg_wait = statistics.mean(waiting_times)
    max_wait = max(waiting_times)
    min_wait = min(waiting_times)

    print(f"Total Customers Served : {len(waiting_times)}")
    print(f"Average Waiting Time   : {avg_wait:.2f} minutes")
    print(f"Maximum Waiting Time   : {max_wait:.2f} minutes")
    print(f"Minimum Waiting Time   : {min_wait:.2f} minutes")
else:
    print("No customers were served.")