from unittest import result
import pytest
from scripts import io_service
import csv

results = [{"address":"1235", "ens": "d.eth"},
          {"address":"80830", "ens": "a.eth"},]

# def test_write_result_to_csv():
#     io_service.write_results(results, "result.csv")

def load_data(file_path):
    with open(file_path, mode='r') as csv_file:
                csv_content = csv.DictReader(csv_file) 
                return [row for row in csv_content]
                # return csv_content


def test_load_valid_csv():
    data = io_service.load_data("./test_file/address.csv")
    print(data)
    assert len(data) == 6