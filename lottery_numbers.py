import requests
import json
from HelperClasses.NumberStat import *

def download_data_json():
     url = "https://bet.szerencsejatek.hu/cmsfiles/otos.json"
     resp = requests.get(url)
     return resp.content
     
def get_top5(number_stats: dict):
     all_number_stats = list()

     for i in range(1, 91):
          number_stat = number_stats[str(i)]
          draw_count = number_stat["drawCount"]
          ratio = number_stat["ratio"]
          statInstance = NumberStat(i, draw_count, ratio)
          all_number_stats.append(statInstance)
          
     all_number_stats.sort(key=lambda stat: stat.draw_count, reverse=True)
     for i in range(5):
          print(all_number_stats[i].to_str())
     
def main():
     json_of_lottery_numbers = download_data_json()
     data_dict = json.loads(json_of_lottery_numbers)
     number_stats = data_dict["numberStatistics"]
     drawingStats = data_dict["drawings"]
     get_top5(number_stats)
          
if __name__ == "__main__":
    main()