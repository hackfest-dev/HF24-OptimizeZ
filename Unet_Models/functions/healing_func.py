def predictHealingTime(wound_type):

  healing_times = {
      "granulating": 14,
      "bone": 30,
      "eschar": 10,
      "slough": 20
  }
  
  if wound_type not in healing_times:
    return None, "Invalid wound type."


  predicted_time = healing_times[wound_type]
  

  return predicted_time

