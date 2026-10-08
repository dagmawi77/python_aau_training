
#the Module containes Workflow used in AAWSA
def vaildate_usage_value(value):
    if value is None:
        return False
    elif not isinstance(value, (int, float)):
        return False
    elif value < 0:
        return False
    else:
        return True
def calculate_bill(usage_in_m3):
    if vaildate_usage_value(usage_in_m3):
        usage_bill = usage_in_m3 * 22.0
    else:
        usage_bill = None
        print("Invalid usage value. Please provide a non-negative number.")
    return usage_bill
def estimate_water_lose(production, billed_consmption):
    if vaildate_usage_value(production) and vaildate_usage_value(billed_consmption):
        if billed_consmption <= production:
            water_loss = production - billed_consmption
        else:
            print("Billed consumption cannot be greater than production. Please provide valid values.")
            water_loss = None
    else:
        water_loss = None
        print("Invalid production or billed consumption value. Please provide non-negative numbers.")
    return water_loss



