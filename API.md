### https://syapi.mm8888.shop/im/App/videoConfig
#### 趣味模塊-獲取視頻播放配置
| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
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

### https://syapi.mm8888.shop/im/App/config
#### 獲取系統配置
| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
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

### https://syapi.mm8888.shop/im/middle.Middle/get_list
#### 獲取底邊欄的動態菜單

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
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

#### Response
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

### https://syapi.mm8888.shop/im/get/getUserInfo
#### 獲取用戶信息

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/get/chatList
#### 獲取群聊列表

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
{
    "err": 0,
    "msg": "",
    "data": [
        {
            "list_id": "61EDFF1C7B59A059B11EF43D7F5E4FF9",
            "last_chat_time": 1733191469,
            "chat_id": "674e672d56cac813e159f38b",
            "no_reader_num": 1,
            "show_name": "guitu、siyu_inaZsL、",
            "last_msg": "guitu,siyu_inaZsL, 加入群聊",
            "photo_path": "\/group_photo\/61EDFF1C7B59A059B11EF43D7F5E4FF9\/90.jpg",
            "time": 1733191469,
            "top": 0,
            "top_time": 0,
            "type": 1,
            "is_disturb": 0
        }
    ]
}



### https://syapi.mm8888.shop/im/get/friendList
#### 通訊錄-好友列表

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |
#### Response
{
    "err": 0,
    "data": {
        "data": {
            "6": {
                "letter": "G",
                "data": [
                    {
                        "photo": "user\/32740\/300.jpg",
                        "user_id": 32740,
                        "name": "guitu",
                        "list_id": "66523003D1311EB53B6958E5AFDD5767"
                    }
                ],
                "index": 6
            },
            "18": {
                "letter": "S",
                "data": [
                    {
                        "photo": "user\/32752\/300.jpg",
                        "user_id": 32752,
                        "name": "siyu_vUhHBf",
                        "list_id": "D0A5CB4631A692B9D26935BF4E995A1D"
                    }
                ],
                "index": 18
            },
            "24": {
                "letter": "Y",
                "data": [
                    {
                        "photo": "user\/32668\/300.jpg",
                        "user_id": 32668,
                        "name": "123456",
                        "list_id": "C928538D7CE3D635EDBFADB09718EDE5"
                    }
                ],
                "index": 24
            }
        },
        "member": []
    }
}

#### Response
{
    "err": 0,
    "data": {
        "data": {
            "6": {
                "letter": "G",
                "data": [
                    {
                        "photo": "user\/32740\/300.jpg",
                        "user_id": 32740,
                        "name": "guitu",
                        "list_id": "66523003D1311EB53B6958E5AFDD5767"
                    }
                ],
                "index": 6
            },
            "18": {
                "letter": "S",
                "data": [
                    {
                        "photo": "user\/32752\/300.jpg",
                        "user_id": 32752,
                        "name": "siyu_vUhHBf",
                        "list_id": "D0A5CB4631A692B9D26935BF4E995A1D"
                    }
                ],
                "index": 18
            },
            "24": {
                "letter": "Y",
                "data": [
                    {
                        "photo": "user\/32668\/300.jpg",
                        "user_id": 32668,
                        "name": "123456",
                        "list_id": "C928538D7CE3D635EDBFADB09718EDE5"
                    }
                ],
                "index": 24
            }
        },
        "member": []
    }
}

### https://syapi.mm8888.shop/im/agent/getOnlineList
#### 探索界面-獲取在線列表

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
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

### https://syapi.mm8888.shop/im/get/getUserbankList
#### 提現-銀行卡列表

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
{"err":0,"msg":"银行卡列表","data":[]}

### https://syapi.mm8888.shop/im/withdraw/getWithDrawConfig
#### 提現-獲取提現配置

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |
#### Response
{
    "err": 0,
    "msg": "config",
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

### https://syapi.mm8888.shop/im/vendor/getUserCapitalList

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/get/getUserCapitalList

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |


### https://syapi.mm8888.shop/im/vendor/getAboutList

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/vendor/getUserStore
#### 我的收藏

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
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
                "id": 32830,
                "username": "siyu_inaZsL",
                "nickname": "siyu_inaZsL",
                "doodling": "本宝宝暂时还没有想到个性的签名",
                "email": "",
                "phone": "",
                "sex": 0,
                "password": "e10adc3949ba59abbe56e057f20f883e",
                "trade_password": "",
                "money": "0.00",
                "freeze_money": "0.00",
                "point": 0,
                "type": 1,
                "status": 0,
                "create_time": 1733190945,
                "circli_img": "",
                "is_customer_service": 0,
                "agent_id": 0,
                "update_time": 1733190945,
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
                "face": "user\/32830\/300.jpg",
                "photo": "user\/32830\/300.jpg"
            }
        }
    }
}

### https://syapi.mm8888.shop/im/video.Share/category

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/video.Share/video_lists
#### 探索界面-短視頻列表

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
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


### https://syapi.mm8888.shop/im/get/applyFriend
#### 添加好友

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/get/applyGroup
#### 添加群

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/get/details
#### 獲取用戶詳情

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
{
    "err": 0,
    "msg": "success",
    "data": {
        "user_id": 32740,
        "nickname": "guitu",
        "username": "guitu_",
        "is_friend": 1,
        "doodling": "本宝宝暂时还没有想到个性的签名",
        "photo": "user\/32740\/300.jpg",
        "show_friend": {
            "circle": [],
            "phone": "guitu_"
        },
        "from": "系统默认添加",
        "content": "",
        "sex": 1,
        "apply_id": 0
    }
}

### https://syapi.mm8888.shop/im/message/getListId
#### 獲取消息列表的ID

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/message/getListTime
#### 獲取消息列表的時間

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/get/chatData
#### 聊天內容

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |
#### Response
{
    "err": 0,
    "data": {
        "stime": "2024-12-03 10:59:54",
        "etime": "2024-12-03 10:59:54",
        "ip": null,
        "region": "",
        "list_id": "61EDFF1C7B59A059B11EF43D7F5E4FF9",
        "type": 1,
        "show_name": "guitu、siyu_inaZsL、(2)",
        "list": [],
        "is_msg": 0,
        "is_action": 1,
        "obj_id": 0,
        "online": 0,
        "last_login": 0,
        "receive_list": []
    }
}

### https://syapi.mm8888.shop/im/vendor/getMemberPhotos
#### 獲取用戶頭像

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |
#### Response
{
    "err": 0,
    "msg": "",
    "data": [
        {
            "user_id": 32740,
            "id": "674e672d56cac813e159f386",
            "photo": "user\/32740\/300.jpg"
        },
        {
            "user_id": 32830,
            "id": "674e672d56cac813e159f388",
            "photo": "user\/32830\/300.jpg"
        }
    ]
}

### https://syapi.mm8888.shop/im/message/setListTime

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/vendor/getMemberList
#### 通訊錄

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
{
    "err": 0,
    "msg": "",
    "data": {
        "data": {
            "24": {
                "letter": "Y",
                "data": [
                    {
                        "photo": "user\/32668\/300.jpg",
                        "user_id": 32668,
                        "name": "123456"
                    }
                ],
                "index": 24
            }
        },
        "member": []
    }
}

### https://syapi.mm8888.shop/im/get/base
#### 獲取個人信息

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
{
    "err": 0,
    "msg": "success",
    "data": {
        "user_info": {
            "id": 32830,
            "nickname": "siyu_inaZsL",
            "username": "siyu_inaZsL",
            "photo": "user\/32830\/300.jpg",
            "doodling": "本宝宝暂时还没有想到个性的签名",
            "sex": 0,
            "circle_img": "default_circle_img.jpg",
            "money": "0.00",
            "trade_password": ""
        },
        "new_group_tips_num": 0,
        "new_friend_tips_num": 0,
        "no_reader_chat_num": 2,
        "no_reader_circle": 0,
        "no_reader_circle_chat_num": 0,
        "kefu_list_id": "",
        "bottom_url": "",
        "pc_page_title": "IM",
        "disappear_after_read": "1",
        "disappear_delay_time": "3"
    }
}

### https://syapi.mm8888.shop/im/user/myfavor

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/message/addGroup

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |


### https://syapi.mm8888.shop/im/message/updataNoReader

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/message/getListTime
#### 獲取消息的時間

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
{"read_time":0,"online":0,"err":0,"msg":"success"}

### https://syapi.mm8888.shop/im/get/chatData

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/vendor/getMemberPhotos

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

### https://syapi.mm8888.shop/im/message/setListTime
#### 設置列表時間

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |


### https://syapi.mm8888.shop/im/user/
#### 我的收藏

| Key | Value |
| --- | ----- |
| 主機 | syapi.mm8888.shop |
| 接受 | */* |
| 用戶代理 | Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 |
| 內容類型 | application/x-www-form-urlencoded |
| 安全取取目的地 | empty |
| 安全取取模式 | cors |
| 安全取取站點 | cross-site |

#### Response
[]

