def water_lose_calculation(weight, activity_level, temperature):
    """
    Calculate the amount of water lost based on weight, activity level, and temperature.

    Parameters:
    weight (float): The weight of the individual in kilograms.
    activity_level (str): The activity level ('low', 'moderate', 'high').
    temperature (float): The ambient temperature in degrees Celsius.

    Returns:
    float: Estimated water loss in liters.
    """
    # Base water loss calculation based on weight
    base_loss = weight * 0.03  # 3% of body weight

    # Adjust for activity level
    if activity_level == 'low':
        activity_multiplier = 1.0
    elif activity_level == 'moderate':
        activity_multiplier = 1.5
    elif activity_level == 'high':
        activity_multiplier = 2.0
    else:
        raise ValueError("Invalid activity level. Choose from 'low', 'moderate', or 'high'.")

    # Adjust for temperature
    if temperature < 20:
        temp_multiplier = 1.0
    elif 20 <= temperature < 30:
        temp_multiplier = 1.2
    else:  # temperature >= 30
        temp_multiplier = 1.5

    # Total water loss calculation
    total_loss = base_loss * activity_multiplier * temp_multiplier

    return total_loss

user_input_weight = float(input("Enter your weight in kg: "))
user_input_activity_level = input("Enter your activity level (low, moderate, high): ")
user_input_temperature = float(input("Enter the ambient temperature in °C: "))
water_loss = water_lose_calculation(user_input_weight, user_input_activity_level, 25)  # Assuming a temperature of 25°C
print(f"Estimated water loss: {water_loss:.2f} liters")

water_lose_calculation(user_input_weight, user_input_activity_level, user_input_temperature)  # Example usage


