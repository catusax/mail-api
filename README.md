# email APi
使用http请求快速发送email

## 接口
`POST` `GET`:
localhost://send/<token>

### 参数
使用`http post`发送`json`或使用`http get`的`Query string`

| 参数  | 类型                 | 说明                     | 是否必需     |
| ------- | ---------------------- | -------------------------- | ---------------- |
| reciver | Array[String] | String | 邮件接收人，一个数组或列表 | 是              |
| cc      | Array[String] | String | 邮件抄送人，一个数组或列表 | 否              |
| bcc     | Array[String] | String | 邮件密送人，一个数组或列表 | 否              |
| subject | String                 | 邮件主题               | 否              |
| text    | String                 | 纯文本邮件内容      | 如果无主题则必需 |
| html    | String                 | html邮件内容           | 如果无主题则必需 |