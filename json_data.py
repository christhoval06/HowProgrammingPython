from json import loads


data = """
[{
  "id": 1,
  "first_name": "Jaymee",
  "last_name": "Maleham",
  "email": "jmaleham0@t.co",
  "gender": "Female",
  "ip_address": "239.91.6.65"
}, {
  "id": 2,
  "first_name": "Rooney",
  "last_name": "Ruprecht",
  "email": "rruprecht1@cornell.edu",
  "gender": "Male",
  "ip_address": "196.217.207.118"
}, {
  "id": 3,
  "first_name": "Manuel",
  "last_name": "Elphinston",
  "email": "melphinston2@vk.com",
  "gender": "Male",
  "ip_address": "69.134.191.72"
}, {
  "id": 4,
  "first_name": "Morgan",
  "last_name": "Court",
  "email": "mcourt3@vistaprint.com",
  "gender": "Male",
  "ip_address": "27.84.15.39"
}, {
  "id": 5,
  "first_name": "Fiann",
  "last_name": "Angrove",
  "email": "fangrove4@github.com",
  "gender": "Female",
  "ip_address": "173.45.93.185"
}, {
  "id": 6,
  "first_name": "Arvin",
  "last_name": "Shippey",
  "email": "ashippey5@wikispaces.com",
  "gender": "Male",
  "ip_address": "185.32.95.105"
}, {
  "id": 7,
  "first_name": "Mychal",
  "last_name": "Piggen",
  "email": "mpiggen6@springer.com",
  "gender": "Male",
  "ip_address": "111.228.231.48"
}, {
  "id": 8,
  "first_name": "Milt",
  "last_name": "Olrenshaw",
  "email": "molrenshaw7@de.vu",
  "gender": "Male",
  "ip_address": "249.10.117.136"
}, {
  "id": 9,
  "first_name": "Delmer",
  "last_name": "Mellows",
  "email": "dmellows8@scribd.com",
  "gender": "Male",
  "ip_address": "63.83.20.226"
}, {
  "id": 10,
  "first_name": "Ryon",
  "last_name": "McConnal",
  "email": "rmcconnal9@pcworld.com",
  "gender": "Male",
  "ip_address": "93.251.12.87"
}]
"""

users = loads(data)
