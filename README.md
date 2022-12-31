# Huawei Cloud Practicum Final Project

## Project Description

A certificate generation project will be designed using Huawei Cloud services. New certificates will be obtained by printing the name-surname data stored in Google Sheets to the blank certificate. This will be done by creating a button in Google Sheets, the API Gateway address will be given to the button to establish a connection, each time the button is clicked, the API will go to the empty image file in OBS and print the name it pulls from the table to the image file with the code in the function graph, then store these certificates in a different OBS address.

## Used Huawei Cloud Services

Function Graph: Function Graph transforms data and stores the transformed data in OBS and calls a function that writes the captured data to the image.

Object Storage Service: Image files are stored. It stores the initial version of the image file and the last processed outputs.

API Gatewey: The API Gateway represents incoming records and passes raw data records directly to the Function Graph.


## Technical Architecture

Its technical architecture is as in the drawing below.

![This is an image](https://github.com/haticedikmn/HuaweiCloudPracticumFinalCase/blob/main/image/TechnicalArchitecture.png)<br/><br/>

1 - With the Python pillow library, image processing was performed by taking the coordinates of a specific point on the image. The function created in the Function Graph service was given one API Gateway output and one OBS output to store images in buckets. Image processing codes were integrated into the Function Graph service.

![This is an image](https://github.com/haticedikmn/HuaweiCloudPracticumFinalCase/blob/main/image/functiongraph.png)<br/><br/>

2- The image used in the project was stored in the certificate-input bucket in the Object Storege Service. Another bucket, certificate-output, was created to store the image after processing.

![This is an image](https://github.com/haticedikmn/HuaweiCloudPracticumFinalCase/blob/main/image/obs1.png)<br/><br/>

3- A button was created in Google Sheets and the Function Graph service was triggered by integrating the API address into the function of the created button.

![This is an image](https://github.com/haticedikmn/HuaweiCloudPracticumFinalCase/blob/main/image/api.png)<br/><br/>

3.1- The data of 121 people in the Patika Cohorts were entered into the Google Sheets table and the function was written by creating a button.

![This is an image](https://github.com/haticedikmn/HuaweiCloudPracticumFinalCase/blob/main/image/googlesheets.png)<br/><br/>

4- Thus, when each button is clicked, the names in the table will be printed to the certificate in the input bucket on OBS and saved to the output bucket.

OBS -> certificate_input
![This is an image](https://github.com/haticedikmn/HuaweiCloudPracticumFinalCase/blob/main/image/certificate_input.png)<br/><br/>

OBS -> certificate_ output 
![This is an image](https://github.com/haticedikmn/HuaweiCloudPracticumFinalCase/blob/main/image/certificate_output.png)<br/><br/>

5- The steps were carried out by designing a certificate instance for Huawei Practicum. As a result of the steps, the first image file and the second image file are as shown.

### Startup screen 
![This is an image](https://github.com/haticedikmn/HuaweiCloudPracticumFinalCase/blob/main/image/template.jpg)<br/><br/>

### Result screen
![This is an image](https://github.com/haticedikmn/HuaweiCloudPracticumFinalCase/blob/main/image/Hatice%20Dikmen.jpg)<br/><br/>
