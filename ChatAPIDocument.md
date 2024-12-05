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
- [我的收藏](#getUserStore)
- [我的收藏資源利用情況](#getStoreStatics)
- 
**聊天功能**
- [獲取聊天列表時間](#getListTime)
- [設置聊天列表時間](#setListTime)
- [獲取聊天成員列表](#getMemberList)
- [獲取聊天收藏列表](#myfavor)
- [獲取聊天成員頭像](#getMemberPhotos)
- [獲取聊天內容](#chatData)


**探索模塊**
- [獲取短視頻分類列表](#videoCategory)
- [獲取短視頻列表](#videoLists)
- [獲取短視頻指定用戶信息](#videoUserinfo)
- [獲取短視頻指定用戶作品列表](#videoUservideo)
- [獲取短視頻指定用戶喜歡列表](#videoFav)
- [獲取短視頻指定用戶評論列表](#videoCommonlog)


**系統相關**
- [獲取系統動態菜單](#getList)
- [獲取視頻配置](#videoConfig)
- [獲取探索界面自定義菜單](#getOnlineList)
- [獲取系統配置](#getConfig)
- [幫助中心文章列表](#getArticleList)
- [幫助中心文章詳情](#getArticleDetail)
- [客服](#kefu)



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


<a id="getOnlineList"></a>
## 獲取探索界面自定義菜單

***Path***

```
POST /im/agent/getOnlineList
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
    "msg": "网站列表",
    "data": [
        {
            "agent_id": "1",
            "appName": "小六合",
            "url": "https:\/\/www.kuhl.com",
            "port": "3303",
            "status": 0,
            "is_customer_service": [],
            "logo_url": "\/uploads\/20240807\/90339b73fce2d7db813f3f07797d753c.jpg",
            "create_time": 1723024592,
            "time": 1723024592,
            "id": "66b344d03a4cc73ada7f7ba3",
            "agent_user_id": 0
        }
    ]
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="videoCategory"></a>
## 獲取短視頻分類列表

***Path***

```
POST /im/video.Share/category
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
	[{"id":4,"name":"life"},{"id":16,"name":"news"}]
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>




<a id="videoCategory"></a>
## 獲取短視頻列表

***Path***

```
POST /im/video.Share/video_lists
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明     |
	| --- |---------|----|--------|
 	| _token | String  | Y  | TOKEN  |
	| _agent_id | String  | Y  | 租戶id   |
  	| page | Integer | Y  | 當前頁碼   |
	| type | Integer  | Y  | 視頻分類id |

	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
 	page: 4
    type: 0
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "total": 6,
    "per_page": 15,
    "current_page": "1",
    "last_page": 1,
    "data": [
        {
            "id": 31,
            "user_id": 32814,
            "title": "1234",
            "video": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.mp4",
            "gif": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.jpeg",
            "fabulous": 0,
            "comment": 0,
            "createtime": 1732089354,
            "status": "1",
            "category_id": 4,
            "is_fabulous": false,
            "is_follow": false,
            "user_info": {
                "id": 32814,
                "username": "swee99999",
                "nickname": "123654",
                "doodling": "本宝宝暂时还没有想到个性的签名",
                "email": "",
                "phone": "swee99999",
                "sex": 0,
                "password": "1ac633444cb5eb9cf03ab1f911732480",
                "trade_password": "",
                "money": "0.00",
                "freeze_money": "0.00",
                "point": 0,
                "type": 1,
                "status": 0,
                "create_time": 1732087726,
                "circli_img": "",
                "is_customer_service": 0,
                "agent_id": 1,
                "update_time": 1732091770,
                "client_id": "7f00000113240000068b",
                "q_permition": 1,
                "tj_username": "",
                "ip": "103.120.122.253",
                "ip_cityname": "",
                "ip_status": 0,
                "phone_status": 0,
                "phone_type": 0,
                "is_robot": 0,
                "storge": 11376,
                "default_friend_id": 0,
                "channel": "",
                "last_login": null,
                "invite_list": null,
                "face": "user\/32814\/300.jpg",
                "photo": "user\/32814\/300.jpg"
            }
        },
        {
            "id": 30,
            "user_id": 32814,
            "title": "1234",
            "video": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.mp4",
            "gif": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.jpeg",
            "fabulous": 0,
            "comment": 0,
            "createtime": 1732089353,
            "status": "1",
            "category_id": 4,
            "is_fabulous": false,
            "is_follow": false,
            "user_info": {
                "id": 32814,
                "username": "swee99999",
                "nickname": "123654",
                "doodling": "本宝宝暂时还没有想到个性的签名",
                "email": "",
                "phone": "swee99999",
                "sex": 0,
                "password": "1ac633444cb5eb9cf03ab1f911732480",
                "trade_password": "",
                "money": "0.00",
                "freeze_money": "0.00",
                "point": 0,
                "type": 1,
                "status": 0,
                "create_time": 1732087726,
                "circli_img": "",
                "is_customer_service": 0,
                "agent_id": 1,
                "update_time": 1732091770,
                "client_id": "7f00000113240000068b",
                "q_permition": 1,
                "tj_username": "",
                "ip": "103.120.122.253",
                "ip_cityname": "",
                "ip_status": 0,
                "phone_status": 0,
                "phone_type": 0,
                "is_robot": 0,
                "storge": 11376,
                "default_friend_id": 0,
                "channel": "",
                "last_login": null,
                "invite_list": null,
                "face": "user\/32814\/300.jpg",
                "photo": "user\/32814\/300.jpg"
            }
        },
        {
            "id": 29,
            "user_id": 32814,
            "title": "1234",
            "video": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.mp4",
            "gif": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.jpeg",
            "fabulous": 0,
            "comment": 0,
            "createtime": 1732089349,
            "status": "1",
            "category_id": 4,
            "is_fabulous": false,
            "is_follow": false,
            "user_info": {
                "id": 32814,
                "username": "swee99999",
                "nickname": "123654",
                "doodling": "本宝宝暂时还没有想到个性的签名",
                "email": "",
                "phone": "swee99999",
                "sex": 0,
                "password": "1ac633444cb5eb9cf03ab1f911732480",
                "trade_password": "",
                "money": "0.00",
                "freeze_money": "0.00",
                "point": 0,
                "type": 1,
                "status": 0,
                "create_time": 1732087726,
                "circli_img": "",
                "is_customer_service": 0,
                "agent_id": 1,
                "update_time": 1732091770,
                "client_id": "7f00000113240000068b",
                "q_permition": 1,
                "tj_username": "",
                "ip": "103.120.122.253",
                "ip_cityname": "",
                "ip_status": 0,
                "phone_status": 0,
                "phone_type": 0,
                "is_robot": 0,
                "storge": 11376,
                "default_friend_id": 0,
                "channel": "",
                "last_login": null,
                "invite_list": null,
                "face": "user\/32814\/300.jpg",
                "photo": "user\/32814\/300.jpg"
            }
        },
        {
            "id": 28,
            "user_id": 32814,
            "title": "1234",
            "video": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.mp4",
            "gif": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.jpeg",
            "fabulous": 0,
            "comment": 0,
            "createtime": 1732089342,
            "status": "1",
            "category_id": 4,
            "is_fabulous": false,
            "is_follow": false,
            "user_info": {
                "id": 32814,
                "username": "swee99999",
                "nickname": "123654",
                "doodling": "本宝宝暂时还没有想到个性的签名",
                "email": "",
                "phone": "swee99999",
                "sex": 0,
                "password": "1ac633444cb5eb9cf03ab1f911732480",
                "trade_password": "",
                "money": "0.00",
                "freeze_money": "0.00",
                "point": 0,
                "type": 1,
                "status": 0,
                "create_time": 1732087726,
                "circli_img": "",
                "is_customer_service": 0,
                "agent_id": 1,
                "update_time": 1732091770,
                "client_id": "7f00000113240000068b",
                "q_permition": 1,
                "tj_username": "",
                "ip": "103.120.122.253",
                "ip_cityname": "",
                "ip_status": 0,
                "phone_status": 0,
                "phone_type": 0,
                "is_robot": 0,
                "storge": 11376,
                "default_friend_id": 0,
                "channel": "",
                "last_login": null,
                "invite_list": null,
                "face": "user\/32814\/300.jpg",
                "photo": "user\/32814\/300.jpg"
            }
        },
        {
            "id": 27,
            "user_id": 32764,
            "title": "2233",
            "video": "\/static\/video\/32764\/20241101\/6d1e5819262694a5f05e2bf4034ae5be.MOV",
            "gif": "\/static\/video\/32764\/20241101\/6d1e5819262694a5f05e2bf4034ae5be.jpeg",
            "fabulous": 0,
            "comment": 0,
            "createtime": 1730441541,
            "status": "1",
            "category_id": 4,
            "is_fabulous": false,
            "is_follow": false,
            "user_info": {
                "id": 32764,
                "username": "18888888889",
                "nickname": "张三",
                "doodling": "本宝宝暂时还没有想到个性的签名",
                "email": "",
                "phone": "18888888889",
                "sex": 0,
                "password": "e10adc3949ba59abbe56e057f20f883e",
                "trade_password": "",
                "money": "0.00",
                "freeze_money": "0.00",
                "point": 0,
                "type": 1,
                "status": 0,
                "create_time": 1730439457,
                "circli_img": "",
                "is_customer_service": 0,
                "agent_id": 1,
                "update_time": 1730439457,
                "client_id": "",
                "q_permition": 1,
                "tj_username": "",
                "ip": "112.1.169.64",
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
                "face": "default_man\/300.jpg",
                "photo": "default_man\/300.jpg"
            }
        },
        {
            "id": 26,
            "user_id": 30426,
            "title": "6666666666",
            "video": "\/static\/video\/30426\/20240623\/2fd53cac2c346e45fc3b9f72621fad10.mp4",
            "gif": "\/static\/video\/30426\/20240623\/2fd53cac2c346e45fc3b9f72621fad10.jpeg",
            "fabulous": 4,
            "comment": 3,
            "createtime": 1719132525,
            "status": "1",
            "category_id": 4,
            "is_fabulous": false,
            "is_follow": false,
            "user_info": {
                "id": 30426,
                "username": "666666",
                "nickname": "666666",
                "doodling": "本宝宝暂时还没有想到个性的签名",
                "email": "",
                "phone": "666666",
                "sex": 1,
                "password": "96e79218965eb72c92a549dd5a330112",
                "trade_password": "",
                "money": "0.00",
                "freeze_money": "0.00",
                "point": 0,
                "type": 1,
                "status": 0,
                "create_time": 1719073586,
                "circli_img": "",
                "is_customer_service": 0,
                "agent_id": 1,
                "update_time": 1719073586,
                "client_id": "7f0000011324000005e4",
                "q_permition": 1,
                "tj_username": "",
                "ip": "203.160.80.7",
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
                "face": "default_woman\/300.jpg",
                "photo": "default_woman\/300.jpg"
            }
        }
    ]
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>



<a id="videoCategory"></a>
## 獲取短視頻分類列表

***Path***

```
POST /im/video.Share/category
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
	[{"id":4,"name":"life"},{"id":16,"name":"news"}]
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="videoUserinfo"></a>
## 獲取短視頻指定用戶信息

***Path***

```
POST /im/video.Share/user_info
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明     |
	| --- |---------|----|--------|
 	| _token | String  | Y  | TOKEN  |
	| _agent_id | String  | Y  | 租戶id   |
 	| user_id | Integer | Y  | 指定用戶id |


	***範例***

	```Form Data
	user_id: 32814
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "user_info": {
        "id": 32814,
        "username": "swee99999",
        "nickname": "123654",
        "doodling": "本宝宝暂时还没有想到个性的签名",
        "email": "",
        "phone": "swee99999",
        "sex": 0,
        "password": "1ac633444cb5eb9cf03ab1f911732480",
        "trade_password": "",
        "money": "0.00",
        "freeze_money": "0.00",
        "point": 0,
        "type": 1,
        "status": 0,
        "create_time": 1732087726,
        "circli_img": "",
        "is_customer_service": 0,
        "agent_id": 1,
        "update_time": 1732091770,
        "client_id": "7f00000113240000068b",
        "q_permition": 1,
        "tj_username": "",
        "ip": "103.120.122.253",
        "ip_cityname": "",
        "ip_status": 0,
        "phone_status": 0,
        "phone_type": 0,
        "is_robot": 0,
        "storge": 11376,
        "default_friend_id": 0,
        "channel": "",
        "last_login": null,
        "invite_list": null,
        "face": "user\/32814\/300.jpg",
        "photo": "user\/32814\/300.jpg"
    },
    "follow": 0,
    "fans": 0,
    "fabulous": 0
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="videoUservideo"></a>
## 獲取短視頻指定用戶作品列表

***Path***

```
POST /im/video.Share/user_video
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明     |
	| --- |---------|----|--------|
 	| _token | String  | Y  | TOKEN  |
	| _agent_id | String  | Y  | 租戶id   |
 	| user_id | Integer | Y  | 指定用戶id |


	***範例***

	```Form Data
	user_id: 32814
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "total": 4,
    "per_page": 15,
    "current_page": "1",
    "last_page": 1,
    "data": [
        {
            "id": 31,
            "user_id": 32814,
            "title": "1234",
            "video": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.mp4",
            "gif": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.jpeg",
            "fabulous": 0,
            "comment": 0,
            "createtime": 1732089354,
            "status": "1",
            "category_id": 4
        },
        {
            "id": 30,
            "user_id": 32814,
            "title": "1234",
            "video": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.mp4",
            "gif": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.jpeg",
            "fabulous": 0,
            "comment": 0,
            "createtime": 1732089353,
            "status": "1",
            "category_id": 4
        },
        {
            "id": 29,
            "user_id": 32814,
            "title": "1234",
            "video": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.mp4",
            "gif": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.jpeg",
            "fabulous": 0,
            "comment": 0,
            "createtime": 1732089349,
            "status": "1",
            "category_id": 4
        },
        {
            "id": 28,
            "user_id": 32814,
            "title": "1234",
            "video": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.mp4",
            "gif": "\/static\/video\/32814\/20241120\/3698ee78092aa88f27e89dbe4eb6ddd7.jpeg",
            "fabulous": 0,
            "comment": 0,
            "createtime": 1732089342,
            "status": "1",
            "category_id": 4
        }
    ]
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="videoFav"></a>
## 獲取短視頻指定用戶喜歡列表

***Path***

```
POST /im/video.Share/fabulous_log
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明    |
	| --- |---------|----|-------|
 	| _token | String  | Y  | TOKEN |
	| _agent_id | String  | Y  | 租戶id  |
 	| user_id | Integer | Y  | 指定用戶id |
  	| page | Integer | N  | 當前頁   |



	***範例***

	```Form Data
	user_id: 32814
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	page: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{"total":0,"per_page":15,"current_page":1,"last_page":0,"data":[]}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="videoCommonlog"></a>
## 獲取短視頻指定用戶評論列表

***Path***

```
POST /im/video.Share/common_log
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明    |
	| --- |---------|----|-------|
 	| _token | String  | Y  | TOKEN |
	| _agent_id | String  | Y  | 租戶id  |
 	| user_id | Integer | Y  | 指定用戶id |
  	| page | Integer | N  | 當前頁   |



	***範例***

	```Form Data
	user_id: 32814
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	page: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "total": 2,
    "per_page": 15,
    "current_page": "1",
    "last_page": 1,
    "data": [
        {
            "id": 34,
            "share_id": 26,
            "user_id": 32811,
            "comment_id": 0,
            "to_id": 0,
            "content": "667",
            "createtime": 1732092530,
            "gif": "\/static\/video\/30426\/20240623\/2fd53cac2c346e45fc3b9f72621fad10.jpeg"
        },
        {
            "id": 33,
            "share_id": 26,
            "user_id": 30426,
            "comment_id": 0,
            "to_id": 0,
            "content": "666",
            "createtime": 1719133289,
            "gif": "\/static\/video\/30426\/20240623\/2fd53cac2c346e45fc3b9f72621fad10.jpeg"
        }
    ]
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="videoCommonlog"></a>
## 獲取系統配置

***Path***

```
POST /im/App/config
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明    |
	| --- |---------|----|-------|
 	| _token | String  | Y  | TOKEN |
	| _agent_id | String  | Y  | 租戶id  |


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
    "msg": "",
    "data": {
        "user_default_friend": "32668|32740",
        "user_default_friend_changer": "0",
        "user_default_friend_random": "0",
        "user_default_friend_speak": "hello",
        "user_default_kefu_friend_speak": "hello",
        "user_create_group": "0",
        "user_withdraw_status": "1",
        "user_invite_status": "1",
        "system_invite_status": "0",
        "user_limit_tourist": "1",
        "disappear_after_read": "1",
        "disappear_delay_time": "3",
        "user_min_withdraw": "98",
        "user_max_withdraw": "10000",
        "user_day_withdraw_times": "3",
        "user_withdraw_fee": "0.03",
        "user_push_appid": "4GILmHOXwU7YOEyRws8nj2",
        "user_push_appKey": "dBjOm7uF739PflFfQDwKsA",
        "user_push_masterSecret": "BavYIGWTro8zOem6qyMKw1",
        "user_limit_ip": "999",
        "tourist_prefix": "siyu_",
        "pc_page_title": "IM",
        "admin_page_title": "管理后台",
        "key": "basic_config",
        "tab_id": "1"
    }
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

<a id="getArticleList"></a>
## 幫助中心文章列表

***Path***

```
POST /im/vendor/getArticleList
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明    |
	| --- |---------|----|-------|
 	| _token | String  | Y  | TOKEN |
	| _agent_id | String  | Y  | 租戶id  |


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
    "msg": "",
    "data": [
        {
            "id": 22,
            "article_name": "二二",
            "article_desc": "二3我",
            "content": "<p>厄尔而威尔<\/p>",
            "status": 1,
            "position": "帮助文档",
            "create_time": "2024-05-08 22:39:19",
            "update_time": "1970-01-01 08:00:00",
            "small_pic": "\/uploads\/2024-05-08\/20240508\/17151791571677.jpg",
            "sort": 0
        },
        {
            "id": 20,
            "article_name": "111",
            "article_desc": "111",
            "content": "",
            "status": 1,
            "position": "帮助文档",
            "create_time": "2020-09-26 01:34:32",
            "update_time": "1970-01-01 08:00:00",
            "small_pic": "\/uploads\/2023-04-03\/20230403\/16804940493525.jpg",
            "sort": 0
        },
        {
            "id": 19,
            "article_name": "222",
            "article_desc": "222",
            "content": "",
            "status": 1,
            "position": "帮助文档",
            "create_time": "2020-09-26 01:33:33",
            "update_time": "1970-01-01 08:00:00",
            "small_pic": "\/uploads\/2023-04-03\/20230403\/16804940709877.jpg",
            "sort": 0
        },
        {
            "id": 21,
            "article_name": "666",
            "article_desc": "666",
            "content": "<p>666999<\/p>",
            "status": 1,
            "position": "帮助文档",
            "create_time": "2022-07-10 22:11:31",
            "update_time": "1970-01-01 08:00:00",
            "small_pic": "\/uploads\/2023-04-03\/20230403\/16804941247728.jpg",
            "sort": 6
        }
    ]
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

<a id="getArticleDetail"></a>
## 幫助中心文章詳情

***Path***

```
POST /im/vendor/getArticleDetail
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明    |
	| --- |---------|----|-------|
 	| _token | String  | Y  | TOKEN |
	| _agent_id | String  | Y  | 租戶id  |
 	| article_id | Integer | Y  | 文章id  |



	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	article_id: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "err": 0,
    "msg": "",
    "data": {
        "id": 22,
        "article_name": "二二",
        "article_desc": "二3我",
        "content": "<p>厄尔而威尔<\/p>",
        "status": 1,
        "position": "帮助文档",
        "create_time": "2024-05-08 22:39:19",
        "update_time": "1970-01-01 08:00:00",
        "small_pic": "\/uploads\/2024-05-08\/20240508\/17151791571677.jpg",
        "sort": 0
    }
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

<a id="getUserStore"></a>
## 我的收藏

***Path***

```
POST /im/vendor/getUserStore
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明                       |
	| --- |---------|----|--------------------------|
 	| _token | String  | Y  | TOKEN                    |
	| _agent_id | String  | Y  | 租戶id                     |
 	| type | Integer | Y  | 收藏分類（0全部1視頻2語音3圖片4文字5文件） |



	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	type: 1
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "err": 0,
    "msg": "",
    "data": {
        "total": 0,
        "per_page": 10,
        "current_page": 1,
        "last_page": 0,
        "data": [],
        "info": {
            "user_storge_count": 0,
            "user_storge": "0B",
            "max_count": 20000,
            "max_storge": "30GB",
            "user_info": {
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
    }
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

<a id="getStoreStatics"></a>
## 我的收藏資源利用情況

***Path***

```
POST /im/vendor/getStoreStatics
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明                       |
	| --- |---------|----|--------------------------|
 	| _token | String  | Y  | TOKEN                    |
	| _agent_id | String  | Y  | 租戶id                     |


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
    "msg": "",
    "data": {
        "list": {
            "s1": "0B",
            "c1": 0,
            "s2": "0B",
            "c2": 0,
            "s3": "0B",
            "c3": 0,
            "s4": "0B",
            "c4": 0,
            "s11": "0B",
            "c11": 0
        },
        "info": {
            "user_storge_count": 0,
            "user_storge": "0B",
            "max_storge": 32212254720,
            "max_count": 20000,
            "rate_1": 0,
            "rate_2": 0,
            "splus_storge": "30GB",
            "splus_count": "20000"
        }
    }
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="kefu"></a>
## 客服

***Path***

```
POST /im/get/kefu
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱 | 資料類型    | 必填 | 說明                       |
	| --- |---------|----|--------------------------|
 	| _token | String  | Y  | TOKEN                    |
	| _agent_id | String  | Y  | 租戶id                     |


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
	{"code":1,"data":"120de41dad9e422bda064059ba82ffa5"}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="setListTime"></a>
## 設置聊天列表時間

***Path***

```
POST /im/message/setListTime
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱      | 資料類型    | 必填 | 說明     |
	|-----------|---------|----|--------|
 	| _token    | String  | Y  | TOKEN  |
	| _agent_id | String  | Y  | 租戶id   |
	| list_id   | String  | Y  | 聊天列表id |


	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	list_id: 120de41dad9e422bda064059ba82ffa5
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{"err":0,"msg":"success"}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="myfavor"></a>
## 獲取聊天收藏列表

***Path***

```
POST /im/user/myfavor
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱      | 資料類型    | 必填 | 說明     |
	|-----------|---------|----|--------|
 	| _token    | String  | Y  | TOKEN  |
	| _agent_id | String  | Y  | 租戶id   |

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
	[]
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a id="getMemberPhotos"></a>
## 獲取聊天成員頭像

***Path***

```
POST /im/vendor/getMemberPhotos
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱      | 資料類型    | 必填 | 說明     |
	|-----------|---------|----|--------|
 	| _token    | String  | Y  | TOKEN  |
	| _agent_id | String  | Y  | 租戶id   |
 	| list_id   | String  | Y  | 聊天列表id |


	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	list_id: 120de41dad9e422bda064059ba82ffa5
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "err": 0,
    "msg": "",
    "data": [
        {
            "user_id": 32752,
            "id": "67515d38b80e9f52726f81fa",
            "photo": "user\/32752\/300.jpg"
        },
        {
            "user_id": 32835,
            "id": "67515d38b80e9f52726f81fb",
            "photo": "user\/32835\/300.jpg"
        }
    ]
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

<a id="chatData"></a>
## 獲取聊天內容

***Path***

```
POST /im/get/chatData
```

<br>

***Request***

- ***Header***
	無

- ***Body (Form Data)***

	| 參數名稱      | 資料類型      | 必填 | 說明     |
	|-----------|-----------|----|--------|
 	| _token    | String    | Y  | TOKEN  |
	| _agent_id | String    | Y  | 租戶id   |
 	| list_id   | String    | Y  | 聊天列表id |
  	| time   | Timestamp | Y  | 時間戳    |
 	| is_up   | Boolean   | Y  | 是否置頂   |



	***範例***

	```Form Data
	_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozMjgzNSwiaXNzIjoiaW1faHR0cCIsImlhdCI6MTczMzM2NjM0NiwiZXhwIjo3NzMzMzY2MzQ2LCJuYmYiOjE3MzMzNjYzNDYsInN1YiI6IiIsImp0aSI6IjZkZjI4OWU0ZTNhYTAyYjJkOThkZDg2YjQ5MThmYWFlIn0.m2cGAOVTTFi4U5dn_IDOSS84O0yd5eWPdJTD2POjwXg
	_agent_id: 1
	list_id: 120de41dad9e422bda064059ba82ffa5
	time: 1733385639
	is_up: 0
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	***範例***
	```json
	{
    "err": 0,
    "data": {
        "stime": "2024-12-05 16:09:54",
        "etime": "2024-12-05 16:09:54",
        "ip": "223.88.95.223",
        "region": "",
        "list_id": "120de41dad9e422bda064059ba82ffa5",
        "type": 0,
        "show_name": "siyu_vUhHBf",
        "list": [],
        "is_msg": 0,
        "is_action": 1,
        "obj_id": 32752,
        "online": 0,
        "last_login": "1729919861",
        "receive_list": []
    }
	}
	```
- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>

