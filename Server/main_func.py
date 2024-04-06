from healing_func import predictHealingTime
from phy_func import phyParams
from geo_func import geoParams
from severity_func import severityCheck
import json
import os

def main():
    image_path = "Image/wound_ana.jpg"
    h, w, area, perimeter = geoParams(image_path)
    woundType = phyParams(image_path)
    severity = severityCheck(area, woundType)
    healingTime = predictHealingTime(woundType)
    
    # Create a dictionary with the collected data
    data = {
        "area": area,
        "h": h,
        "w": w,
        "woundType": woundType,
        "severity": severity,
        "healingTime": healingTime
    }
    
    # Specify the output directory
    output_directory = "Server/output"
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Save the data as JSON
    output_path = os.path.join(output_directory, "output.json")
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file)
    
    print(f"JSON data saved to: {output_path}")

if __name__ == "__main__":
    main()
