def predict_severity(area, wound_type):


  severity_weights = {
      "bone": 4,
      "granulation": 3,
      "slough": 2,
      "eschar": 1
  }

  
  weighted_area = area * severity_weights[wound_type]

  severity_thresholds = {
      "high": 50,  
      "medium": 25,  
      "low": 0
  }

 
  if weighted_area >= severity_thresholds["high"]:
    return "high"  
  elif weighted_area >= severity_thresholds["medium"]:
    return "medium"  
  else:
    return "low"


# wound_area = 20
# wound_type = "granulation"
# severity = predict_severity(wound_area, wound_type)
# print(f"Wound severity: {severity}")
