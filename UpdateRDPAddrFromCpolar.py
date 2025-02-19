import re

def get_cpolar_url():
   import requests

   login_url = "https://dashboard.cpolar.com/login"
   status_url = "https://dashboard.cpolar.com/status"


   # 创建一个 session 对象
   session = requests.Session()

   r = session.get(login_url)

   # 从登录页面中提取 csrf_token
   reg = r'<input type="hidden" name="csrf_token" value="(.*)" />'
   pattern = re.compile(reg)
   result = pattern.findall(r.content.decode('utf-8'))
   token = result[0]

   # 登录的 URL 和数据

   login_data = {
   'login': 'your_username',
   'password': 'your_password',
   'csrf_token':token
   }

   # 发送 POST 请求进行登录
   session.post(login_url, data=login_data)

   r = session.get(status_url)

   # 从状态页面中提取 csrf_token
   reg = r'<th scope="row"><a href="#ZgotmplZ" target="_blank">(.*)</a></th>'
   pattern = re.compile(reg)
   result = pattern.findall(r.content.decode('utf-8'))
   url = result[0] 
   return url
def get_cpolar_url_fake():
   return 'tcp://example.tcp.cpolar.top:11204'



if __name__ == '__main__':
   url = get_cpolar_url_fake()
   print(f'get URL:{url}')

   url = re.sub('tcp://', '', url)

   file_path = 'your_rdp_file_path/your_rdp_file.rdp'

   with open(file_path, 'r', encoding='utf-16-le') as file:
      content = file.read()

   pattern = r'full address:s:.*'  # 匹配 'full address:s:' 后的任意字符
   replacement = f'full address:s:{url}'
   content = re.sub(pattern, replacement, content)
   with open(file_path, 'w', encoding='utf-16-le') as file:
      file.write(content)

   print(f"New address {url} has been updated.")  


