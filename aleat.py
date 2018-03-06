#!/usr/bin/python3

import webapp
import random

class aleatapp(webapp.webApp):

    def process(self, parsedRequest):
        number = random.randint(1,1000000000)
        code = "200 OK"
        htmlAnswer = '<p><a href="http://localhost:1234/' + str(number) + '">Dame otra</a></p>'
        return code, htmlAnswer

if __name__ == '__main__':
    URLsAleat = aleatapp('localhost', 1234)
