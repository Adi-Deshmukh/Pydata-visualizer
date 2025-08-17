

# we give column details as the input
def generate_alerts(column_details, settings=None):
    alerts = []
    
    skewness = column_details.get("skewness")
    
    if skewness is not None:
        if abs(skewness)> settings.skewness_threshold:
            new_alert = {
                "alert_type":"skewness",
                "message": f"Data is highly skewed (value: {skewness:.2f})",
                "value": skewness
            }
            
            alerts.append(new_alert)
            
    missing_percent = column_details.get("missing_%")
    if missing_percent is not None:
        if missing_percent > 20 :
            new_alert = {
                "alert_type":"High Missing Values",
                "message": f"Data is highly Missing (value: {missing_percent:.2f})",
                "value": missing_percent
                
            }

            alerts.append(new_alert)
    
    
    
    return alerts
    


