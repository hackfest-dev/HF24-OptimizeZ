import numpy as np

class WoundAnalyzer:
    def __init__(self, current_image, previous_image=None, blood_glucose_level=100):
        """
        Initialize the WoundAnalyzer with current and previous wound images, 
        and patient's blood glucose level.
        """
        self.current_image = current_image  # Current wound image path or data
        self.previous_image = previous_image  # Previous wound image path or data
        self.blood_glucose_level = blood_glucose_level  # Patient's blood glucose level

    def severityCheck(self, area, wound_type):
        """
        Calculate wound severity based on the wound area and type.
        """
        severity_weights = {
            "bone": 4,
            "granulating": 3,
            "slough": 2,
            "eschar": 1
        }
        area = area / 100  # Normalize area to a 0–1 scale
        weighted_area = area * severity_weights[wound_type]

        severity_thresholds = {
            "high": 100,  
            "medium": 50,  
            "low": 25
        }

        if weighted_area >= severity_thresholds["high"]:
            return "high"  
        elif weighted_area >= severity_thresholds["medium"]:
            return "medium"  
        else:
            return "low"

    def analyze_wound_severity(self, area, wound_type):
        """
        Analyze the severity of the current wound based on area and type.
        """
        return self.severityCheck(area, wound_type)

    def compare_images(self, current_area, current_type, previous_area, previous_type):
        """
        Compare the previous wound image with the current wound image.
        Returns suggestions based on improvement or worsening.
        """
        if not self.previous_image:
            return "No previous image to compare."

        prev_severity = self.severityCheck(previous_area, previous_type)
        curr_severity = self.severityCheck(current_area, current_type)

        severity_order = {"low": 1, "medium": 2, "high": 3}

        if severity_order[curr_severity] < severity_order[prev_severity]:
            return {
                "message": "Wound severity has reduced. Keep following the current care routine.",
                "prev_severity": prev_severity,
                "curr_severity": curr_severity,
            }
        elif severity_order[curr_severity] > severity_order[prev_severity]:
            return {
                "message": "Wound severity has increased. Consider consulting a healthcare provider.",
                "prev_severity": prev_severity,
                "curr_severity": curr_severity,
            }
        else:
            return {
                "message": "No significant change in wound severity.",
                "prev_severity": prev_severity,
                "curr_severity": curr_severity,
            }

   

   
    def classify_wound(self, wound_duration):
        """
        Classify whether the wound is chronic or normal based on duration and severity.
        """
        if wound_duration > 4:  # Duration in weeks
            return "Chronic wound detected. Specialized care is required."
        else:
            return "Normal wound healing detected."

    def process(self, wound_duration=2, current_area=20, current_type="granulating", 
                previous_area=None, previous_type=None):
        """
        Main processing function to analyze wound and provide insights.
        """
        severity = self.analyze_wound_severity(current_area, current_type)
        comparison = self.compare_images(current_area, current_type, previous_area, previous_type)
        healing_rate = self.adjust_healing_rate()
        recommendations = self.generate_recommendations(severity)
        wound_type = self.classify_wound(wound_duration)
        
        return {
            "severity": severity,
            "comparison": comparison,
            "healing_rate": healing_rate,
            "recommendations": recommendations,
            "wound_type": wound_type,
        }

# Example Usage
if __name__ == "__main__":
    # Dummy data for wounds
    current_area = 20
    current_type = "granulating"
    previous_area = 25
    previous_type = "slough"
    blood_glucose_level = 180
    wound_duration = 6  # Duration in weeks

    # Initialize analyzer
    analyzer = WoundAnalyzer(
        current_image="path/to/current_image.jpg",
        previous_image="path/to/previous_image.jpg",
        blood_glucose_level=blood_glucose_level
    )

    # Process the wound analysis
    results = analyzer.process(wound_duration=wound_duration, current_area=current_area, 
                               current_type=current_type, previous_area=previous_area, 
                               previous_type=previous_type)
    
    # Display results
    print("Wound Analysis Results:")
    print(f"Severity: {results['severity']}")
    print(f"Comparison: {results['comparison']['message']}")
    print(f"Previous Severity: {results['comparison']['prev_severity']}")
    print(f"Current Severity: {results['comparison']['curr_severity']}")
    print(f"Healing Rate: {results['healing_rate']}")
    print(f"Recommendations: {results['recommendations']}")
    print(f"Wound Type: {results['wound_type']}")
