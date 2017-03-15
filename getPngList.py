import sys
import os
import hashlib
import json

picList = {
	'aaa':['jpg', 'bbb'],
	'bbb':['jpg', 'aaa', 'ccc'],
	'ccc':['jpg', 'bbb', 'aaa']
}

confJosnArr = {}
picNameMapMd5 = {}

def getJsonConf(name):
	return confJosnArr[name]

def getBigFileMD5(filepath):
    if os.path.isfile(filepath):
        md5obj = hashlib.md5()
        maxbuf = 8192
        f = open(filepath,'rb')
        while True:
            buf = f.read(maxbuf)
            if not buf:
                break
            md5obj.update(buf)
        f.close()
        hash = md5obj.hexdigest()
        return str(hash).upper()
    else:
    	return None

def createPicMd5Dict(fileDir):
	confDict = {}
	for name, nameList in picList.iteritems():
		tempDict = {}
		ext = nameList.pop(0)
		for picName in nameList:
			if (picName not in picNameMapMd5):
				extName = picName + '.' + ext
				picNameMapMd5[picName] = getBigFileMD5(os.path.join(fileDir, extName))
			tempDict[picName] = picNameMapMd5[picName]
		confDict[name] = tempDict

	return confDict

def createPicJsonDict(md5Dic):
	for name, md5List in md5Dic.iteritems():
		tempJson = {}
		tempJson['version'] = 1.0
		tempJson['picArr'] = md5List
		confJosnArr[name] = json.dumps(tempJson)



def init(fileDir):
	dic = createPicMd5Dict(fileDir)
	createPicJsonDict(dic)

init(os.path.join(sys.path[0], "pic"))
