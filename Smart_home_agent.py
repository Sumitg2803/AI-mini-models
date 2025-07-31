# Sensor input functions (manual input simulation)
def get_temperature():
    return float(input("Enter temperature (°C): "))

def get_light_intensity():
    return int(input("Enter light intensity (in lux): "))

def get_current_hour():
    return int(input("Enter current hour (0-23): "))

# Smart agent decision logic
def smart_home_agent(temperature, light_intensity, hour):
    # Initialize device states
    fan = "OFF"
    light = "OFF"
    heater = "OFF"

    # Fan control rule
    if temperature > 28:
        fan = "ON"

    # Light control rule
    if hour >= 19 or hour < 6:  # Night time
        if light_intensity < 300:
            light = "ON"

    # Heater control rule (winter hours only)
    if (6 <= hour <= 9 or 19 <= hour <= 23) and temperature < 18:
        heater = "ON"

    return {
        "Fan": fan,
        "Light": light,
        "Heater": heater
    }

# Main function
def main():
    print("=== Smart Home Agent ===")
    temperature = get_temperature()
    light_intensity = get_light_intensity()
    hour = get_current_hour()

    status = smart_home_agent(temperature, light_intensity, hour)

    print("\n--- Device Status ---")
    for device, state in status.items():
        print(f"{device}: {state}")

if __name__ == "__main__":
    main()