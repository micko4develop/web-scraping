
##########################################
## 01. Sripe all images sec on web page ##
##########################################
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://umetnickeslike.org/?gad_source=1&gclid=Cj0KCQjw8J6wBhDXARIsAPo7QA8l_Jum8rDxG5Iuk0A7bu_HT-xdHaoWMTJIVlN35HGEfiZhSQSUOHsaAmdnEALw_wcB'
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Extracting and printing the title of the webpage
# title = soup.title
# print(title.text)
#
# # Extracting and printing all the links on the webpage
# for link in soup.find_all('img'):
#     print(link.get('src'))

######################################################################
## 02. Scriping questions, views and vote_count from Stack OverFlow ##
######################################################################
# import requests
# from bs4 import BeautifulSoup
# import json
#
# response = requests.get("https://stackoverflow.com/questions");
#
# soup = BeautifulSoup(response.text, "html.parser")
#
# questions_data = {
#     "questions": []
# }
#
# questions = soup.select(".s-post-summary")
#
# #print(questions)
#
# for que in questions:
#     href_for_question = "https://stackoverflow.com/" + que.select_one(".s-link").get('href')
#     post_summary = que.select_one(".s-post-summary--content-excerpt").getText()
#     vote_count = que.select_one('.s-post-summary--stats-item-number').getText()
#     questions_data['questions'].append({
#         "href_for_question": href_for_question,
#         "post_summary": post_summary,
#         "vote_count": vote_count
#     })
#
# json_data = json.dumps(questions_data)
#
# print(json_data)



####################################################################################
## 03. Scriping questions, views and vote_count from Stack OverFlow and add Flask ##
####################################################################################
import requests

from bs4 import BeautifulSoup
import json

from flask import Flask

app = Flask(__name__)

@app.route("/stack_overflow_questions")
def index():
    response = requests.get("https://stackoverflow.com/questions")

    soup = BeautifulSoup(response.text, "html.parser")

    questions_data = {
        "questions": []
    }

    questions = soup.select(".s-post-summary")

    for que in questions:
        href_for_question = "https://stackoverflow.com/" + que.select_one(".s-link").get('href')
        post_summary = que.select_one(".s-post-summary--content-excerpt").getText()
        vote_count = que.select_one('.s-post-summary--stats-item-number').getText()
        questions_data['questions'].append({
            "href_for_question": href_for_question,
            "post_summary": post_summary,
            "vote_count": vote_count
        })

    json_data = json.dumps(questions_data)

    return json_data

    #return jsonify(questions_data)

if __name__ == "__main__":
    app.run()