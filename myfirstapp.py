from tornado.web import HTTPError
from gramex.http import BAD_REQUEST
import pandas as pd
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import xlrd
import datetime
import matplotlib.pyplot as plt
import re
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

def topCrimeYTD(data, handler): #YearToDate function for each precinct
  thing2=pd.DataFrame()
  thing2=data
  thing2 = thing2[['Crime Type', 'Year to Date 2020', 'precinct']]
  cols = list(thing2['Crime Type'].unique())
  top5precinctYear = pd.pivot_table(thing2, values='Year to Date 2020', index=['precinct'],columns=['Crime Type'])
  unwanted_Cols =['TOTAL']
  top5precinctYear.drop(columns=unwanted_Cols, inplace=True)
  top5precinctYear['top5CrimeByPrec_YTD'] = top5precinctYear.max(axis=1)
  top5precinctYear['Max'] = top5precinctYear.idxmax(axis=1)
  top5precinctYear[['top5CrimeByPrec_YTD', 'Max']].sort_values(by=['top5CrimeByPrec_YTD'], ascending=False).head(5)
  return data


def topCrimeWTD(data, handler):#WeekToDate function for each precinct
  thing1=data
  thing1 = thing1[['Crime Type', 'Week to Date 2020', 'precinct']]
  cols = list(thing1['Crime Type'].unique())
  top5precinct = pd.pivot_table(thing1, values='Week to Date 2020', index=['precinct'], columns=['Crime Type'])
  unwanted_Cols =['TOTAL']
  top5precinct.drop(columns=unwanted_Cols, inplace=True)
  top5precinct['top5CrimeByPrecWTD'] = top5precinct.max(axis=1)
  top5precinct['Max'] = top5precinct.idxmax(axis=1)
  top5precinct=top5precinct[['top5CrimeByPrecWTD', 'Max']].sort_values(by=['top5CrimeByPrecWTD'], ascending=False)
  return top5precinct


def topCrimeMTD(data, handler):#MonthToDate function for each precinct
  thing1=data
  thing1 = thing1[['Crime Type', '28 day 2020', 'precinct']]
  cols = list(thing1['Crime Type'].unique())
  top5precinct = pd.pivot_table(thing1, values='28 day 2020', index=['precinct'], columns=['Crime Type'])
  unwanted_Cols =['TOTAL']
  top5precinct.drop(columns=unwanted_Cols, inplace=True)
  top5precinct['top5CrimeByPrecMTD'] = top5precinct.max(axis=1)
  top5precinct['Max'] = top5precinct.idxmax(axis=1)
  top5precinct=top5precinct[['top5CrimeByPrecMTD', 'Max']].sort_values(by=['top5CrimeByPrecMTD'], ascending=False)
  return top5precinct


# TopCrimeYTD-data:
  #   pattern: /$YAMLURL/TopCrimeYTD
  #   handler: FormHandler
  #   kwargs:
  #     url: sqlite:///$YAMLPATH/save_pandas.db
  #     table: TopCrimes