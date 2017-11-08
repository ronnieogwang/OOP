# OOP
from assign import Banks,Tellers,Customers,Accounts,Base,Loans,Savings,Checkings,Evidence
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///class.db')
Base.metadata.bind = engine
Session = sessionmaker(bind = engine)
session = Session()
from random import *
from datetime import *


class CLI(object):
    def __init__(self,options: list):
        self.options = options

    def Enter(self):
        print('=' * 70, '\tMAC BANKING SYSTEM', '=' * 70, sep='\n')
        print('Enter the no corresponding to the desired command prompt'\
              , *self.options, sep = '\n')

    def get(self):
        print('>>>:')
        return input('')


class Bank(CLI):

    def stanbic(self):
       pass

    def centenary(self):
        pass





class Customer(CLI):

    def GeneralInquiry(self,account_no,name):
        try:
            today = date.today()
            fh = session.query(Customers).filter_by(account_no = account_no).one()

            s = session.query(Accounts).filter_by(customer_id = fh.id).one()
            print('ATM')
            print('DATE:\t{}'.format(today))
            print('\n\n\n')

            print('MAC BANKING SYSTEM\n\n\n\n\n')
            print('BALANCE INQUIRY\n\n\n\n')

            print('AVAILABLE BALANCE {}:'.format(s.amount))
        except:
            print('DATA DOES NOT EXIST IN THE SYSTEM')

    def DepositMoney(self,amount,account_no):
        try:
            f = session.query(Customers).filter_by(account_no = account_no).one()
            n = session.query(Accounts).filter_by(customer_id = f.id).one()
            n.amount = int(n.amount) + int(amount)
            session.add(n)
            session.commit()
            print('Your new balance is {} '.format(n.amount))

        except:
            print('PLEASE TRY AGAIN')

    def WithdrawMoney(self,amount,account_no,name):
        try:
            f = session.query(Customers).filter_by(account_no = account_no).one()
            n = session.query(Accounts).filter_by(customer_id = f.id).one()
            if name != f.name:
                print ('WRONG A/C NO OR NAME')
            elif int(n.amount <= 5000):
                print("You can't leave less than the creditline amount")
            else:
                n.amount = int(n.amount)-int(amount)
                session.add(n)
                session.commit()
                print()
                print('Your new Balance is {}'.format(n.amount))

        except:
            print('PLEASE CHECK YOUR CREDENTIALS')

    def OpenAccount(self,name,address,phone_no,account_type,bv):
        try:
            L = [1234, 5678, 9012, 3456, 7890, 1122, 3344, 4455, 6677, 8899,1299,2388]
            new = Customers(name = str(name), address = str(address), phone_no = phone_no,bank_id =bv )
            session.add(new)
            session.commit()
            l = session.query(Customers).filter_by(id = new.id).one()
            l.account_no = L[new.id -1]
            if account_type =='S':
                c = Savings(customer_id = new.id)
                a = Accounts(customer_id = new.id)
                a.amount = 5000
                session.add(c)
                session.commit()
                session.add(a)
                session.commit()
                print('YOUR A/C NO IS {}'.format(l.account_no))
            elif account_type =='C':
                c = Checkings(customer_id = new.id)
                a = Accounts(customer_id  = new.id)
                a.amount = 5000
                session.add(c)
                session.commit()
                session.add(a)
                session.commit()
                print('YOUR A/C NO IS {}'.format(l.account_no))
            else:
                print("YOU'VE ENTERED AN INVALID INPUT")

        except:
            print("PLEASE CHECK YOUR INPUTS")


        # print('{}, you have opened an account with {}'.format(name,b1.name))

    def CloseAccount(self,account_no,name):
        try:
            dt = session.query(Customers).filter_by(account_no=account_no).one()
            f = session.query(Accounts).filter_by(customer_id = dt.id).one()
            # i = session.query(Loans).filter_by(customer_id = dt.id).one()
            session.delete(dt)
            session.commit()
            session.delete(f)
            session.commit()

            b= []
            e =[]
            for o in session.query(Savings).all():
                b.append(o.customer_id)

            for q in session.query(Checkings).all():
                e.append(q.customer_id)

            if  dt.name != name:
                print('INVALID INPUTS')
            #
            if dt.id  in e:
                j = session.query(Checkings).filter_by(customer_id=dt.id).one()
                session.delete(j)
                session.commit()


            if dt.id  in b:
                s = session.query(Savings).filter_by(customer_id=dt.id).one()
                session.delete(s)
                session.commit()

            else:
                print('The account of {} is about to be deleted'.format(dt.name))

        except:
            print('CHECK YOUR INPUTS AND TRY AGAIN')


    def ApplyForLoan(self,name,account_no,reason,security,repayment_intervals,amount):
        n = Evidence(name = name, account_no = account_no, reason = reason, repayment_intervals = repayment_intervals,amount = amount)
        session.add(n)
        session.commit()
        print('{}\t'.format(name))
        print('\n')
        print('{}\t'.format(name))
        print('\n')
        print('{}\t'.format(name))
        print('\n')
        print('{}\t'.format(name))
        print('\n')
        print('{}\t'.format(name))
        print('\n')
        print('{}\t'.format(name))



    def RequestLoan(self,loan_type,account,loan_amount):
        try:

            y = session.query(Customers).all()
            x = []
            for f in y:
                 x.append(f.account_no)

            if not account in x :
                 print('REQUEST INVALID')
            else:
                k = session.query(Customers).filter_by(account_no = account).one()
                j = Loans(customer_id = k.id)
                j.loan_amount =loan_amount
                j.loan_type = loan_type
                j.account_no = account
                # j = Loans(loan_type = loan_type, account_no = account,loan_amount = loan_amount)
                session.add(j)
                session.commit()
                a = session.query(Accounts).filter_by(customer_id = k.id).one()
                a.amount = int(a.amount) + int(loan_amount)
                session.add(a)
                session.commit()

        except:
            print('PLEASE CHECK WHEATHER YOU HAVE AN ACCOUNT WITH US')


class Teller(CLI):




    def CollectMoney(self,account_no,amount):
        try:
            f = session.query(Customers).filter_by(account_no=account_no).one()
            n = session.query(Accounts).filter_by(customer_id=f.id).one()
            n.amount = int(n.amount) + int(amount)
            session.add(n)
            session.commit()
            print('Your new balance is {} '.format(n.amount))

        except:
            print("CHECK THE AMOUNT YOU'VE ENTERED")

    def OpenAccount(self,name,address,phone_no,account_no,account_type,bv):
        try:
            new = Customers(name=name, address=address, phone_no=phone_no, account_no=account_no,bv = bv)
            session.add(new)
            session.commit()

            if account_type =='S':
                c = Savings(customer_id = new.id)
                a = Accounts(customer_id = new.id)
                a.amount = 5000
                session.add(c)
                session.commit()
                session.add(a)
                session.commit()
                print('YOUR A/C NO IS {}'.format(account_no))
            elif account_type =='C':
                c = Checkings(customer_id = new.id)
                a = Accounts(customer_id  = new.id)
                a.amount = 5000
                session.add(c)
                session.commit()
                session.add(a)
                session.commit()
                print('YOUR A/C NO IS {}'.format(account_no))

        except:
            print('PLEASE CHECK YOUR INFORMATION')

    def CloseAccount(self,account_no,name):
        try:
            dt = session.query(Customers).filter_by(account_no=account_no).one()
            f = session.query(Accounts).filter_by(customer_id=dt.id).one()
            # i = session.query(Loans).filter_by(customer_id = dt.id).one()
            session.delete(dt)
            session.commit()
            session.delete(f)
            session.commit()

            b = []
            e = []
            for o in session.query(Savings).all():
                b.append(o.customer_id)

            for q in session.query(Checkings).all():
                e.append(q.customer_id)

            if dt.name != name:
                print('INVALID INPUTS')
            #
            if dt.id in e:
                j = session.query(Checkings).filter_by(customer_id=dt.id).one()
                session.delete(j)
                session.commit()

            if dt.id in b:
                s = session.query(Savings).filter_by(customer_id=dt.id).one()
                session.delete(s)
                session.commit()

            else:
                print('The account of {} is about to be deleted'.format(dt.name))
                session.delete(dt)
                session.commit()
                session.delete(f)
                session.commit()
        except:
            print('CHECK YOUR INPUTS AND TRY AGAIN')

        if  dt.name != name:
            print('INVALID INPUTS')


    def LoanRequest(self,loan_type,account,loan_amount):
        try:
            y = session.query(Customers).all()
            x = []
            for f in y:
                 x.append(f.account_no)

            if not account in x :
                 print('REQUEST INVALID')
            else:
                k = session.query(Customers).filter_by(account_no = account).one()
                j = Loans(customer_id = k.id)
                j.loan_amount =loan_amount
                j.loan_type = loan_type
                j.account_no = account
                # j = Loans(loan_type = loan_type, account_no = account,loan_amount = loan_amount)
                session.add(j)
                session.commit()
                a = session.query(Accounts).filter_by(customer_id = k.id).one()
                a.amount = int(a.amount) + int(loan_amount)
                session.add(a)
                session.commit()
        except:
            print('AMOUNT MUST BE INTEGERS')


    def ProvideInfo(self,teller_id,account_no):
        try:
            fh = session.query(Tellers).filter_by(id =teller_id).one()

            print('TELLER NAME')
            print(fh.name)


            today = date.today()
            fh = session.query(Customers).filter_by(account_no=account_no).one()

            s = session.query(Accounts).filter_by(customer_id=fh.id).one()
            print('MAC BANKING SYSTEM\n\n\n\n\n')
            print('ATM')
            print('DATE:\t{}'.format(today))
            print('\n\n\n')
            print('BALANCE INQUIRY\n\n\n\n')

            print('AVAILABLE BALANCE {}:'.format(s.amount))

        except:
            print('PLEASE CHECK YOUR INPUTS')

    def IssueCard(self):

        pass

class Account:

    def list(self):
        try:
            for i in session.query(Accounts).all():
                print(i.customer.account_no)
                print(i.customer.name)
        except:
            print('ERROR OCCURED')

class Loan(object):

    def list(self):
        try:
            for i in session.query(Loans).all():
                print(i.loan_type)
                print(i.customer.name)
                print(i.loan_amount)
        except:print('ERROR OCCURED')

class Checking(Account):
    try:
        def list(self):
            for i in session.query(Checkings).all():
                print(i.customer.name)
    except:
        print('ERROR OCCURED')

class Saving(Account):
    try:
        def list(self):
            for i in session.query(Saving).all():
                print(i.customer.name)
    except:
        print('ERROR')

#
if __name__ == '__main__':


    Menu = Bank((['\t1.STANBIC','\t2.CENTENARY']))
    Menu.Enter()
    userinput = Menu.get()


    if userinput == '1':
        Menu.stanbic()

        MainMenu = CLI((['\t1.ACCESS CUSTOMER DETAILS', '\t2.TELLERS MENU ', '\t3.ADMIN MENU']))
        MainMenu.Enter()
        userinput = MainMenu.get()
        if userinput == '1':

            cust = Customer((['\t1.GENERAL INQUIRY', '\t2.DEPOSIT MONEY',
                              '\t3.WITHDRAW MONEY', '\t4.OPEN ACCOUNT',
                              '\t5.CLOSE ACCOUNT', '\t6.REQUEST FOR LOAN',
                              '\t7.APPLY FOR LOAN', '\t8.GO TO PREVIOUS MENU'])
                            )
            cust.Enter()
            userinput = cust.get()
            if userinput == '1':
                ac = input('PLEASE ENTER YOUR A/C NO\t\n')
                n = input('PLEASE ENTER YOUR NAME\t\n\n')
                cust.GeneralInquiry(ac, n)

            if userinput == '2':
                am = input('ENTER AMOUNT YOU WANT TO DEPOSIT\t')
                ac = input('ENTER YOUR A/C NUMBER\t')
                cust.DepositMoney(am, ac)

            if userinput == '3':
                w = input('ENTER THE AMOUNT YOU WANT TO WITHDRAW\t')
                ac = input('ENTER YOUR A/C NUMBER')
                name = input('ENTER YOUR NAME')
                cust.WithdrawMoney(w, ac, name)

            if userinput == '4':
                na = input('ENTER YOUR NAME\t')
                ad = input('ENTER YOUR ADDRESS\t')
                f = input('ENTER YOUR PHONE_NO\t')
                t = input("ENTER 'C' OR 'S' FOR CHECKING OR SAVINGS ACCOUNT\t").upper()

                cust.OpenAccount(na, ad, f, t,bv = 1)

            if userinput == '5':
                ac = int(input('ENTER YOUR A/C NUMBER'))
                n = str(input('ENTER NAME'))
                cust.CloseAccount(ac, n)

            if userinput == '6':
                b = input('LOAN TYPE\t')
                ac = int(input("A/C NO\t"))
                m = int(input('ENTER THE AMOUNT YOU ARE APPLYING FOR\t'))
                cust.RequestLoan(b, ac, m)

            if userinput == '7':
                b = input('NAME\t')
                r = input('REASON')
                s = input('SECURITY')
                i = input('PAYMENT INTERVAL')
                a = input('A/C NO')
                m = input('ENTER THE AMOUNT')
                cust.ApplyForLoan(b, r, s, i, a, m)

        elif userinput == '2':

            tellermenu = Teller(['\t1.COLLECTMONEY', '\t2.OPENACCOUNT', \
                                 '\t3.CLOSEACCOUNT', \
                                 '\t4.LOANREQUEST', '\t5.PROVIDEINFO'])

            tellermenu.Enter()
            userinput = tellermenu.get()

            if userinput == '1':
                ac = input('ENTER THE A/C NO')
                am = input('ENTER THE AMOUNT')
                tellermenu.CollectMoney(ac, am)

            if userinput == '2':
                name = input('ENTER THE NAME')
                ad = input('ENTER THE ADDRESS')
                fn = input('ENTER THE PHONE_NO')
                ac = int(input('ENTER THE A/C NO'))
                t = input("ENTER 'S' FOR SAVINGS OR 'C' FOR CHECKING")
                tellermenu.OpenAccount(name, ad, fn, ac, t,bv =1)

            if userinput == '3':
                ac = input('ENTER THE A/C NO')
                n = input('ENTER YOUR NAME')
                tellermenu.CloseAccount(ac, n)

            if userinput == '4':
                b = input('LOAN TYPE\t')
                ac = int(input("A/C NO\t"))
                m = int(input('ENTER THE AMOUNT YOU ARE APPLYING FOR\t'))

                tellermenu.LoanRequest(b, ac, m)

            if userinput == '5':
                tellermenu.ProvideInfo(i)



        elif userinput == '3':

            admin = Account()
            admin.list()

    if userinput =='2':
        Menu.centenary()

        MainMenu = CLI((['\t1.ACCESS CUSTOMER DETAILS', '\t2.TELLERS MENU ', '\t3.ADMIN MENU']))
        MainMenu.Enter()
        userinput = MainMenu.get()
        if userinput == '1':

            cust = Customer((['\t1.GENERAL INQUIRY', '\t2.DEPOSIT MONEY',
                              '\t3.WITHDRAW MONEY', '\t4.OPEN ACCOUNT',
                              '\t5.CLOSE ACCOUNT','\t6.REQUEST FOR LOAN',
                              '\t7.APPLY FOR LOAN','\t8.GO TO PREVIOUS MENU'])
                            )
            cust.Enter()
            userinput = cust.get()
            if userinput == '1':
                ac = input('PLEASE ENTER YOUR A/C NO\t\n')
                n = input('PLEASE ENTER YOUR NAME\t\n\n')
                cust.GeneralInquiry(ac, n)

            if userinput == '2':
                am = input('ENTER AMOUNT YOU WANT TO DEPOSIT\t')
                ac = input('ENTER YOUR A/C NUMBER\t')
                cust.DepositMoney(am, ac)

            if userinput == '3':
                w = input('ENTER THE AMOUNT YOU WANT TO WITHDRAW\t')
                ac = input('ENTER YOUR A/C NUMBER')
                name = input('ENTER YOUR NAME')
                cust.WithdrawMoney(w, ac, name)

            if userinput == '4':
                na = input('ENTER YOUR NAME\t')
                ad = input('ENTER YOUR ADDRESS\t')
                f = input('ENTER YOUR PHONE_NO\t')
                t = input("ENTER 'C' OR 'S' FOR CHECKING OR SAVINGS ACCOUNT\t").upper()

                cust.OpenAccount(na, ad, f, t,bv = 2)

            if userinput == '5':
                ac = int(input('ENTER YOUR A/C NUMBER'))
                n = str(input('ENTER NAME'))
                cust.CloseAccount(ac,n)

            if userinput == '6':
                b = input('LOAN TYPE\t')
                ac = int(input("A/C NO\t"))
                m = int(input('ENTER THE AMOUNT YOU ARE APPLYING FOR\t'))
                cust.RequestLoan(b,ac,m)

            if userinput == '7':
                b = input('NAME\t')
                r= input('REASON')
                s = input('SECURITY')
                i = input('PAYMENT INTERVAL')
                a = input('A/C NO')
                m = input('ENTER THE AMOUNT')
                cust.ApplyForLoan(b,r,s,i,a,m)

        elif userinput == '2':

                tellermenu = Teller(['\t1.COLLECTMONEY', '\t2.OPENACCOUNT', \
                                     '\t3.CLOSEACCOUNT', \
                                     '\t4.LOANREQUEST', '\t5.PROVIDEINFO'])

                tellermenu.Enter()
                userinput = tellermenu.get()

                if userinput == '1':
                    ac = input('ENTER THE A/C NO')
                    am = input('ENTER THE AMOUNT')
                    tellermenu.CollectMoney(ac, am)

                if userinput == '2':
                    name = input('ENTER THE NAME')
                    ad = input('ENTER THE ADDRESS')
                    fn = input('ENTER THE PHONE_NO')
                    ac = int(input('ENTER THE A/C NO'))
                    t =input("ENTER 'S' FOR SAVINGS OR 'C' FOR CHECKING").upper()
                    tellermenu.OpenAccount(name,ad,fn,ac,bv=2)

                if userinput == '3':
                    ac = input('ENTER THE A/C NO')
                    n = input('ENTER YOUR NAME')
                    tellermenu.CloseAccount(ac,n)


                if userinput == '4':
                    b = input('LOAN TYPE\t')
                    ac = int(input("A/C NO\t"))
                    m = int(input('ENTER THE AMOUNT YOU ARE APPLYING FOR\t'))

                    tellermenu.LoanRequest(b,ac,m)


                if userinput == '5':
                    tellermenu.ProvideInfo(i)



        elif userinput == '3' :

            admin = Account()
            admin.list()

        elif userinput =='4':
            admin = Loan()
            admin.list()

        elif userinput =='5':
            admin = Checking()
            admin.list()

        elif userinput =='6':
            admin = Saving()
            admin.list()
