import os
import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta

deta_key = os.getenv("DETA_KEY")


deta=Deta(deta_key)
db=deta.Base("monthly_reports")


def insert_period(period, incomes, expenses, comment):
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    res = db.fetch()
    return res.items


def get_period(period):
    return db.get(period)