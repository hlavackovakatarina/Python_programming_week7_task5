WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
        
def main ():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f"Reading file \"{filename}\"")
    analyse(filename)
    print("Program ending.")

def analyse(filename):
    print("Analysing timestamps.")
    print("Displaying results.\n### Electricity consumption summary ###")
    daily_usage = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    daily_cost = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    with open(filename, "r") as file:
        file.readline()
        for row in file:
            part = row.strip().split(";")
            day = part [0]
            usage = float(part [2])
            price = float(part [3])
            for j in range(len(WEEKDAYS)):
                if day == WEEKDAYS[j]:
                    daily_usage[j] += usage
                    daily_cost[j] += usage * price

    for i in range(len(WEEKDAYS)):
        print(f"- {WEEKDAYS[i]} usage {daily_usage[i]:.2f} kWh, cost {daily_cost[i]:.2f} €")
        
    print("### Electricity consumption summary ###")

if __name__ == "__main__":
    main()