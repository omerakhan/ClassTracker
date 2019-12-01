import requests
from bs4 import BeautifulSoup

def check_availability():
URL = 'https://saprod.emory.edu/psc/saprod_7/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?Page=PT_AGSTARTPAGE_NUI&Action=U&ACAD_CAREER=&CLASS_NBR=0&CRSE_ID=&CRSE_OFFER_NBR=0&INSTITUTION=EMORY&STRM=5201&CONTEXTIDPARAMS=TEMPLATE_ID:SR_ENRL_FL&CONTEXTIDPARAMS=OPRID:HIDDEN&replaceCurrentTopWindow=Y&fmode=1'

headers = {
	
	"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content,'html.parser')

title = soup.find(id = "win7divSEATS$0")

availability = soup.find(id = "seats").get_Text()

converted_availability = float(availability[0:5])

if(availability>0)
	send_mail()


def send_mail():
	server = smtplib.SMIP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('Hidden','Hidden')
	subject = 'Class is Open!'
	body = 'Check OPUS https://saprod.emory.edu/psc/saprod_7/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?Page=PT_AGSTARTPAGE_NUI&Action=U&ACAD_CAREER=&CLASS_NBR=0&CRSE_ID=&CRSE_OFFER_NBR=0&INSTITUTION=EMORY&STRM=5201&CONTEXTIDPARAMS=TEMPLATE_ID:SR_ENRL_FL&CONTEXTIDPARAMS=OPRID:OKHAN6&replaceCurrentTopWindow=Y&fmode=1'

	msg = f"Subject: {subject}\n\n{body}"

	server.send_mail{
	'HIDDEN'
	'HIDDEN'
	 msg
	}
	server.quit()
