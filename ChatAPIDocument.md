# Chat API Document

## 目錄

**註冊流程**

- [頭像上傳](#photo)
- [註冊](#reg)
- [登陸](#login)

**用戶相關**

- [搜索好友](#searchUser)
- [獲取用戶基本信息](#base)
- [獲取用戶個人信息](#getUserInfo)
- [獲取群聊列表](#chatList)
- [獲取好友列表](#friendList)
- [獲取新朋友列表](#applyFriend)
- [獲取群驗證消息列表](#applyGroup)

**系統相關**
- [獲取系統動態菜單](#getList)
- [獲取視頻配置](#videoConfig)




<br>

<a id="photo"></a>
## 頭像上傳

***Path***

```
POST /im/in/photo
```

<br>

***Request***

- ***Body (form-data)***
	
	| 參數名稱 | 資料類型 | 必填 | 說明      |
	| --- | --- | --- |---------|
	| username | String | Y | 用戶名     |
	| file | binary | Y | 文件（二進制） |

- ***範例***

	```Form Data
		username: damdao
		file: (binary)
	```
	
<br>

***Response***
    
- ***Body***

{"err":0,"msg":"success"}

- ***Status code***

    | 錯誤代碼 | 說明     |
    |------|--------|
    | 200  | 頭像上傳成功 |
    
<br>


<a id="reg"></a>
## 註冊

***Path***

```
POST /im/in/reg
```

<br>

***Request***

- ***Body (form-data)***
	
	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| account | String | Y | 帳號 (email 格式) |
	| password | String | Y | 密碼 (大小寫英文數字組合，最少8碼。至少1大寫英文，1小寫英文，1數字) |

- ***範例***

	```Form Data
		nickname: rfdqef
		password: 11111111
		client_id: 
		type: REGISTER
		sex: 1
		invite_code: 111111
		username: damdao
		mobileCode: 0
		_token: 
		_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body***

	```json
    {"err":1,"msg":"这个用户名已经存在了"}
	```
- ***Status code***

    | 錯誤代碼 | 說明              |
    | --- |-----------------|
    | 200 | 調用成功（但是有可能註冊失敗） |
    
<br>


<a id="login"></a>
## 登入

***Path***

```
POST /im/in/login
```

<br>

***Request***

- ***Header***
	無

- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明           |
	| --- | --- |----|--------------|
	| username | String | Y  | 用戶名          |
 	| password | String | Y  | 密碼           |
	| client_id | String | N  | 客戶端id        |
	| invite_code | String | N  | 邀請碼          |
 	| _token | String | N  | Token，登陸時不需要 |
	| _agent_id | String | Y  | 租戶id         |

	***範例***

	```Form Data
	username: ffffff
	password: 111111
	client_id: 
	invite_code: 
	_token: 
	_agent_id: 1
	```

<br>
***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
	"err": 0,
	"msg": "登陆成功",
	"data": {
		"myavatar": "user\/32835\/300.jpg",
		"myname": "ffffff",
		"userid": "Mac_trtc_32835",
		"usersig": "eJxNjstugzAQRf*FddUYOzakO0RIBWkWpI*IqpJlbAMu4hHjIpKq-x5AROosz5k7c3*tt5fXR8Z581Mbai6ttJ4sYD3MWAlZG5UpqUd4YJwabThF0EV42WBtqwRlhiIt-gU7UdJZjcxeA4BdBAhcpBxapSVlmZnvEnBP9VJ3qqlHBoGNbYjANIs0qpqq2Q5CiBC0JvdXKp-KBYkfxlu841X0vB-0e9Kn*efwkZzc3LtsD*BMemhXSVjgc5eW5TEOCy*MT0Pg5W3ffK06TnDqe10UFVeyv4bC*YaZCop6U-mRc9xYfzcsBVoa",
		"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg",
		"bottom_url": ""
	}
	}
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | - | --- |
    | 0 | 登陆成功 |

<br>


<a id="searchUser"></a>
## 搜索好友

***Path***

```
POST /im/get/searchUser
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型 | 必填 | 說明    |
	| --- | --- |----|-------|
	| val | String | Y  | 搜索關鍵字 |
 	| _token | String | Y  | TOKEN |
	| _agent_id | String | Y  | 租戶id  |

	***範例***

	```Form Data
	val: f
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{"err":0,"msg":"success","data":{"data":[],"is_type":0}}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="base"></a>
## 獲取用戶基本信息

***Path***

```
POST /im/get/base
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型 | 必填 | 說明    |
	| --- | --- |----|-------|
 	| _token | String | Y  | TOKEN |
	| _agent_id | String | Y  | 租戶id  |

	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "err": 0,
    "msg": "success",
    "data": {
        "user_info": {
            "id": 32835,
            "nickname": "ffffff",
            "username": "ffffff",
            "photo": "user\/32835\/300.jpg",
            "doodling": "本宝宝暂时还没有想到个性的签名",
            "sex": 1,
            "circle_img": "default_circle_img.jpg",
            "money": "0.00",
            "trade_password": ""
        },
        "new_group_tips_num": 0,
        "new_friend_tips_num": 0,
        "no_reader_chat_num": 0,
        "no_reader_circle": 0,
        "no_reader_circle_chat_num": 0,
        "kefu_list_id": "",
        "bottom_url": "",
        "pc_page_title": "IM",
        "disappear_after_read": "1",
        "disappear_delay_time": "3"
    }
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

<a id="getUserInfo"></a>
## 獲取用戶個人信息

***Path***

```
POST /im/get/getUserInfo
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型 | 必填 | 說明    |
	| --- | --- |----|-------|
 	| _token | String | Y  | TOKEN |
	| _agent_id | String | Y  | 租戶id  |

	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "err": 0,
    "msg": "success",
    "data": {
        "id": 32835,
        "username": "ffffff",
        "nickname": "ffffff",
        "doodling": "本宝宝暂时还没有想到个性的签名",
        "email": "",
        "phone": "ffffff",
        "sex": 1,
        "password": "96e79218965eb72c92a549dd5a330112",
        "trade_password": "",
        "money": "0.00",
        "freeze_money": "0.00",
        "point": 0,
        "type": 1,
        "status": 0,
        "create_time": 1733366324,
        "circli_img": "",
        "is_customer_service": 0,
        "agent_id": 1,
        "update_time": 1733366324,
        "client_id": "",
        "q_permition": 1,
        "tj_username": "",
        "ip": "128.22.165.211",
        "ip_cityname": "",
        "ip_status": 0,
        "phone_status": 0,
        "phone_type": 0,
        "is_robot": 0,
        "storge": 0,
        "default_friend_id": 0,
        "channel": "",
        "last_login": null,
        "invite_list": null,
        "face": "user\/32835\/300.jpg",
        "photo": "user\/32835\/300.jpg"
    }
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>



<a id="getList"></a>
## 獲取系統動態菜單

***Path***

```
POST /im/middle.Middle/get_list
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型 | 必填 | 說明    |
	| --- | --- |----|-------|
 	| _token | String | Y  | TOKEN |
	| _agent_id | String | Y  | 租戶id  |

	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "total": 1,
    "per_page": 15,
    "current_page": 1,
    "last_page": 1,
    "data": [
        {
            "id": 7,
            "name": "趣味",
            "url": "https:\/\/www.kuhl.com",
            "logo": "\/uploads\/20240913\/0b292fcb9aa2bdfd903d633414167b81.jpg",
            "status": 1,
            "createtime": 1726228888
        }
    ]
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="videoConfig"></a>
## 獲取視頻配置

***Path***

```
POST /im/App/videoConfig
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***
	無
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "err": 0,
    "msg": "",
    "data": {
        "vedio_privatekey": "e6618ac0c79b157844715e7231a039e26b424349cbe6c5f0221c0ebdcf6ba9ef",
        "vedio_appid": "1600057106",
        "key": "vedio",
        "tab_id": "3"
    }
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

<a id="chatList"></a>
## 獲取群聊列表

***Path***

```
POST /im/get/chatList
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型 | 必填 | 說明    |
	| --- | --- |----|-------|
 	| _token | String | Y  | TOKEN |
	| _agent_id | String | Y  | 租戶id  |

	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "total": 1,
    "per_page": 15,
    "current_page": 1,
    "last_page": 1,
    "data": [
        {
            "id": 7,
            "name": "趣味",
            "url": "https:\/\/www.kuhl.com",
            "logo": "\/uploads\/20240913\/0b292fcb9aa2bdfd903d633414167b81.jpg",
            "status": 1,
            "createtime": 1726228888
        }
    ]
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

<a id="friendList"></a>
## 獲取好友列表

***Path***

```
POST /im/get/friendList
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明    |
	| -- |---------|----|-------|
  	| list_id | String  | Y  | 列表id  |
	| friend | Integer | Y  | 好友數量？ |
 	| _token | String  | Y  | TOKEN |
	| _agent_id | String  | Y  | 租戶id  |

	***範例***

	```Form Data
	list_id: 0
	friend: 1
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{"err":0,"data":{"data":[],"member":[]}}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

<a id="friendList"></a>
## 獲取好友列表

***Path***

```
POST /im/get/friendList
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明    |
	| -- |---------|----|-------|
  	| list_id | String  | Y  | 列表id  |
	| friend | Integer | Y  | 好友數量？ |
 	| _token | String  | Y  | TOKEN |
	| _agent_id | String  | Y  | 租戶id  |

	***範例***

	```Form Data
	list_id: 0
	friend: 1
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{"err":0,"data":{"data":[],"member":[]}}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="applyFriend"></a>
## 獲取新朋友列表

***Path***

```
POST /im/get/applyFriend
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型 | 必填 | 說明    |
	| --- | --- |----|-------|
 	| _token | String | Y  | TOKEN |
	| _agent_id | String | Y  | 租戶id  |

	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{"err":0,"msg":"success","data":[]}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="applyGroup"></a>
## 獲取群驗證消息列表

***Path***

```
POST /im/get/applyGroup
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型 | 必填 | 說明    |
	| --- | --- |----|-------|
 	| _token | String | Y  | TOKEN |
	| _agent_id | String | Y  | 租戶id  |

	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{"err":0,"msg":"success","data":[]}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>




























<a id="queryDevices"></a>
## 查詢已註冊裝置清單

查詢已註冊的裝置清單

***Path***

```
GET /api/v1/manage/device/{projectID}
```
<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	
<br>

- ***Path Parameters***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| projectID | String | Y | 專案唯一識別碼 |

<br>

- ***Query Parameters***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| platform | String | N | 平台 |
	| deviceID | String | N | 推播裝置的唯一識別碼 |
	| token | Bool | N | 推播Token |
	| bundleID | String | N | App唯一識別碼 |
	| version | String | N | SDK版本號 |
	| appVersion | String | N | App版本號 |
	| deviceBrand | String | N | 裝置廠牌 |
	| deviceModel | String | N | 裝置型號 |
	| osVersion | String | N | 裝置系統版本 |
	| limit | Int | N | 資料筆數 (1-300)，預設100 |
	| startDate | Timestamp(秒) | N | 起始時間 |
	| endDate | Timestamp(秒) | N | 結束時間 |

<br>

***Response***

- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 唯一識別碼 |
	| deviceID | String | Y | 推播裝置的唯一識別碼 |
	| platform | String | Y | 平台 |
	| token | Bool | Y | 推播Token |
	| bundleID | String | Y | App唯一識別碼 |
	| version | String | Y | SDK版本號 |
	| appVersion | String | Y | App版本號 |
	| deviceBrand | String | Y | 裝置廠牌 |
	| deviceModel | String | Y | 裝置型號 |
	| osVersion | String | Y | 裝置系統版本 |
	| updateDate | Timestamp(秒) | Y | 更新時間 |
	| createDate | Timestamp(秒) | Y | 建立時間 |

- ***範例***

	```json
	[
		{
			"id":"XXXX-XXXX-XXXX-XXXX",
			"deviceID":"XXXX-XXXX-XXXX-XXXX",
			"platform":"ios",
			"token": "XXXX-XXXX-XXXX-XXXX",
			"bundleID": "com.xxx.xxx",
			"version": "SDK版本號",
			"appVersion": "App版本號",
			"deviceBrand": "裝置廠牌",
			"deviceModel": "裝置型號",
			"osVersion": "裝置系統版本",
			"updateDate": 1234567890,
			"createDate": 1234567890
		},
	]
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

