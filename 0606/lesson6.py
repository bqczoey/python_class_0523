import requests
from requests import Response
from pandas import DataFrame
import pandas as pd
import report
from pathlib import Path

def main():
    # 台北市 YouBike 2.0 的 Web API 網址
    url:str = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

        # 使用 requests 套件裡面的 get 函式，執行後會傳出 Response 的實體
    response:Response = requests.get(url) 

    if response.status_code == 200: # 使用 Response 裡的 Property 叫 status_code，如果取得的數字是 200 代表下載成功，如果不是則代表下載失敗
            data:list[dict] = response.json() # 使用 Response 實體的 json() 方法，會傳出 list 的資料結構

            # list[dict] -> DataFrame
            df:DataFrame = pd.DataFrame(data=data)
            
            output_file = Path(__file__).with_name("youbike_report.pdf")

            report.export_to_pdf(df, output_file)
    else:
            print("下載失敗")

if __name__ == '__main__':
    main()


