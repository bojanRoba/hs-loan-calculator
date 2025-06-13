# write your code here
import argparse, math

parser = argparse.ArgumentParser(description="Annuity / Differentiate Payment Calculator")

parser.add_argument('--type', type=str, help="Type of Payment")
parser.add_argument("--payment", type=float, help="Monthly payment amount")
parser.add_argument('--principal', type=float, help="Loan principle amount")
parser.add_argument('--periods', type=int, help="Number of months to repay loan")
parser.add_argument('--interest', type=float, help="Annual interest rate")

args = parser.parse_args()

if args.interest is None:
    print("Incorrect parameters")
    exit()

else:
    nominal_interest = args.interest / 12 / 100

if args.type == 'annuity':

    if args.payment is None and args.principal > 0 and args.periods > 0:
        payment = args.principal * ((nominal_interest * math.pow(1 + nominal_interest, args.periods)) /
                                    (math.pow(1 + nominal_interest, args.periods) - 1))
        print(f"Your monthly payment is $ {math.ceil(payment)}!")

        overpayment = (args.periods * math.ceil(payment)) - args.principal

    elif args.principal is None and args.periods > 0 and args.payment > 0:
        principal = args.payment / ((nominal_interest * math.pow(1 + nominal_interest, args.periods))/
                                    (math.pow(1 + nominal_interest, args.periods) - 1))
        print(f"Your loan principal is $ {int(principal)}!")

        overpayment = (args.periods * args.payment) - int(principal)

    elif args.periods is None and args.principal > 0 and args.payment > 0:
        periods = math.log(args.payment / (args.payment - nominal_interest * args.principal), 1 + nominal_interest)
        periods = math.ceil(periods)
        years, months = divmod(periods, 12)

        overpayment = (periods * args.payment) - args.principal

        if years > 0:
            if months > 0:
                print(f"It will take {years} year{'s' if years > 1 else ''} to repay this loan!")
            else:
                print(f"It will take {years} year{'s' if years > 1 else ''} to repay this loan!")
            # It will take Y year('s)( and M month(s)) to repay this loan!

        else:
            print(f"It will take {months} month{'s' if months > 1 else ''} to repay this loan!")
            # It will take M month(s) to repay this loan!
    else:
        print("Incorrect parameters")
        exit()

    print(f'Overpayment is {math.ceil(overpayment)}')

elif args.type == 'diff' and args.principal > 0 and args.periods > 0 and args.interest > 0:
    nominal_interest = args.interest / 12 / 100

    if args.payment is not None:
        print("For --type=diff combination with --payment is invalid. Please try again! RobaRoba")
        exit()

    else:
        sum_payments = 0
        for diff_month in range(1, args.periods + 1):
            diff_payment = ((args.principal / args.periods) +
                            nominal_interest * (args.principal - ((args.principal * (diff_month - 1)) / args.periods)))
            sum_payments += math.ceil(diff_payment)
            print(f'Month {diff_month}: payment is {math.ceil(diff_payment)}')

    overpayment = round(sum_payments - args.principal)
    print(f'Overpayment is {overpayment}')

else:
    print("Incorrect parameters")
    exit()