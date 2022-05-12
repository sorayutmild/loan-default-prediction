import pandas as pd

def cal_revenue(total_amount, loan_duration_month, paid_month, interest_rate_peryear):
    '''
    Interest (Compound) = P(1+i)^t - P
    P = all / (1+i)^t
    '''
    principle = total_amount / (1+interest_rate_peryear)**(loan_duration_month//12)
    expected_revenue = total_amount - principle
    revenue = paid_month * expected_revenue / loan_duration_month
    return revenue

def cal_cost(loan_payment, loan_duration_month, paid_month):
    not_paid_month = loan_duration_month - paid_month
    cost = not_paid_month * loan_payment
    return cost

if __name__ == '__main__':
    df = pd.read_csv('prepared_data_beforeloan_normbyday.csv')
    after_trans_for_loan = pd.read_csv('after_trans_payment_for_loan.csv')
    df = pd.merge(df, after_trans_for_loan, how='left', on=['account_id'])
    
    df['revenue'] = cal_revenue(total_amount=df['loan_amount'], 
                loan_duration_month=df['loan_duration'], 
                paid_month=df['count_loan_trans'], 
                interest_rate_peryear=0.05)
    df['cost'] = cal_cost(loan_payment=df['loan_payments'], 
                loan_duration_month=df['loan_duration'],
                paid_month=df['count_loan_trans'])
    
    df['profit'] = df['revenue'] - df['cost']