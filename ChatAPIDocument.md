# Manage API Document

## 目錄

- [註冊](#signUp)
- [登入](#signIn)

**使用者**

- [查詢使用者資訊](#queryUser)
- [變更使用者密碼](#editUser)

**應用程式**

- [建立應用程式](#createProject)
- [查詢應用程式列表](#queryProject)
- [查詢應用程式詳情](#queryProjectByID)
- [重置MasterSecret](#editProject)
- [刪除應用程式](#deleteProject)

**各平台推播憑證設定**

***iOS***

- [查詢iOS平台設定(p12)](#queryPlatformIOSp12)
- [查詢iOS平台設定(p8)](#queryPlatformIOSp8)
- [更新平台設定值iOS(p12)](#editPlatformIOSp12)
- [更新平台設定值iOS(p8)](#editPlatformIOSp8)

***Web***

- [查詢Web平台設定值](#queryPlatformWeb)
- [更新平台設定值Web](#editPlatformWeb)

**發送推播通知紀錄**

- [查詢發送推播通知紀錄](#querySendRecord)
- [查詢發送推播通知紀錄詳細資訊](#querySendDetailRecord)
- [查詢已註冊裝置清單](#queryDevices)

<br>

<a name="signUp"></a>
## 趣味模塊-獲取視頻播放配置

***Path***

```
POST /im/App/videoConfig
```

<br>

***Request***

- ***Body (JSON)***
	
	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| account | String | Y | 帳號 (email 格式) |
	| password | String | Y | 密碼 (大小寫英文數字組合，最少8碼。至少1大寫英文，1小寫英文，1數字) |

- ***範例***

	```json
	{
		"account": "user01@baifu-tech.net",
		"password": "Password01"
	}
	```
	
<br>

***Response***
    
- ***Body***

    無

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 201 | 註冊成功 |
    
<br>




<a name="signIn"></a>
## 登入

***Path***

```
GET /api/v1/manage/signIn
```

<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | Basic Auth 認證機制<br>帳號 (email 格式)<br>密碼 (大小寫英文數字組合，最少8碼。至少1大寫英文，1小寫英文，1數字) |
	
<br>

***Response***
    
- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| auth | String | Y | JWT認證Token，後續呼叫其他API需要使用 |

	***範例***

	```json
	{
		"auth": "JWTAuthToken"
	}
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 登入成功 |

<br>


<a name="queryUser"></a>
## 查詢使用者資訊

***Path***

```
GET /api/v1/manage/user
```

<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	
<br>

***Response***
    
- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 使用者唯一識別碼 |
	| account | String | Y | 帳號 |
	| updateDate | Timestamp(秒) | Y | 最後更新時間 |
	| createDate | Timestamp(秒) | Y | 建立時間 |

	***範例***

	```json
	{
		"id": "XXXXXX-XXXXXX-XXXXXXX-XXXXXX",
		"account": "mail@mail.com",
		"updateDate": 1234567890,
		"createDate": 1234567890
	}
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a name="editUser"></a>
## 變更使用者密碼

***Path***

```
PATCH /api/v1/manage/user
```

<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	
<br>

- ***Body (JSON)***
	
	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| password | String | Y | 密碼 (大小寫英文數字組合，最少8碼。至少1大寫英文，1小寫英文，1數字) |

- ***範例***

	```json
	{
		"password": "NewPassword"
	}
	```

<br>

***Response***
    
- ***Body (JSON)***

	無

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 修改成功 |

<br>


<a name="createProject"></a>
## 建立應用程式

建立應用程式，應用程式底下會再區分雙平台，並有各自的設定。

建立 Project 時，要產生 AppKey 跟 MasterSecret 

建立 Project 時，要順便把 Platform ios 跟 android 的資料一起建立

***Path***

```
POST /api/v1/manage/project
```

<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	
<br>

- ***Body (JSON)***
	
	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| name | String | Y | 應用程式名稱 |

- ***範例***

	```json
	{
		"name": "application01"
	}
	```
	
<br>

***Response***
    
- ***Body (JSON)***

	無

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 201 | 建立成功 |

<br>


<a name="queryProject"></a>
## 查詢應用程式列表

查詢此用戶的應用程式列表 (僅限此用戶建立的應用程式)

***Path***

```
GET /api/v1/manage/project
```

<br>

***Request***

 - ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	
<br>

***Response***
    
- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 應用程式唯一識別碼 |
	| name | String | Y | 應用程式名稱 |
	| appKey | String | Y | 給 SDK 用的 App Key |
	| masterSecret | String | Y | 給 Integrate 用的 Secret |
	| updateDate | Timestamp(秒) | Y | 最後更新時間 |
	| createDate | Timestamp(秒) | Y | 建立時間 |
	
- ***範例 (多筆資料)***
	
	```json
	[
		{
			"id": "proejctID",
			"name": "application01",
			"appKey": "給 SDK 用的 App Key",
			"masterSecret": "給 Integrate 用的 Secret",
			"updateDate": 1234567890,
			"createDate": 1234567890
		},
		{
			"id": "proejctID",
			"name": "application02",
			"appKey": "給 SDK 用的 App Key",
			"masterSecret": "給 Integrate 用的 Secret",
			"updateDate": 1234567890,
			"createDate": 1234567890
		}
	]
	```

- ***範例 (1筆資料)***
	
	```json
	[
		{
			"id": "proejctID",
			"name": "application01",
			"appKey": "給 SDK 用的 App Key",
			"masterSecret": "給 Integrate 用的 Secret",
			"updateDate": 1234567890,
			"createDate": 1234567890
		}
	]
	```
	
- ***範例 (無資料)***
	
	```json
	[]
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a name="queryProjectByID"></a>
## 查詢應用程式詳情

查詢應用程式詳情 (僅限此用戶建立的應用程式)

***Path***

```
GET /api/v1/manage/project/{projectID}
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
	| projectID | String | N | 應用程式唯一識別碼。沒給的話就回傳此用戶所有的應用程式 |

<br>

***Response***

- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 應用程式唯一識別碼 |
	| name | String | Y | 應用程式名稱 |
	| appKey | String | Y | 給 SDK 用的 App Key |
	| masterSecret | String | Y | 給 Integrate 用的 Secret |
	| updateDate | Timestamp(秒) | Y | 最後更新時間 |
	| createDate | Timestamp(秒) | Y | 建立時間 |

- ***範例***

	```json
	{
		"id": "proejctID",
		"name": "application01",
		"appKey": "給 SDK 用的 App Key",
		"masterSecret": "給 Integrate 用的 Secret",
		"updateDate": 1234567890,
		"createDate": 1234567890
	}
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a name="editProject"></a>
## 重置MasterSecret

重置應用程式的 MasterSecret (僅限此用戶建立的應用程式)

***Path***

```
PATCH /api/v1/manage/project/{projectID}
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
	| projectID | String | Y | 應用程式唯一識別碼 |

<br>

***Response***

- ***Body***
	
	無
	
- ***Status Code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 202 | 重置成功 |

<br>


<a name="deleteProject"></a>
## 刪除應用程式

刪除指定的應用程式 (僅限此用戶建立的應用程式)

***Path***

```
DELETE /api/v1/manage/project/{projectID}
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
	| projectID | String | Y | 應用程式唯一識別碼 |

<br>

***Response***
    
- ***Body (JSON)***

	無

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 刪除成功 |

<br>


<a name="queryPlatformIOSp12"></a>
## 查詢iOS平台設定(p12)

***Path***

```
GET /api/v1/manage/platform/{projectID}/{platform}/p12
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
	| projectID | String | Y | 應用程式唯一識別碼 |
	| platform | String | Y | 固定用 ios |

<br>

***Response***

- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 唯一識別碼 |
	| platform | String | Y | 平台 |
	| bundleID | String | Y | App 唯一識別碼 |
	| p12Sandbox | Bool | Y | 是否已上傳開發環境p12憑證 |
	| p12SandboxPassword | String | N | (可能為空)<br>開發環境p12憑證密碼 |
	| p12Product | Bool | Y | 是否已上傳正式環境p12憑證 |
	| p12ProductPassword | String | N | (可能為空)<br>正式環境p12憑證密碼 |
	| updateDate | Timestamp(秒) | Y | 最後更新時間 |
	| createDate | Timestamp(秒) | Y | 建立時間 |

- ***範例***

	```json
	{
		"id":"XXXX-XXXX-XXXX-XXXX",
		"platform": "ios",
		"bundleID": "com.xxx.xxx",
		"p12Sandbox": true,
		"p12SandboxPassword": "123",
		"p12Product": true,
		"p12ProductPassword": "123",
		"updateDate": 1234567890,
		"createDate": 1234567890
	}
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a name="queryPlatformIOSp8"></a>
## 查詢iOS平台設定(p8)

***Path***

```
GET /api/v1/manage/platform/{projectID}/{platform}/p8
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
	| projectID | String | Y | 應用程式唯一識別碼 |
	| platform | String | Y | 固定用 ios |

<br>

***Response***

- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 唯一識別碼 |
	| platform | String | Y | 平台 |
	| p8 | Bool | Y | 是否已上傳p8憑證 |
	| bundleID | String | Y | App 唯一識別碼 |
	| keyID | String | Y | 憑證的 ID |
	| teamID | String | Y | Apple開發者帳號的 Team ID |
	| updateDate | Timestamp(秒) | Y | 最後更新時間 |
	| createDate | Timestamp(秒) | Y | 建立時間 |

- ***範例***

	```json
	{
		"id":"XXXX-XXXX-XXXX-XXXX",
		"platform": "ios",
		"p8": true,
		"bundleID": "com.baifu.demo.app",
		"keyID": "11AA5478BB",
		"teamID": "A123V5V789",
		"updateDate": 1234567890,
		"createDate": 1234567890
	}
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a name="editPlatformIOSp12"></a>
## 更新平台設定值iOS(p12)

更換iOS平台的推播憑證

- p12 => 上傳兩張 p12 憑證

***Path***

```
PATCH /api/v1/manage/platform/{projectID}/{platform}/p12
```
<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	| Content-Type | String | Y | 若有上傳 p12 p8 檔案，Content-Type=multipart/form-data |
	
<br>

- ***Path Parameters***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| projectID | String | Y | 應用程式唯一識別碼 |
	| platform | String | Y | 固定用 ios |

<br>

- ***Body (form-data)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| bundleID | String | Y | App 唯一識別碼 |
	| p12Sandbox | Data | Y | ios開發推播憑證 |
	| p12SandboxPassword | String | Y | ios開發推播憑證密碼 |
	| p12Product | Data | Y | ios正式推播憑證 |
	| p12ProductPassword | String | Y | ios正式推播憑證密碼 |

<br>

***Response***

- ***Body (JSON)***

	無

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 設定成功 |

<br>


<a name="editPlatformIOSp8"></a>
## 更新平台設定值iOS(p8)

更換iOS平台的推播憑證

- p8 => 上傳一張 p8 憑證及，bundleID, keyId, teamID

***Path***

```
PATCH /api/v1/manage/platform/{projectID}/{platform}/p8
```
<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	| Content-Type | String | Y | 若有上傳 p12 p8 檔案，Content-Type=multipart/form-data |
	
<br>

- ***Path Parameters***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| projectID | String | Y | 應用程式唯一識別碼 |
	| platform | String | Y | 固定用 ios |

<br>

- ***Body (form-data)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| p8 | Data | Y | ios專用<br>通用憑證<br>需搭配bundleID, keyID, teamID 使用 |
	| bundleID | String | Y | ios專用<br>應用程式唯一識別碼 |
	| keyID | String | Y | ios專用<br>p8憑證唯一識別碼 |
	| teamID | String | Y | ios專用<br>App帳號識別碼 |

<br>

***Response***

- ***Body (JSON)***

	無

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 設定成功 |

<br>


<a name="queryPlatformAndroid"></a>
## 查詢Android平台設定值

***Path***

```
GET /api/v1/manage/platform/{projectID}/{platform}
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
	| projectID | String | Y | 應用程式唯一識別碼 |
	| platform | String | Y | 固定用 android |

<br>

***Response***

- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 唯一識別碼 |
	| platform | String | Y | 平台 |
	| json | Bool | Y | 是否已上傳json檔案 |
	| packageName | String | Y | App 唯一識別碼 |
	| updateDate | Timestamp(秒) | Y | 最後更新時間 |
	| createDate | Timestamp(秒) | Y | 建立時間 |

- ***範例***

	```json
	{
		"id":"XXXX-XXXX-XXXX-XXXX",
		"platform": "ios",
		"json": true,
		"packageName": "com.baifu.demo.app",
		"updateDate": 1234567890,
		"createDate": 1234567890
	}
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a name="editPlatformAndroid"></a>
## 更新平台設定值Android

更換Android平台的推播憑證

***Path***

```
PATCH /api/v1/manage/platform/{projectID}/{platform}
```
<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	| Content-Type | String | Y | 若有上傳 json 檔案，Content-Type=multipart/form-data |
	
<br>

- ***Path Parameters***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| projectID | String | Y | 應用程式唯一識別碼 |
	| platform | String | Y | 固定用 android |

<br>

- ***Body (form-data)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| json | Data | Y | Android專用<br>推播JSON檔案 |
	| packageName | String | Y | App 唯一識別碼 |

<br>

***Response***

- ***Body (JSON)***

	無

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 設定成功 |

<br>


<a name="queryPlatformWeb"></a>
## 查詢Web平台設定值

***Path***

```
GET /api/v1/manage/platform/{projectID}/{platform}
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
	| projectID | String | Y | 應用程式唯一識別碼 |
	| platform | String | Y | 固定用 web |

<br>

***Response***

- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 唯一識別碼 |
	| platform | String | Y | 平台 |
	| packageName | String | Y | App 唯一識別碼 |
	| json | Bool | Y | 是否已上傳json檔案 |
	| updateDate | Timestamp(秒) | Y | 最後更新時間 |
	| createDate | Timestamp(秒) | Y | 建立時間 |

- ***範例***

	```json
	{
		"id":"XXXX-XXXX-XXXX-XXXX",
		"platform": "web",
		"packageName": "com.baifu.demo.app",
		"json": true,
		"updateDate": 1234567890,
		"createDate": 1234567890
	}
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a name="editPlatformWeb"></a>
## 更新平台設定值Web

更換Web平台的推播憑證

***Path***

```
PATCH /api/v1/manage/platform/{projectID}/{platform}
```
<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	| Content-Type | String | Y | 若有上傳 json 檔案，Content-Type=multipart/form-data |
	
<br>

- ***Path Parameters***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| projectID | String | Y | 應用程式唯一識別碼 |
	| platform | String | Y | 固定用 web |

<br>

- ***Body (form-data)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| json | Data | Y | Web專用<br>推播JSON檔案 |
	| packageName | String | Y | App 唯一識別碼 |

<br>

***Response***

- ***Body (JSON)***

	無

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 設定成功 |

<br>


<a name="querySendRecord"></a>
## 查詢發送推播通知紀錄

查詢當前用戶所有的發送推播通知紀錄

***Path***

```
GET /api/v1/manage/sendRecord
```
<br>

***Request***

- ***Header***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| Authorization | String | Y | JWT認證機制，登入回傳的 auth, 前面加上 Bearer |
	
<br>

- ***Query Parameters***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| projectID | String | N | 應用程式唯一識別碼<br>查詢指定的Project的紀錄 |
	| platform | String | N | 平台 ios or android or web<br>查詢指定的Platform的紀錄 |
	| title | String | N | 推播通知標題(模糊搜尋) |
	| message | String | N | 推播通知訊息內容(模糊搜尋) |
	| limit | Int | N | 資料筆數 (1-300)，預設100 |
	| startDate | Timestamp(秒) | N | 起始時間 |
	| endDate | Timestamp(秒) | N | 結束時間 |

<br>

***Response***

- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 唯一識別碼 |
	| projectID | String | Y | 專案唯一識別碼 |
	| masterSecret | String | Y | 專案的masterSecret |
	| platform | String | Y | 平台 |
	| title | String | Y | 推播通知標題 |
	| message | String | Y | 推播通知訊息內容 |
	| createDate | Timestamp(秒) | Y | 建立時間 |

- ***範例***

	```json
	[
		{
			"id":"XXXX-XXXX-XXXX-XXXX",
			"projectID":"XXXX-XXXX-XXXX-XXXX",
			"masterSecret":"f97de827fbec19ddc21740c8af54edad",
			"platform": "ios",
			"title": "推播通知標題",
			"message": "推播通知訊息內容",
			"createDate": 1234567890
		},
		{
			"id":"XXXX-XXXX-XXXX-XXXX",
			"projectID":"XXXX-XXXX-XXXX-XXXX",
			"masterSecret":"f97de827fbec19ddc21740c8af54edad",
			"platform": "ios",
			"title": "推播通知標題",
			"message": "推播通知訊息內容",
			"createDate": 1234567890
		}
	]
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a name="querySendDetailRecord"></a>
## 查詢發送推播通知紀錄詳細資訊

查詢指定的推播通知紀錄詳情

***Path***

```
GET /api/v1/manage/sendRecord/{sendRecordID}
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
	| sendRecordID | String | Y | 推播通知紀錄唯一識別碼 |

<br>

***Response***

- ***Body (JSON)***

	| 參數名稱 | 資料類型 | 必填 | 說明 |
	| --- | --- | --- | --- |
	| id | String | Y | 唯一識別碼 |
	| sendRecordID | String | Y | 推播通知紀錄唯一識別碼 |
	| token | String | Y | 推播裝置的唯一識別碼 |
	| status | Bool | Y | 發送推播通知的結果<br> true => 成功<br>false => 失敗 |
	| result | String | Y | 發送推播通知結果的錯誤訊息 |
	| createDate | Timestamp(秒) | Y | 建立時間 |

- ***範例***

	```json
	[
		{
			"id":"XXXX-XXXX-XXXX-XXXX",
			"sendRecordID":"XXXX-XXXX-XXXX-XXXX",
			"token":"f97de827fbec19ddc21740c8af54edad",
			"status": true,
			"result": "發送成功的資訊",
			"createDate": 1234567890
		},
		{
			"id":"XXXX-XXXX-XXXX-XXXX",
			"sendRecordID":"XXXX-XXXX-XXXX-XXXX",
			"token":"f97de827fbec19ddc21740c8af54edad",
			"status": false,
			"result": "發送錯誤的資訊",
			"createDate": 1234567890
		},
		{
			"id":"XXXX-XXXX-XXXX-XXXX",
			"sendRecordID":"XXXX-XXXX-XXXX-XXXX",
			"token":"f97de827fbec19ddc21740c8af54edad",
			"status": true,
			"result": "XXXXXXXX",
			"createDate": 1234567890
		}
	]
	```

- ***Status code***

    | 錯誤代碼 | 說明 |
    | --- | --- |
    | 200 | 查詢成功 |

<br>


<a name="queryDevices"></a>
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

