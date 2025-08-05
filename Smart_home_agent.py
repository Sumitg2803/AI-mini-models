
def get_temperature():
    return float(input("Enter temperature (°C): "))

def get_light_intensity():
    return int(input("Enter light intensity (in lux): "))

def get_current_hour():
    return int(input("Enter current hour (0-23): "))


def smart_home_agent(temperature, light_intensity, hour):

    fan = "OFF"
    light = "OFF"
    heater = "OFF"


    if temperature > 28:
        fan = "ON"


    if hour >= 19 or hour < 6: 
        if light_intensity < 300:
            light = "ON"


    if (6 <= hour <= 9 or 19 <= hour <= 23) and temperature < 18:
        heater = "ON"

    return {
        "Fan": fan,
        "Light": light,
        "Heater": heater
    }

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