
local MainScene = class("MainScene", cc.load("mvc").ViewBase)

function MainScene:onCreate()
    -- add background image
    display.newSprite("HelloWorld.png")
        :move(display.center)
        :addTo(self)

    -- add HelloWorld label
    cc.Label:createWithSystemFont("Hello World", "Arial", 40)
        :move(display.cx, display.cy + 200)
        :addTo(self)
	
	self:downloaderTest() 
end

local index = 0 
function MainScene:downloaderTest()
	local button = ccui.Button:create("HelloWorld.png")
		:move(cc.pAdd(display.center, cc.p(0, -200)))
		:addTo(self)

	index = index + 1
	local callBack = function ( ... )
		local filePath = device.writablePath .. "christmas" .. tostring(index) .. ".jpg"
		print("Start download -- ", filePath)
		local taskId = cc.load("http").Downloader.downloadData(
			"https://httpbin.org/get", 
			function (result, data)
				print("download ended -- ", result, data)
			end
			)

		cc.load("http").Downloader.setProgressCallBack(taskId, function (bytesRec, totalBytesRec, totalBytesExpected)
			print("download progress -- ", totalBytesRec*100/totalBytesExpected)
		end)
	end

	button:onClick(callBack)
end

return MainScene
