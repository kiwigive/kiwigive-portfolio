# CS50 Final Project: A Personal Portfolio Website Project
#### Video Demo:  https://www.youtube.com/watch?v=f0poFig4v5w
#### Introduction
Kiwigive is my personal portfolio website. At first, I think about making a routine tracking web application. For my certain level of knowledge, I would like to start from the simplest one first. I decided to do the online portfolio because it will be useful. I can use this website to collect all of my information and my future projects.

#### Designing
I started sketching on my Ipad, and try to color them. I got pink, mint, blue, brown, and yellow to be the color theme. They give liveliness and playful feelings, that can represent my personality. I do a lot of research for designing. I think this project is more about front-end than back-end. The first thing I got is a favicon, that turns to become my mascot from now on.

#### Details
The webpage is modified from the finance-CS50x starter template, which uses a bootstrap, flask, CSS, and Javascript. It would not be wrong if I said it is all vanilla-Javascript. It took more time than expected to finish this project. When I want something, I google it, change it, find a bug, google again, repeat, and so on. I want to make sure that this website is responsive on a different device. Moreover, I put some details on some pages, and on every page, it will appear the same header, footer, and go-to-top button.

This site has 4 main routes as follows:
- homepage
When you arrive at this website, you will be redirected to the homepage. At the top of the page is my portrait image. It will appear differently according to the size of your device. Inside of this image will display a greeting message, that will change through the present time. For example, if it is morning, they will greet you, good morning. I put some details on this page. The seal can blink! Not only clicking but also touching the screen on your mobile device, the seal will blink.

- about
When you hover about-tab, it will appear a subtopic. It is a quick link to those sections. On the top of the page have a slide show of my pictures. Next section, once you click the "resume" button, my resume will pop up. You may download or close by the button on the right top corner. For more user-friendly, you may click anywhere excepts the resume image to close. My learning journeys are shown in a timeline style and my skills are shown in a gauge style. In experiences section, you may click each experience to reveal the information of those experiences. In the last section, the other side, they have my image. It allows clicking to a pop-up images slide show of that event.

- project
The design of this page is a web browser window. You may see the seal icon bouncing. In the body part, it will appear all of my project cards, which have images, titles, and details. You may click on those project cards that you want to discover for more information.

- contact
The core of this page is a contact box. You may use this box to send me a message. An empty field is not accepted, all fields are required and the email field has basic email checking. If the message was sent successfully, it will be delivered via LINE application and I will be notified immediately.


#### How to run the projects
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=application
flask run
```