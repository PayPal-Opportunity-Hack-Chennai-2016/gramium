# coding=latin-1
from dbclients.MySqlClient import MySqlClient
from sms.TwilioClient import TwilioClient
import datetime


class VoiceAppRunner:

    def pre_due_call(self, due_day):
        client = TwilioClient()
        mysql_client = MySqlClient()
        mysql_db_conn = mysql_client.getDatabaseConnection()
        mysql_cursor  = mysql_db_conn.cursor()

        query = "SELECT core_member.phone, core_loan.due_date, core_loan.monthly_installment " \
                "FROM core_member join core_loan join core_group where core_member.group_id=core_loan.group_id " \
                "AND core_member.group_id=core_group.id AND core_loan.is_active=1  AND (send_sms_to_all_in_group | is_incharge) " \
                "AND DATE_FORMAT(core_loan.due_date,'%d')=" + due_day

        #date = #update date for installment payment
        mysql_cursor.execute(query)
        result = mysql_cursor.fetchall()
        print "Total Numbers selected: " + str(mysql_cursor.rowcount)
        for row in result:
            to = '+91' + str(row[0])
            due_date = str(row[1])
            due_year_diff = datetime.date.today().year - int(due_date.split("-")[0])
            due_month_diff = datetime.date.today().month - int(due_date.split("-")[1])
            amount = str(row[2] * (due_year_diff*12 + (due_month_diff + 1)))
            url= "http://twimlets.com/menu?Message=Message+From+GrawMeYum+Organization.+Pay+Your+Due+Amount+Rupees+"+amount+"+before+"+due_day+"+of+this+month."
            print "Making Call to: " + to + " with amount: " + amount
            client.makeCall(to=to, from_="(267) 433-0959", url=url)
        mysql_client.closeConnection()

        return

    def run(self):
        print "Running App"

        current_day = str( datetime.date.today().day)
        if current_day=="01" or current_day=="03":
            due_day = "05"
            self.pre_due_call(due_day)
        elif current_day=="11" or current_day=="13":
            due_day = "15"
            self.pre_due_call(due_day)
        else:
            due_day = "-1"
            self.pre_due_call(due_day)

if __name__ == "__main__":
    app = VoiceAppRunner()
    app.run()