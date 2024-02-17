# Hungarian lottery statistics (Otoslotto)

This simple Python script extracts the data of the Hungarian Lottery (5Hit) and prints out the five most
prevalent numbers.

## Description of the project

I was just curious if there was some way to extract all data from the official [website](https://bet.szerencsejatek.hu/jatekok/otoslotto/szamstatisztika)
The official website didn't allow me to find the top 5 most prevalent numbers from the drawings, as it only showcased the numbers, which I input.

First, I thought getting data for 5 specific numbers was handled through queries and requests, whenever I clicked the "Get stats" button

It turned out, that their website always receives a json from a google analytics site, which includes every lottery data from 1953 until today.
I realised this while using the dev tools of the browser and the network tab especially.
Showing only the five specific numbers that I asked for, was handled on the client side (Angular)

With this find, I could extract all data of all drawings and numbers, and get the top5 easily
