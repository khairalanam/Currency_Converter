import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Fetching data from API

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
text = response.json()
currencies = text["rates"]

# Functions used


def convert(from_currency, to_currency, amount):
    usd_amount = amount / currencies[from_currency]
    pre_final_amount = usd_amount * currencies[to_currency]
    final_amount = round(pre_final_amount, 4)
    return final_amount
