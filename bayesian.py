def validate_input(label):
    while True: 
        try:
            user_input = float(input(f"{label} = "))
            break
        except ValueError:
            print("Invalid entry, please type a number")
    return user_input

def bayesian(prior, likelihood, evidence):
    posterior = prior * likelihood / evidence
    return posterior

prior = validate_input("prior")
likelihood = validate_input("likelihood")
evidence = validate_input("evidence")

print("Result is =", bayesian(prior, likelihood, evidence))
