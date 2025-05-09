 def generate_recommendations(self, severity):
        """
        Generate wound care recommendations based on severity.
        """
        if severity == "low":
            return "Mild wound: Clean and dress regularly. Use antiseptic."
        elif severity == "medium":
            return ("Moderate wound: Use advanced dressings, ensure wound is dry and infection-free, "
                    "and monitor healing progress closely.")
        else:
            return ("Severe wound: Seek medical attention immediately. Consider advanced therapies "
                    "and regular monitoring.")
