def send_message(message):
	from twilio.rest import TwilioRestClient
	account = "ACfd03a9b8c45fb66bab8b834a21ec578c"
	token = "aff6d0726a21c044cc3797d9037e9b15"
	client = TwilioRestClient(account, token)

	message = client.messages.create(to="+917299139948", from_="(347) 380-7554",
	                             body="Hello there!yjgjyl jl klu")
	
	message = client.messages.create(to="+918526520700", from_="(347) 380-7554",
	                             body="Hello there! this is soundarya here")
	print(message.sid)

def xls_to_csv():
	wb = xlrd.open_workbook("/Users/soundaryat/Desktop/Icici 15th repayment.xlsx","r")
	sh = wb.sheet_by_index(0)

	fh = open("/Users/soundaryat/Desktop/new.csv","wb")
	csv_out = unicodecsv.writer(fh, encoding='utf-8')

	for row_number in xrange (sh.nrows):
	    csv_out.writerow(sh.row_values(row_number))

	fh.close()