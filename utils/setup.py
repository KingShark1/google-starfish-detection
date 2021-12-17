import os
import argparse
from posixpath import dirname
import requests
from pathlib import Path



def command_line_utility():
  # Check whether data folder exists
  
  dirname = "data"
  data_path = os.path.join(Path(__file__).parent.parent, dirname)
  print(data_path + "/train.csv")
  print(data_path + "/test.csv")
  

  # Initialize Parser
  parser = argparse.ArgumentParser()
  

  # Read arguments from command line
  args = parser.parse_args()

