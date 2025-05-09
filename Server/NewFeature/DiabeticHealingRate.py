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