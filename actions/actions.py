# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from selenium import webdriver
import pandas as pd
import time

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ent = tracker.latest_message['entities'][0]['value']
        dispatcher.utter_message(text=ent)
        # This is done to structure the string 
        # into search url.(This can be ignored)
        search_string = ent.replace(' ', '+')
  
        # Assigning the browser variable with chromedriver of Chrome.
        # Any other browser and its respective webdriver 
        # like geckodriver for Mozilla Firefox can be used
        browser = webdriver.Chrome(r'C:/Users/PRATIK/rasa/actions/chromedriver.exe')
  
        for i in range(1):
            matched_elements = browser.get("https://www.google.com/search?q=" +
                                     search_string + "&start=" + str(i))
        return []
    
class ActionPostLinkedin(Action):

    def name(self) -> Text:
        return "action_post_linkedin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ent = "Done"
        # specifies the path to the chromedriver.exe
        driver = webdriver.Chrome(r'C:/Users/PRATIK/rasa/actions/chromedriver.exe')

        # reading csv file  
        df = pd.read_csv(r'C:/Users/PRATIK/rasa/actions/credentials.csv', encoding='utf-8')
        # reading username
        myUsername = df.Username[0]

        # reading password
        myPassword = df.Password[0]

        # reading post
        myPost = "Please find my article on a simple technique for the generalization of ML models.\n https://becominghuman.ai/generalization-technique-for-ml-models-ed6ba666d171"
        # driver.get method() will navigate to a page given by the URL address
        driver.get("https://www.linkedin.com/login?")
        # locate email form by_name
        username = driver.find_element_by_name('session_key')
        username.send_keys(myUsername)
        #locate password form by_xpath
        password = driver.find_element_by_xpath('//*[@id="password"]')


        # send_keys() to simulate key strokes
        password.send_keys(myPassword)
        # locate submit button by_class_name
        log_in_button = driver.find_element_by_class_name('btn__primary--large')

        # locate submit button by_xpath
        #log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
        # .click() to mimic button click
        log_in_button.click()
        # locate post field by_xpath
        time.sleep(5)
        postButton = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/button')
        # .click() to mimic button click 
        postButton.click()
        time.sleep(4)
        # locate text editor by_class_name
        postContent = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]')

        # send_keys() to simulate key strokes
        postContent.send_keys(myPost)
        #locate post button by_id
        time.sleep(10)
        post = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button')

        # .click() to mimic button click 
        post.click()
            
        dispatcher.utter_message(text=ent)
        return []
