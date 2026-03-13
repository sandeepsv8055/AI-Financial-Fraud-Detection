import datetime


def fraud_alert(transaction, risk_score=None):

    timestamp = datetime.datetime.now()

    print("\n🚨 FRAUD ALERT 🚨")
    print("Time:", timestamp)
    print("Transaction Data:", transaction)

    if risk_score:
        print("Risk Score:", risk_score, "%")

    print("Action: Transaction flagged for review\n")