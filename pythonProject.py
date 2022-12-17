import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

phone_details = []
thePrice = []
shipping_Type = []
Evaluation = []
Url = "https://www.amazon.eg/gp/aw/s/ref=mh_s9_acss_cg_ATF1208_3b1_w?i=electronics&bbn=21832883031&rh=n%3A21832883031%2Cp_89%3ASAMSUNG&pf_rd_m=A1ZVRGNO5AYLOV&pf_rd_s=mobile-hybrid-14&pf_rd_r=7NXTE9T8V19F46DB7MJK&pf_rd_t=30901&pf_rd_p=12935e2e-0e4e-43ab-8dab-9628af9ab07b&pf_rd_i=21832883031"
result = requests.get(Url)
src = result.content
Soup = BeautifulSoup(src, "html.parser")
phone_details = Soup.find_all("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
# print(phone_details)
thePrice = Soup.find_all("span", {"class": "a-price-whole"})
# print(thePrice)
shipping_Type = Soup.find_all("span", {"class": "a-color-base"})
# print(shipping_Type)
Evaluation = Soup.find_all("span", {"class": "a-icon-alt"})
# print(Evaluation)
for web in range(len(phone_details)):
    thePrice.append(thePrice[web].text)
    Evaluation.append(Evaluation[web].text)
    print(thePrice, "\n", Evaluation)
    phone_details.append(print(phone_details)[web].text)
    ##########################################################################################################################
    # انا عامله المشروع فردى حاولت اعمله فى sheet excel بس كان فيه شويه مشاكل حاولت احلها معرفتش

    # file_list = [phone_details, thePrice, Evaluation]
    # page = zip_longest(* file_list)
    # with open("python project.csv", "w", newline='') as myfile:
    #     wr = csv.writer(myfile)
    #     wr.writerow([phone_details, thePrice, Evaluation])
    #     wr.writerows(page)







    file_list = [phone_details, thePrice, Evaluation]
    page = zip_longest(*file_list)
    Fields = ["phone_details", " thePrice"]
    filepath = "C:/Users/Microsoft/Documents/python project.csv"
    with open(filepath, "w") as csvfile:
        csvwriter = csv.writer(csvwriter)
        csvwriter.writerow(Fields)
    csvwriter.writerows(phone_details, thePrice)
    print(phone_details, "\n", thePrice, "\n", Evaluation)
