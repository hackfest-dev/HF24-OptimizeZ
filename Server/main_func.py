# from healing_func import predictHealingTime
# from phy_func import phyParams
# from geo_func import geoParams
# from severity_func import severityCheck
# import json
# import os

# def main_mod():
#     image_path = "Image/wound_ana.jpg"
#     h, w, area, perimeter = geoParams(image_path)
#     woundType = phyParams(image_path)
#     severity = severityCheck(area, woundType)
#     healingTime = predictHealingTime(woundType)
    
#     # Create a dictionary with the collected data
#     data = {
#         "area": area,
#         "h": h,
#         "w": w,
#         "woundType": woundType,
#         "severity": severity,
#         "healingTime": healingTime
#     }
    
#     # Specify the output directory
#     output_directory = "output"
#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     # Save the data as JSON
#     output_path = os.path.join(output_directory, "output.json")
#     with open(output_path, 'w') as json_file:
#         json.dump(data, json_file)
    
#     print(f"JSON data saved to: {output_path}")

# if __name__ == "__main__":
#     main()
# existing code above


from new import WoundAnalyzer  # Importing the WoundAnalyzer class
from healing_func import predictHealingTime
from phy_func import phyParams
from geo_func import geoParams
from severity_func import severityCheck
import json
import os

def main_mod():
    # Paths for current and previous images
    current_image_path = "Image/wound_ana.jpg"
    previous_image_path = "Image/previous_wound.jpg"
    blood_glucose_level = 180  # Example glucose level
    wound_duration = 6  # Duration in weeks

    # Initialize WoundAnalyzer
    analyzer = WoundAnalyzer(
        current_image=current_image_path,
        previous_image=previous_image_path,
        blood_glucose_level=blood_glucose_level
    )

    # Analyze wound using existing functions
    h, w, area, perimeter = geoParams(current_image_path)
    woundType = phyParams(current_image_path)
    severity = severityCheck(area, woundType)
    healingTime = predictHealingTime(woundType)
    
    # Analyze wound using new functionalities
    results = analyzer.process(wound_duration=wound_duration)

    # Combine data from both sources
    combined_data = {
        "area": area,
        "height": h,
        "width": w,
        "woundType": woundType,
        "severity": severity,
        "healingTime": healingTime,
        "analyzer_severity": results["severity"],
        "comparison_message": results["comparison"]["message"],
        "previous_severity": results["comparison"]["prev_severity"],
        "current_severity": results["comparison"]["curr_severity"],
        "healing_rate": results["healing_rate"],
        "recommendations": results["recommendations"],
        "wound_type_classification": results["wound_type"]
    }

    # Specify the output directory
    output_directory = "output"
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Save the combined data as JSON
    output_path = os.path.join(output_directory, "output.json")
    with open(output_path, 'w') as json_file:
        json.dump(combined_data, json_file, indent=4)
    
    print(f"JSON data saved to: {output_path}")

if __name__ == "__main__":
    main_mod()
