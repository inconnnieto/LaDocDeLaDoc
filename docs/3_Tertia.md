# Tertia

a network is a group of computers connected to each other 

the core of the internet is 

## ``` GET https://dummyjson.com:443/recipes?limit=10 HTTP/2```

## HTTP request
Hyper text transfer protocol

it is a message sent by a client (web browser/ mobile app) to a server to initiate an action / retrieve information

typically consists of 3 main parts: 

type: protocol request 
in text-based format

## DNS 
Domain name system

used to translate domain names into IP address.

Here it will translate `dummyjson.com` into IP address that computers will use to identify each other

when a domain name is entered into a web browser computer sends a DNS query to DNS server which returns the corresponding IP address

dns is like a phonebook

## GET 

it is the Request line of the `HTTP` request.

It specifies the request `method` used to transfer data between client & server

 retrieve data from a specified resource

it indicates that the client wants to fetch information rather than submit data

expects response from server

`GET` retrieves data from the server without modifying it

will always return a HTTP response

it is the name of the function

## https:// 
Hypertext Transfer Protocol Secure

secure version of HTTP

it encrypts data exchanged between client and server

## dummyjson.com 
Domain name

they are fixed and unique.

input in DNS to get IP

IATA 8 servers ww 


## 443 
port number used for the HTTPS protocol.

it indicates the specific port on the server `(dummyjson.com)` that is designed for secure web traffic.

The default port used for secure encrypted HTTPS connections.

It facilitates communication over the internet by routing traffic to the appropriate service.

## recipes 
it indicates that the request is for recipe data, allowing the client to retrieve information related to recipes from the specified service.

le nom de la page qu'on veut afficher
le nom de la resource

sinon code 404

## ? 

separator 

everything before is URL and after is variables and parameters

separates the main part of the URL from the query parameters

beginning of the query string in the URL. This part of the URL is used to pass additional parameters to the server, allowing the client to specify criteria for the request—in this case, it’s used to indicate that the client wants to limit the number of recipe entries returned to 10.

## limit 

In this case, limit=10 is a query parameter that specifies a constraint or option for the request. Here, it indicates that you want to limit the results to 10 items. 

A query parameter that specifies how many items to return in the response. It allows clients to control the amount of data retrieved.

## 10
The value associated with the "limit" parameter, indicating that the client wants to receive a maximum of 10 `recipe` entries. It helps manage response size.

## HTTP/2 
The second major version of the HTTP protocol, improving speed and performance. It allows multiple requests to be sent simultaneously over a single connection.

protocol & version du protocol

## Que contient la réponse à cette requête ?

retrieve 10 recipes from `dummyjson.com`

contenu tableau json avec 10 recettes