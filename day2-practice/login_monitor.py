def check_login(attempts):
    print("AI SECURITY LOGIN MONITOR")
    print("-------------------------")

    print("Failed login attempts:", attempts)

    if attempts >= 5:
        print("ALERT: Suspicious login activity detected!")
    else:
        print("Status: Login activity normal.")


attempts = int(input("Enter failed login attempts: "))
check_login(attempts)
