from tkinter import *
import random
import time
import datetime
import sqlite3

# Initialize the main window
payroll = Tk()
payroll.geometry("895x525+0+0")
payroll.title("PMS - Payroll Systems")


# Database connection
def connect_db():
    conn = sqlite3.connect("database/payroll.db")
    return conn


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS payroll_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        employee_name TEXT,
                        address TEXT,
                        reference TEXT,
                        employer_name TEXT,
                        email TEXT,
                        job_status TEXT,
                        city_weighting REAL,
                        basic_salary REAL,
                        overtime REAL,
                        gross_pay REAL,
                        net_pay REAL,
                        tax REAL,
                        pension REAL,
                        student_loan REAL,
                        ni_payment REAL,
                        deductions REAL,
                        postcode TEXT,
                        gender TEXT,
                        grade TEXT,
                        department TEXT,
                        pay_date TEXT,
                        tax_period INTEGER,
                        ni_number TEXT,
                        ni_code TEXT,
                        taxable_pay REAL,
                        pension_pay REAL,
                        other_payment_due REAL
                    )''')
    conn.commit()
    conn.close()


create_table()


def Exit():
    payroll.destroy()


def Reset():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    Email.set("")
    JobStatus.set("")
    City.set("")
    BasicSalary.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    Pension.set("")
    StudentLoan.set("")
    NIPayment.set("")
    Deductions.set("")
    PostCode.set("")
    Gender.set("")
    Grade.set("")
    Department.set("")
    PayDate.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionPay.set("")
    OtherPaymentDue.set("")


def PayRef():
    PayDate.set(time.strftime("%d/%m/%y"))

    Refpay = random.randint(20000, 709467)
    Refpaid = ("PR" + str(Refpay))
    Reference.set(Refpaid)

    NIpay = random.randint(4200, 9467)
    NIpaid = ("NI" + str(NIpay))
    NINumber.set(NIpaid)


def PayPeriod():
    i = datetime.datetime.now()
    TaxPeriod.set(i.month)

    NCode = random.randint(1200, 4467)
    Cod = ("NICode" + str(NCode))
    NICode.set(Cod)


def MonthlySalary():
    BS = float(BasicSalary.get())
    CW = float(City.get())
    OT = float(OverTime.get())

    MTax = ((BS + CW + OT) * 0.5)
    Tax.set(f"P {MTax:.2f}")

    M_Pension = ((BS + CW + OT) * 0.026)
    Pension.set(f"P {M_Pension:.2f}")

    M_StudentLoan = ((BS + CW + OT) * 0.012)
    StudentLoan.set(f"P {M_StudentLoan:.2f}")

    M_NIPayment = ((BS + CW + OT) * 0.011)
    NIPayment.set(f"P {M_NIPayment:.2f}")

    Deduct = (MTax + M_Pension + M_StudentLoan + M_NIPayment)
    Deductions.set(f"P {Deduct:.2f}")

    Gross_Pay = f"P {BS + CW + OT:.2f}"
    GrossPay.set(Gross_Pay)

    NetPayAfter = (BS + CW + OT) - Deduct
    NetPay.set(f"P {NetPayAfter:.2f}")

    TaxablePay.set(f"P {MTax:.2f}")
    PensionPay.set(f"P {M_Pension:.2f}")
    OtherPaymentDue.set("0")

    # Save data to database
    save_to_db()


def save_to_db():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO payroll_data (employee_name, address, reference, employer_name, email, job_status,
            city_weighting, basic_salary, overtime, gross_pay, net_pay, tax, pension, student_loan,
            ni_payment, deductions, postcode, gender, grade, department, pay_date, tax_period,
            ni_number, ni_code, taxable_pay, pension_pay, other_payment_due)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        EmployeeName.get(),
        Address.get(),
        Reference.get(),
        EmployerName.get(),
        Email.get(),
        JobStatus.get(),
        City.get(),
        BasicSalary.get(),
        OverTime.get(),
        GrossPay.get(),
        NetPay.get(),
        Tax.get(),
        Pension.get(),
        StudentLoan.get(),
        NIPayment.get(),
        Deductions.get(),
        PostCode.get(),
        Gender.get(),
        Grade.get(),
        Department.get(),
        PayDate.get(),
        TaxPeriod.get(),
        NINumber.get(),
        NICode.get(),
        TaxablePay.get(),
        PensionPay.get(),
        OtherPaymentDue.get()
    ))
    conn.commit()
    conn.close()


EmployeeName = StringVar()
Address = StringVar()
Reference = StringVar()
EmployerName = StringVar()
Email = StringVar()
JobStatus = StringVar()
City = StringVar()
BasicSalary = StringVar()
OverTime = StringVar()
GrossPay = StringVar()
NetPay = StringVar()
Tax = StringVar()
Pension = StringVar()
StudentLoan = StringVar()
NIPayment = StringVar()
Deductions = StringVar()
PostCode = StringVar()
Gender = StringVar()
Grade = StringVar()
Department = StringVar()
PayDate = StringVar()
TaxPeriod = StringVar()
NINumber = StringVar()
NICode = StringVar()
TaxablePay = StringVar()
PensionPay = StringVar()
OtherPaymentDue = StringVar()

# GUI components here...

payroll.mainloop()
