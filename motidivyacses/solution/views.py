from django.shortcuts import render
from .models import *
import os
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    allSolutions = PythonSolution.objects.all()
    solutions = []
    for solution in allSolutions:
        solutions.append({"id": solution.id, "title": solution.title})
        context = {
            "solutions": solutions
        }
    return render(request, "solution/index.html", context)

def solution(request, id):
    solutions_folder_path = "..\solutions"
    os.chdir(solutions_folder_path)
    for file in os.listdir():
        if file.endswith(".py"):
            file_path = f"{solutions_folder_path}\{file}"
            extract_id_and_code_from_file(file_path)
        
    solution = PythonSolution.objects.get(id = id)
    context = {
        "solution": solution
    }
    return render(request, "solution/solution.html", context)

def extract_id_and_code_from_file(file_path):
    with open(file_path, 'r') as f:

        # print(f.read())
        raw_data = f.read()
        solution_id = int(raw_data[1:5])
        code = raw_data[6:]
        url = "https://cses.fi/problemset/task/" + str(solution_id)
        get_url = requests.get(url)
        get_text = get_url.text
        soup = BeautifulSoup(get_text, "html.parser")
        title = soup.select("h1")[0].text.strip()
        
        print(solution_id, title)
        