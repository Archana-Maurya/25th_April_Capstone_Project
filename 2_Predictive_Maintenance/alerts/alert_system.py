def send_alert(failure_prediction, probability):
    if failure_prediction == 1:
        print("ALERT: Machine Failure Predicted!")
        print("Failure Probability:", probability)
        print("Maintenance Team Notified Successfully")
    else:
        print("Machine is operating normally")


# Example test
send_alert(0, 0.97)