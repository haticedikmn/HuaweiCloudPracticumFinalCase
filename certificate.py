# -*- coding: utf-8 -*-
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont
from obs import *

current_file_path = os.path.dirname(os.path.realpath(__file__))
# append current path to search paths, so that we can import some third party libraries.
sys.path.append(current_file_path)
obs_server = 'obs.myhuaweicloud.com'
region = 'ap-southeast-1'


def newObsClient(context):
    ak = context.getAccessKey()
    sk = context.getSecretKey()
    return ObsClient(access_key_id=ak, secret_access_key=sk, server=obs_server,
                     path_style=True, region=region, ssl_verify=False, max_retry_count=5, timeout=20)


def downloadFile(obsClient, bucket, objName, localFile):
    resp = obsClient.getObject(bucket, objName, localFile)
    if resp.status < 300:
        print
        'download file', file, 'succeed'
    else:
        print('download failed, errorCode: %s, errorMessage: %s, requestId: %s' % (resp.errorCode, resp.errorMessage,
                                                                                   resp.requestId))


def uploadFileToObs(client, bucket, objName, file):
    resp = client.putFile(bucket, objName, file)
    if resp.status < 300:
        print
        'upload file', file, 'succeed'
    else:
        print('upload failed, errorCode: %s, errorMessage: %s, requestId: %s' % (resp.errorCode, resp.errorMessage,
                                                                                 resp.requestId))


def getObjInfoFromObsEvent(event):
    # name = event['queryStringParameters'][0]['name']
    s3 = event['Records'][0]['s3']
    eventName = event['Records'][0]['eventName']
    bucket = s3['bucket']['name']
    objName = s3['object']['key']
    print
    "*** obsEventName: %s, srcBucketName: %s, objName: %s", eventName, bucket, objName
    return bucket, objName


# def fnt(im, name):
#    d = ImageDraw.Draw(im)
#    fnt = ImageFont.truetype("OpenSans-Regular.ttf", 50)
#    x = im.width / 2
#    y = im.height / 2
#    d.text((x - 190, y - 250), name, font=fnt, fill=(0, 0, 0))
#    return im, name

def fnt_image(tmpfile, fileName, name):
    # print('version',Image.__version__)
    print(os.getcwd())
    newname = name.encode('UTF-8')
    encodedname = ''.join([i if ord(i) < 128 else '_' for i in newname])
    # newname2 = newname.decode('UTF-8')
    fnt_path = os.path.join(current_file_path, "OpenSans-Regular.ttf")
    font = ImageFont.truetype(font=fnt_path, size=60, index=0, encoding='', layout_engine=None)
    print(font.getsize(newname))
    print('name', type(newname))
    # font = ImageFont.load_default()
    textsize = font.getsize(newname)
    print(textsize)
    # textsize = 417
    im = Image.open(tmpfile)
    # tmp_image_path = os.path.join(current_file_path, "template.jpg")
    # fnt = Image.open(tmp_image_path)

    d = ImageDraw.Draw(im)
    # fnt = ImageFont.truetype(font, 50)
    x = 960
    y = 280
    d.text((x - int(textsize[0]) / 2, y), name, font=font, fill=(0, 0, 0))

    # out = fnt(im, fnt)
    name = fileName.split('.')
    outFileName = encodedname + '-fnt.' + name[1]
    outFilePath = "/tmp/" + outFileName
    # outFilePath = "./" + outFileName

    if im:
        # out = out.convert('RGB')
        im.save(outFilePath)
        # out.save("{name}.jpg")
    else:
        print
        "Sorry, save file Failed."

    return outFileName, outFilePath


def handler(event, context):
    # return 'OK1'
    name = event['queryStringParameters'][0]['name']
    #name = 'hatice4'
    srcBucket, srcObjName = getObjInfoFromObsEvent(event)
    outputBucket = context.getUserData('obs_output_bucket')
    region = context.getUserData('obs_region')
    print('region: ' + region)
    if len(region) > 0:
        global obs_server
        obs_server = 'obs.' + region + '.myhuaweicloud.com'

        client = newObsClient(context)
        localFile = "/tmp/" + srcObjName  # download file uploaded by user from obs
        downloadFile(client, srcBucket, srcObjName, localFile)
        # name = event['queryStringParameters']['name']
        outFileName, outFile = fnt_image(localFile, srcObjName, name)
        uploadFileToObs(client, outputBucket, outFileName, outFile)
        #return {'statusCode': 200, 'body': json.dumps({'statusCode': 200}, indent=0, sort_keys=True, default=str)}
    else:
        return {'statusCode': 200, 'body': json.dumps({'statusCode': 200}, indent=0, sort_keys=True, default=str)}
        #return {"statusCode": 200, "isBase64Encoded": false, "headers": {"Content-Type": "application/json;charset=UTF-8"}
