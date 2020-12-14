import requests
import matplotlib.pyplot as plt

# Retrieve UK Power generation mix and display in a bar chart.

# Datetime in ISO8601 format YYYY-MM-DDThh:mmZ e.g. 2017-08-25T12:35Z

date_from = "2020-11-22T12:00Z"
date_to = "2020-11-22T12:30Z"
url = "https://api.carbonintensity.org.uk/generation/"+date_from+"/"+date_to
power_request = requests.get(url)

print("Status code: ", power_request.status_code)

if power_request.status_code == requests.codes.ok:
    print(power_request.json())
    power = power_request.json()["data"][0]
    print(power)

    labels = []
    sizes = []

    total = 0
    for energy in power["generationmix"]:
        if energy["perc"] > 0:
            print(energy["fuel"], energy["perc"])
            total += energy["perc"]

            labels.append(energy["fuel"])
            sizes.append(energy["perc"])

    print("Total: ", total)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=45)
    ax1.axis("equal") # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
