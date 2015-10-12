# coding=utf-8
import requests
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.defaulttags import register
# Create your views here.
from books.forms import ContactForm
from books.models import Book
import json


text = '{"list":[{"id":0,"passengerOrderHashMap":[[{"id":2,"role":2,"phoneNumber":"0666076706","fbProfile":{"id":"id_link2","type":2,"link":"https://plus.google.com/+AlexanderZhovnuvaty","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя2","surName":"Фамилия2","gender":2,"age":34,"email":"email2","birthday":"1983-03-26"}},{"id":1300,"totalSeats":2,"depLocation":{"mLongitudeE6":24007593,"mLatitudeE6":49823836,"mAltitude":0},"destLocation":{"mLongitudeE6":24053202,"mLatitudeE6":49864560,"mAltitude":0},"depAddress":"From 1","destAddress":"To 1","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":4,"role":2,"phoneNumber":"0666076707","vkProfile":{"id":"id_link5","type":3,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя5","surName":"Фамилия5","gender":2,"age":34,"email":"email5","birthday":"1983-03-27"}},{"id":1301,"totalSeats":2,"depLocation":{"mLongitudeE6":24017829,"mLatitudeE6":49801100,"mAltitude":0},"destLocation":{"mLongitudeE6":24029501,"mLatitudeE6":49844071,"mAltitude":0},"depAddress":"From 2","destAddress":"To 2","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":1,"role":2,"phoneNumber":"0666076705","gPlusProfile":{"id":"id_link1","type":1,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя1","surName":"Фамилия1","gender":1,"age":33,"email":"email1","birthday":"1982-03-25"}},{"id":1299,"totalSeats":2,"depLocation":{"mLongitudeE6":23990761,"mLatitudeE6":49811403,"mAltitude":0},"destLocation":{"mLongitudeE6":24010512,"mLatitudeE6":49826688,"mAltitude":0},"depAddress":"From 0","destAddress":"To 0","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":5,"role":2,"phoneNumber":"0666076708","vkProfile":{"id":"id_link8","type":3,"link":"https://www.facebook.com/app_scoped_user_id/1637344933216693/","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя8","surName":"Фамилия8","gender":2,"age":34,"email":"email8","birthday":"1983-03-28"}},{"id":1302,"totalSeats":2,"depLocation":{"mLongitudeE6":24017314,"mLatitudeE6":49812844,"mAltitude":0},"destLocation":{"mLongitudeE6":24000663,"mLatitudeE6":49816720,"mAltitude":0},"depAddress":"From 3","destAddress":"To 3","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}]],"stops":{"0":{"passengerId":4,"orderId":1301,"type":1},"1":{"passengerId":5,"orderId":1302,"type":1},"2":{"passengerId":1,"orderId":1299,"type":1},"3":{"passengerId":5,"orderId":1302,"type":2},"4":{"passengerId":2,"orderId":1300,"type":1},"5":{"passengerId":1,"orderId":1299,"type":2},"6":{"passengerId":4,"orderId":1301,"type":2},"7":{"passengerId":2,"orderId":1300,"type":2}},"stateId":1,"price":120},{"id":0,"passengerOrderHashMap":[[{"id":2,"role":2,"phoneNumber":"0666076706","fbProfile":{"id":"id_link2","type":2,"link":"https://plus.google.com/+AlexanderZhovnuvaty","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя2","surName":"Фамилия2","gender":2,"age":34,"email":"email2","birthday":"1983-03-26"}},{"id":1300,"totalSeats":2,"depLocation":{"mLongitudeE6":24007593,"mLatitudeE6":49823836,"mAltitude":0},"destLocation":{"mLongitudeE6":24053202,"mLatitudeE6":49864560,"mAltitude":0},"depAddress":"From 1","destAddress":"To 1","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}],[{"id":1,"role":2,"phoneNumber":"0666076705","gPlusProfile":{"id":"id_link1","type":1,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя1","surName":"Фамилия1","gender":1,"age":33,"email":"email1","birthday":"1982-03-25"}},{"id":1299,"totalSeats":2,"depLocation":{"mLongitudeE6":23990761,"mLatitudeE6":49811403,"mAltitude":0},"destLocation":{"mLongitudeE6":24010512,"mLatitudeE6":49826688,"mAltitude":0},"depAddress":"From 0","destAddress":"To 0","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}],[{"id":5,"role":2,"phoneNumber":"0666076708","vkProfile":{"id":"id_link8","type":3,"link":"https://www.facebook.com/app_scoped_user_id/1637344933216693/","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя8","surName":"Фамилия8","gender":2,"age":34,"email":"email8","birthday":"1983-03-28"}},{"id":1302,"totalSeats":2,"depLocation":{"mLongitudeE6":24017314,"mLatitudeE6":49812844,"mAltitude":0},"destLocation":{"mLongitudeE6":24000663,"mLatitudeE6":49816720,"mAltitude":0},"depAddress":"From 3","destAddress":"To 3","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}]],"stops":{"0":{"passengerId":5,"orderId":1302,"type":1},"1":{"passengerId":1,"orderId":1299,"type":1},"2":{"passengerId":5,"orderId":1302,"type":2},"3":{"passengerId":2,"orderId":1300,"type":1},"4":{"passengerId":1,"orderId":1299,"type":2},"5":{"passengerId":2,"orderId":1300,"type":2}},"stateId":1,"price":120},{"id":0,"passengerOrderHashMap":[[{"id":2,"role":2,"phoneNumber":"0666076706","fbProfile":{"id":"id_link2","type":2,"link":"https://plus.google.com/+AlexanderZhovnuvaty","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя2","surName":"Фамилия2","gender":2,"age":34,"email":"email2","birthday":"1983-03-26"}},{"id":1300,"totalSeats":2,"depLocation":{"mLongitudeE6":24007593,"mLatitudeE6":49823836,"mAltitude":0},"destLocation":{"mLongitudeE6":24053202,"mLatitudeE6":49864560,"mAltitude":0},"depAddress":"From 1","destAddress":"To 1","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":4,"role":2,"phoneNumber":"0666076707","vkProfile":{"id":"id_link5","type":3,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя5","surName":"Фамилия5","gender":2,"age":34,"email":"email5","birthday":"1983-03-27"}},{"id":1301,"totalSeats":2,"depLocation":{"mLongitudeE6":24017829,"mLatitudeE6":49801100,"mAltitude":0},"destLocation":{"mLongitudeE6":24029501,"mLatitudeE6":49844071,"mAltitude":0},"depAddress":"From 2","destAddress":"To 2","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":1,"role":2,"phoneNumber":"0666076705","gPlusProfile":{"id":"id_link1","type":1,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя1","surName":"Фамилия1","gender":1,"age":33,"email":"email1","birthday":"1982-03-25"}},{"id":1299,"totalSeats":2,"depLocation":{"mLongitudeE6":23990761,"mLatitudeE6":49811403,"mAltitude":0},"destLocation":{"mLongitudeE6":24010512,"mLatitudeE6":49826688,"mAltitude":0},"depAddress":"From 0","destAddress":"To 0","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":5,"role":2,"phoneNumber":"0666076708","vkProfile":{"id":"id_link8","type":3,"link":"https://www.facebook.com/app_scoped_user_id/1637344933216693/","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя8","surName":"Фамилия8","gender":2,"age":34,"email":"email8","birthday":"1983-03-28"}},{"id":1302,"totalSeats":2,"depLocation":{"mLongitudeE6":24017314,"mLatitudeE6":49812844,"mAltitude":0},"destLocation":{"mLongitudeE6":24000663,"mLatitudeE6":49816720,"mAltitude":0},"depAddress":"From 3","destAddress":"To 3","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}]],"stops":{"0":{"passengerId":4,"orderId":1301,"type":1},"1":{"passengerId":5,"orderId":1302,"type":1},"2":{"passengerId":1,"orderId":1299,"type":1},"3":{"passengerId":5,"orderId":1302,"type":2},"4":{"passengerId":2,"orderId":1300,"type":1},"5":{"passengerId":1,"orderId":1299,"type":2},"6":{"passengerId":4,"orderId":1301,"type":2},"7":{"passengerId":2,"orderId":1300,"type":2}},"stateId":1,"price":120},{"id":0,"passengerOrderHashMap":[[{"id":2,"role":2,"phoneNumber":"0666076706","fbProfile":{"id":"id_link2","type":2,"link":"https://plus.google.com/+AlexanderZhovnuvaty","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя2","surName":"Фамилия2","gender":2,"age":34,"email":"email2","birthday":"1983-03-26"}},{"id":1300,"totalSeats":2,"depLocation":{"mLongitudeE6":24007593,"mLatitudeE6":49823836,"mAltitude":0},"destLocation":{"mLongitudeE6":24053202,"mLatitudeE6":49864560,"mAltitude":0},"depAddress":"From 1","destAddress":"To 1","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}],[{"id":1,"role":2,"phoneNumber":"0666076705","gPlusProfile":{"id":"id_link1","type":1,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя1","surName":"Фамилия1","gender":1,"age":33,"email":"email1","birthday":"1982-03-25"}},{"id":1299,"totalSeats":2,"depLocation":{"mLongitudeE6":23990761,"mLatitudeE6":49811403,"mAltitude":0},"destLocation":{"mLongitudeE6":24010512,"mLatitudeE6":49826688,"mAltitude":0},"depAddress":"From 0","destAddress":"To 0","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}],[{"id":5,"role":2,"phoneNumber":"0666076708","vkProfile":{"id":"id_link8","type":3,"link":"https://www.facebook.com/app_scoped_user_id/1637344933216693/","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя8","surName":"Фамилия8","gender":2,"age":34,"email":"email8","birthday":"1983-03-28"}},{"id":1302,"totalSeats":2,"depLocation":{"mLongitudeE6":24017314,"mLatitudeE6":49812844,"mAltitude":0},"destLocation":{"mLongitudeE6":24000663,"mLatitudeE6":49816720,"mAltitude":0},"depAddress":"From 3","destAddress":"To 3","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}]],"stops":{"0":{"passengerId":5,"orderId":1302,"type":1},"1":{"passengerId":1,"orderId":1299,"type":1},"2":{"passengerId":5,"orderId":1302,"type":2},"3":{"passengerId":2,"orderId":1300,"type":1},"4":{"passengerId":1,"orderId":1299,"type":2},"5":{"passengerId":2,"orderId":1300,"type":2}},"stateId":1,"price":120},{"id":0,"passengerOrderHashMap":[[{"id":2,"role":2,"phoneNumber":"0666076706","fbProfile":{"id":"id_link2","type":2,"link":"https://plus.google.com/+AlexanderZhovnuvaty","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя2","surName":"Фамилия2","gender":2,"age":34,"email":"email2","birthday":"1983-03-26"}},{"id":1300,"totalSeats":2,"depLocation":{"mLongitudeE6":24007593,"mLatitudeE6":49823836,"mAltitude":0},"destLocation":{"mLongitudeE6":24053202,"mLatitudeE6":49864560,"mAltitude":0},"depAddress":"From 1","destAddress":"To 1","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":4,"role":2,"phoneNumber":"0666076707","vkProfile":{"id":"id_link5","type":3,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя5","surName":"Фамилия5","gender":2,"age":34,"email":"email5","birthday":"1983-03-27"}},{"id":1301,"totalSeats":2,"depLocation":{"mLongitudeE6":24017829,"mLatitudeE6":49801100,"mAltitude":0},"destLocation":{"mLongitudeE6":24029501,"mLatitudeE6":49844071,"mAltitude":0},"depAddress":"From 2","destAddress":"To 2","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":1,"role":2,"phoneNumber":"0666076705","gPlusProfile":{"id":"id_link1","type":1,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя1","surName":"Фамилия1","gender":1,"age":33,"email":"email1","birthday":"1982-03-25"}},{"id":1299,"totalSeats":2,"depLocation":{"mLongitudeE6":23990761,"mLatitudeE6":49811403,"mAltitude":0},"destLocation":{"mLongitudeE6":24010512,"mLatitudeE6":49826688,"mAltitude":0},"depAddress":"From 0","destAddress":"To 0","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":5,"role":2,"phoneNumber":"0666076708","vkProfile":{"id":"id_link8","type":3,"link":"https://www.facebook.com/app_scoped_user_id/1637344933216693/","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя8","surName":"Фамилия8","gender":2,"age":34,"email":"email8","birthday":"1983-03-28"}},{"id":1302,"totalSeats":2,"depLocation":{"mLongitudeE6":24017314,"mLatitudeE6":49812844,"mAltitude":0},"destLocation":{"mLongitudeE6":24000663,"mLatitudeE6":49816720,"mAltitude":0},"depAddress":"From 3","destAddress":"To 3","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}]],"stops":{"0":{"passengerId":4,"orderId":1301,"type":1},"1":{"passengerId":5,"orderId":1302,"type":1},"2":{"passengerId":1,"orderId":1299,"type":1},"3":{"passengerId":5,"orderId":1302,"type":2},"4":{"passengerId":2,"orderId":1300,"type":1},"5":{"passengerId":1,"orderId":1299,"type":2},"6":{"passengerId":4,"orderId":1301,"type":2},"7":{"passengerId":2,"orderId":1300,"type":2}},"stateId":1,"price":120},{"id":0,"passengerOrderHashMap":[[{"id":2,"role":2,"phoneNumber":"0666076706","fbProfile":{"id":"id_link2","type":2,"link":"https://plus.google.com/+AlexanderZhovnuvaty","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя2","surName":"Фамилия2","gender":2,"age":34,"email":"email2","birthday":"1983-03-26"}},{"id":1300,"totalSeats":2,"depLocation":{"mLongitudeE6":24007593,"mLatitudeE6":49823836,"mAltitude":0},"destLocation":{"mLongitudeE6":24053202,"mLatitudeE6":49864560,"mAltitude":0},"depAddress":"From 1","destAddress":"To 1","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}],[{"id":1,"role":2,"phoneNumber":"0666076705","gPlusProfile":{"id":"id_link1","type":1,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя1","surName":"Фамилия1","gender":1,"age":33,"email":"email1","birthday":"1982-03-25"}},{"id":1299,"totalSeats":2,"depLocation":{"mLongitudeE6":23990761,"mLatitudeE6":49811403,"mAltitude":0},"destLocation":{"mLongitudeE6":24010512,"mLatitudeE6":49826688,"mAltitude":0},"depAddress":"From 0","destAddress":"To 0","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}],[{"id":5,"role":2,"phoneNumber":"0666076708","vkProfile":{"id":"id_link8","type":3,"link":"https://www.facebook.com/app_scoped_user_id/1637344933216693/","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя8","surName":"Фамилия8","gender":2,"age":34,"email":"email8","birthday":"1983-03-28"}},{"id":1302,"totalSeats":2,"depLocation":{"mLongitudeE6":24017314,"mLatitudeE6":49812844,"mAltitude":0},"destLocation":{"mLongitudeE6":24000663,"mLatitudeE6":49816720,"mAltitude":0},"depAddress":"From 3","destAddress":"To 3","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}]],"stops":{"0":{"passengerId":5,"orderId":1302,"type":1},"1":{"passengerId":1,"orderId":1299,"type":1},"2":{"passengerId":5,"orderId":1302,"type":2},"3":{"passengerId":2,"orderId":1300,"type":1},"4":{"passengerId":1,"orderId":1299,"type":2},"5":{"passengerId":2,"orderId":1300,"type":2}},"stateId":1,"price":120},{"id":0,"passengerOrderHashMap":[[{"id":2,"role":2,"phoneNumber":"0666076706","fbProfile":{"id":"id_link2","type":2,"link":"https://plus.google.com/+AlexanderZhovnuvaty","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя2","surName":"Фамилия2","gender":2,"age":34,"email":"email2","birthday":"1983-03-26"}},{"id":1300,"totalSeats":2,"depLocation":{"mLongitudeE6":24007593,"mLatitudeE6":49823836,"mAltitude":0},"destLocation":{"mLongitudeE6":24053202,"mLatitudeE6":49864560,"mAltitude":0},"depAddress":"From 1","destAddress":"To 1","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":4,"role":2,"phoneNumber":"0666076707","vkProfile":{"id":"id_link5","type":3,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя5","surName":"Фамилия5","gender":2,"age":34,"email":"email5","birthday":"1983-03-27"}},{"id":1301,"totalSeats":2,"depLocation":{"mLongitudeE6":24017829,"mLatitudeE6":49801100,"mAltitude":0},"destLocation":{"mLongitudeE6":24029501,"mLatitudeE6":49844071,"mAltitude":0},"depAddress":"From 2","destAddress":"To 2","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":1,"role":2,"phoneNumber":"0666076705","gPlusProfile":{"id":"id_link1","type":1,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя1","surName":"Фамилия1","gender":1,"age":33,"email":"email1","birthday":"1982-03-25"}},{"id":1299,"totalSeats":2,"depLocation":{"mLongitudeE6":23990761,"mLatitudeE6":49811403,"mAltitude":0},"destLocation":{"mLongitudeE6":24010512,"mLatitudeE6":49826688,"mAltitude":0},"depAddress":"From 0","destAddress":"To 0","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}],[{"id":5,"role":2,"phoneNumber":"0666076708","vkProfile":{"id":"id_link8","type":3,"link":"https://www.facebook.com/app_scoped_user_id/1637344933216693/","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя8","surName":"Фамилия8","gender":2,"age":34,"email":"email8","birthday":"1983-03-28"}},{"id":1302,"totalSeats":2,"depLocation":{"mLongitudeE6":24017314,"mLatitudeE6":49812844,"mAltitude":0},"destLocation":{"mLongitudeE6":24000663,"mLatitudeE6":49816720,"mAltitude":0},"depAddress":"From 3","destAddress":"To 3","timestamp":1443703796000,"clientType":1,"stateId":1,"price":30}]],"stops":{"0":{"passengerId":4,"orderId":1301,"type":1},"1":{"passengerId":5,"orderId":1302,"type":1},"2":{"passengerId":1,"orderId":1299,"type":1},"3":{"passengerId":5,"orderId":1302,"type":2},"4":{"passengerId":2,"orderId":1300,"type":1},"5":{"passengerId":1,"orderId":1299,"type":2},"6":{"passengerId":4,"orderId":1301,"type":2},"7":{"passengerId":2,"orderId":1300,"type":2}},"stateId":1,"price":120},{"id":0,"passengerOrderHashMap":[[{"id":2,"role":2,"phoneNumber":"0666076706","fbProfile":{"id":"id_link2","type":2,"link":"https://plus.google.com/+AlexanderZhovnuvaty","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя2","surName":"Фамилия2","gender":2,"age":34,"email":"email2","birthday":"1983-03-26"}},{"id":1300,"totalSeats":2,"depLocation":{"mLongitudeE6":24007593,"mLatitudeE6":49823836,"mAltitude":0},"destLocation":{"mLongitudeE6":24053202,"mLatitudeE6":49864560,"mAltitude":0},"depAddress":"From 1","destAddress":"To 1","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}],[{"id":1,"role":2,"phoneNumber":"0666076705","gPlusProfile":{"id":"id_link1","type":1,"link":"https://plus.google.com/118055503722424615520","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя1","surName":"Фамилия1","gender":1,"age":33,"email":"email1","birthday":"1982-03-25"}},{"id":1299,"totalSeats":2,"depLocation":{"mLongitudeE6":23990761,"mLatitudeE6":49811403,"mAltitude":0},"destLocation":{"mLongitudeE6":24010512,"mLatitudeE6":49826688,"mAltitude":0},"depAddress":"From 0","destAddress":"To 0","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}],[{"id":5,"role":2,"phoneNumber":"0666076708","vkProfile":{"id":"id_link8","type":3,"link":"https://www.facebook.com/app_scoped_user_id/1637344933216693/","imgUrl":"https://lh3.googleusercontent.com/-RAgLglo1zEg/AAAAAAAAAAI/AAAAAAAACB4/tObTcEGkReE/photo.jpg?sz=50","name":"Имя8","surName":"Фамилия8","gender":2,"age":34,"email":"email8","birthday":"1983-03-28"}},{"id":1302,"totalSeats":2,"depLocation":{"mLongitudeE6":24017314,"mLatitudeE6":49812844,"mAltitude":0},"destLocation":{"mLongitudeE6":24000663,"mLatitudeE6":49816720,"mAltitude":0},"depAddress":"From 3","destAddress":"To 3","timestamp":1443703796000,"clientType":1,"stateId":1,"price":40}]],"stops":{"0":{"passengerId":5,"orderId":1302,"type":1},"1":{"passengerId":1,"orderId":1299,"type":1},"2":{"passengerId":5,"orderId":1302,"type":2},"3":{"passengerId":2,"orderId":1300,"type":1},"4":{"passengerId":1,"orderId":1299,"type":2},"5":{"passengerId":2,"orderId":1300,"type":2}},"stateId":1,"price":120}],"state":"success"}'


def get_json():
    # url = 'http://188.40.133.134:8480/GatherCarBackend/GCServlet'
    # payload = {"action": "get_potential_routes", "weight": 8}
    # headers = {'Accept-Encoding': 's'}
    # response = requests.post(url, data=json.dumps(payload), headers=headers)
    output = json.loads(text)
    # cnt = len(output['list'])
    # for i in range(cnt):
    #     return output['list'][0]
    return output['list']


def get_routes_cnt():
    json = get_json()
    cnt = len(json)
    return cnt

def test():
    route = get_route_by_pos(0)
    return route['stops']

def get_route_by_pos(pos):
    route = get_json()[pos]
    return route

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def get_coord_by_order_id(order_id, route_pos, start=True):
    passenger = 0
    cor = {}
    # for i in range(get_routes_cnt()):
    route = get_route_by_pos(route_pos)
    for order in range(len(route['stops'])):
        id = str(order)
        if order_id == route['stops'][id]['orderId']:
            passengerId = route['stops'][id]['passengerId']
            passenger = passengerId
    # for i in range(get_routes_cnt()):
    route = get_route_by_pos(route_pos)
    for order in range(len(route['passengerOrderHashMap'])):
        if route['passengerOrderHashMap'][order][0]['id'] == passenger:
            if start:
                lng = route['passengerOrderHashMap'][order][1]['depLocation']['mLongitudeE6']
                lat = route['passengerOrderHashMap'][order][1]['depLocation']['mLatitudeE6']
                cor.update({"lat": float(str(lat)[:2]+"."+str(lat)[2:]), "lng": float(str(lng)[:2]+"."+str(lng)[2:]), "description": (order_id, 'Get On'), "label": 'S', "numbers of passanger on the route": (len(route['passengerOrderHashMap']))})
            else:
                lng = route['passengerOrderHashMap'][order][1]['destLocation']['mLongitudeE6']
                lat = route['passengerOrderHashMap'][order][1]['destLocation']['mLatitudeE6']
                cor.update({"lat": float(str(lat)[:2]+"."+str(lat)[2:]), "lng": float(str(lng)[:2]+"."+str(lng)[2:]), "description": (order_id, 'Get Out'), "label": 'F', "numbers of passanger on the route": (len(route['passengerOrderHashMap']))})
    return cor

def get_cord_of_all_routes():
    routes = []
    for i in range(get_routes_cnt()):
        route = get_route_by_pos(i)
        coor_one_route = []
        for order in range(len(route['stops'])):
            id = str(order)
            type = route['stops'][id]['type']
            order_id = route['stops'][id]['orderId']
            if type == 1:
                cor = get_coord_by_order_id(order_id, i, start=True)
                coor_one_route.append(cor)
            else:
                cor = get_coord_by_order_id(order_id, i, start=False)
                coor_one_route.append(cor)
        routes.append(coor_one_route)
    return routes

def search_form(request):
    return render(request, 'search_form.html')


def google_maps(request):
    routes = get_cord_of_all_routes()
    json_for_js = json.dumps(get_cord_of_all_routes())
    return render(request, 'google_maps.html', {'json': json_for_js, 'routes': routes, 'range': range(len(routes))})

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_form.html',
        {'errors': errors})


# def contact(request):
#     # if request.method == 'POST':
#     #     form = ContactForm(request.POST)
#     #     if form.is_valid():
#     #         cd = form.cleaned_data
#     #         send_mail(
#     #             cd['subject'],
#     #             cd['message'],
#     #             cd.get('email', 'noreply@example.com'),
#     #             ['siteowner@example.com'],
#     #         )
#     #         return HttpResponseRedirect('/contact/thanks/')
#     # else:
#     #     form = ContactForm(
#     #         initial={'subject': 'I love your site!'}
#     #     )
#     form = get_cord_of_all_routes()
#     points = json.dumps(get_cord_of_all_routes())
#     return render(request, 'google_maps.html', {'json': form})

