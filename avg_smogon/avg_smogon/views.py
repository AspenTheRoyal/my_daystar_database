from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests, json
from collections import Counter
import time
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def avg_smogon_view(request):
    return render(request, 'avg_smogon.html')
def my_smogon_script(request):
    if request.method == 'POST':
        da_pokemon_needed = request.POST.get('pokemon_input', '')
        result = smogon_actual_script(da_pokemon_needed)
        context = {"result": result}
        return render(request, 'avg_smogon.html', context)
    else:
        # This is the GET request that shows the form with {% csrf_token %}
        return render(request, 'avg_smogon.html')
def smogon_actual_script(inputText):
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-images')
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    baseURL = "https://pokeapi.co/api/v2/pokemon-species/"
    inputThing = inputText.lower()
    specificURL = baseURL+inputThing
    pokemonData = requests.get(specificURL).json()
    generationData = pokemonData["generation"]
    generationName = generationData["name"]
    generationToBaseURL = {
        "generation-ix": ["https://www.smogon.com/dex/sv/pokemon/"],
        "generation-viii": ["https://www.smogon.com/dex/ss/pokemon/", "https://www.smogon.com/dex/sv/pokemon/"],
        "generation-vii": ["https://www.smogon.com/dex/ss/pokemon/", "https://www.smogon.com/dex/sv/pokemon/", "https://www.smogon.com/dex/sm/pokemon/"],
        "generation-vi": ["https://www.smogon.com/dex/ss/pokemon/", "https://www.smogon.com/dex/sv/pokemon/", "https://www.smogon.com/dex/sm/pokemon/", "https://www.smogon.com/dex/xy/pokemon/"],
        "generation-v": ["https://www.smogon.com/dex/ss/pokemon/", "https://www.smogon.com/dex/sv/pokemon/", "https://www.smogon.com/dex/sm/pokemon/", "https://www.smogon.com/dex/xy/pokemon/", 
                         "https://www.smogon.com/dex/bw/pokemon/"],
        "generation-iv": ["https://www.smogon.com/dex/ss/pokemon/", "https://www.smogon.com/dex/sv/pokemon/", "https://www.smogon.com/dex/sm/pokemon/", "https://www.smogon.com/dex/xy/pokemon/", 
                         "https://www.smogon.com/dex/bw/pokemon/", "https://www.smogon.com/dex/dp/pokemon/"],
        "generation-iii": ["https://www.smogon.com/dex/ss/pokemon/", "https://www.smogon.com/dex/sv/pokemon/", "https://www.smogon.com/dex/sm/pokemon/", "https://www.smogon.com/dex/xy/pokemon/", 
                         "https://www.smogon.com/dex/bw/pokemon/", "https://www.smogon.com/dex/dp/pokemon/",],
        "generation-ii": ["https://www.smogon.com/dex/ss/pokemon/", "https://www.smogon.com/dex/sv/pokemon/", "https://www.smogon.com/dex/sm/pokemon/", "https://www.smogon.com/dex/xy/pokemon/", 
                         "https://www.smogon.com/dex/bw/pokemon/", "https://www.smogon.com/dex/dp/pokemon/",],
        "generation-i": ["https://www.smogon.com/dex/ss/pokemon/", "https://www.smogon.com/dex/sv/pokemon/", "https://www.smogon.com/dex/sm/pokemon/", "https://www.smogon.com/dex/xy/pokemon/", 
                         "https://www.smogon.com/dex/bw/pokemon/", "https://www.smogon.com/dex/dp/pokemon/",],
    }
    driver = webdriver.Chrome(options=options)
    tinyList = []
    for url in generationToBaseURL[generationName]:
        newUrl = url+inputThing
        driver.get(newUrl)
        driver.implicitly_wait(0.25)
        intendedClass = driver.find_element(By.CLASS_NAME, "PokemonAltInfo-data")
        theList = intendedClass.text
        splittedList = theList.split("\n")
        tinyList.append(splittedList[-1])
    driver.quit()
    if "NFE" in tinyList:
        status = ["NFE"]
    elif "LC" in tinyList:
        status = ["LC"]
    else:
        status = [item for item in tinyList if item != "National Dex"]
        for format, number in zip(status,range(len(status))):
            if format == "UUBL":
                status[number] = "OU"
            if format == "NUBL":
                status[number] = "RU"
            if format == "RUBL":
                status[number] = "UU"
            if format == "PUBL":
                status[number] == "NU"
            if format == "ZUBL":
                status[number] == "PU"
    formats = Counter()
    for i in status:
        formats[i] += 1
    return formats

# rb, gs, rs, dp, bw, xy, sm, ss, sv
# Create your views here.
