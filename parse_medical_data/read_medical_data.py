import pandas as pd

from medical_data import MedicalData 

class ReadMedicalData:

    URL = "https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}"

    def __init__(self) -> None:
        """
        """
        self.__id_sheet = "1cO0sPRhIvt71J-iB313BeRfNXzXM0FjiQ4bDYmwddBQ"
        self.__sheet_name = "Sheet1"

    @property
    def google_sheet_url(self) -> str:
        """
        """
        return self.URL.format(self.__id_sheet, self.__sheet_name)

    def get_google_sheet_data(self):
        """
        """
        url = self.google_sheet_url
        google_sheet_data = pd.read_csv(url)
        return google_sheet_data
  
    def get_medicals_data(self):
        medicals_data = list()
        google_sheet_data = self.get_google_sheet_data()

        for _, row in google_sheet_data.iterrows():
            hierarchy = row["hierarchy"]
            option = row["option"]
            answer = row["answer"]
            link = row["link"]

            medical_data = MedicalData(hierarchy, option, answer, link)
            medicals_data.append(medical_data)

        return medicals_data

def main():
    medicals_data = ReadMedicalData().get_medicals_data()
    a = 1
    b = a

if __name__ == "__main__":
    main()