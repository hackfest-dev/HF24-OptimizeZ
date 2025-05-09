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
    
    def predict_severity(self, image):
        """
        Placeholder for wound severity prediction based on image analysis.
        Replace this with an actual ML model.
        """
        # Simulate severity prediction (scale: 0–100)
        severity_score = np.random.randint(0, 100)
        return severity_score

    def analyze_wound_severity(self):
        """
        Analyze the severity of the current wound image.
        """
        return self.predict_severity(self.current_image)
    
    def compare_images(self):
        """
        Compare the previous wound image with the current wound image.
        Returns suggestions based on improvement or worsening.
        """
        if not self.previous_image:
            return "No previous image to compare."
        
        prev_severity = self.predict_severity(self.previous_image)
        curr_severity = self.analyze_wound_severity()
        
        if curr_severity < prev_severity:
            return {
                "message": "Wound severity has reduced. Keep following the current care routine.",
                "prev_severity": prev_severity,
                "curr_severity": curr_severity,
            }
        elif curr_severity > prev_severity:
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

    def adjust_healing_rate(self):
        """
        Adjust the healing rate based on the blood glucose level.
        """
        if self.blood_glucose_level < 140:
            return "Normal healing rate expected."
        elif 140 <= self.blood_glucose_level <= 199:
            return "Healing rate is slightly slower due to elevated blood glucose."
        else:
            return "Healing rate is significantly reduced. Monitor the wound closely."
    
    def generate_recommendations(self, severity):
        """
        Generate wound care recommendations based on severity.
        """
        if severity < 30:
            return "Mild wound: Clean and dress regularly. Use antiseptic."
        elif 30 <= severity < 70:
            return ("Moderate wound: Use advanced dressings, ensure wound is dry and infection-free, "
                    "and monitor healing progress closely.")
        else:
            return ("Severe wound: Seek medical attention immediately. Consider advanced therapies "
                    "and regular monitoring.")

    def classify_wound(self, wound_duration):
        """
        Classify whether the wound is chronic or normal based on duration and severity.
        """
        if wound_duration > 4:  # Duration in weeks
            return "Chronic wound detected. Specialized care is required."
        else:
            return "Normal wound healing detected."

    def process(self, wound_duration=2):
        """
        Main processing function to analyze wound and provide insights.
        """
        severity = self.analyze_wound_severity()
        comparison = self.compare_images()
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
    # Dummy images for current and previous wound
    current_image = "path/to/current_image.jpg"
    previous_image = "path/to/previous_image.jpg"
    blood_glucose_level = 180
    wound_duration = 6  # Duration in weeks
    
    # Initialize analyzer
    analyzer = WoundAnalyzer(
        current_image=current_image,
        previous_image=previous_image,
        blood_glucose_level=blood_glucose_level
    )
    
    # Process the wound analysis
    results = analyzer.process(wound_duration=wound_duration)
    
    # Display results
    print("Wound Analysis Results:")
    print(f"Severity Score: {results['severity']}")
    print(f"Comparison: {results['comparison']['message']}")
    print(f"Previous Severity: {results['comparison']['prev_severity']}")
    print(f"Current Severity: {results['comparison']['curr_severity']}")
    print(f"Healing Rate: {results['healing_rate']}")
    print(f"Recommendations: {results['recommendations']}")
    print(f"Wound Type: {results['wound_type']}")
