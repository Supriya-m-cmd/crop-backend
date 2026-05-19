from utils.soil_lookup import get_soil_data


district = "Dharwad"


soil_data = get_soil_data(
    district
)


print("\n===== SOIL DATA =====\n")

print(soil_data)