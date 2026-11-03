from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.


class Account(View):
    def get(self, request):
        data = {
            "Account_Number": 1234567890,
            "Account_Holder": "Adhish Santhosh",
            "Account_Type": "Savings",
            "Balance": 50000,
            "IFSC_Code": "SBIN0001234",
            "Branch": "Alappuzha"
        }

        return JsonResponse(data)


class Customer(View):
    def get(self, request):
        data = {
            "Customer_ID": 101,
            "Name": "Adhish Santhosh",
            "Age": 23,
            "Mobile": "9876543210",
            "Email": "adhish@gmail.com",
            "Address": "Alappuzha"
        }

        return JsonResponse(data)


class Loan(View):
    def get(self, request):
        data = {
            "Loan_ID": 201,
            "Customer_Name": "Adhish Santhosh",
            "Loan_Type": "Home Loan",
            "Loan_Amount": 1000000,
            "Interest_Rate": 8.5,
            "Duration": "10 Years"
        }

        return JsonResponse(data)


class Branch(View):
    def get(self, request):
        data = {
            "Branch_ID": 301,
            "Branch_Name": "State Bank of India",
            "Location": "Alappuzha",
            "IFSC_Code": "SBIN0001234",
            "Manager": "Arun Kumar",
            "Contact": "9876543211"
        }

        return JsonResponse(data)


class Transaction(View):
    def get(self, request):
        data = {
            "Transaction_ID": 401,
            "Account_Number": 1234567890,
            "Transaction_Type": "Credit",
            "Amount": 5000,
            "Date": "2026-11-03",
            "Status": "Successful"
        }

        return JsonResponse(data)
