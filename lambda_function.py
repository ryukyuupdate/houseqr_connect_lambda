from urllib import request, parse
import json



def lambda_handler(event, context):
    connect_type = event['Details']['Parameters']['connect_type']
    
    if connect_type == 'phone_number_certification':
        company_id = event['Details']['Parameters']['company_id']
        company_name = event['Details']['Parameters']['company_name']
        
        data = {
            'message': ('<speak><break time="0.5s"/>'+ company_name +'様<break time="0.5s"/>電話番号認証が完了いたしました<break time="0.5s"/></speak>')
        }
        phone_number_certification_status_ok(company_id=company_id)
        return data


# DB更新
def phone_number_certification_status_ok(company_id):
    url = "http://api.housewatcher.ryukyuupdate.com/api/company/phone_check"
    data = {
        'company_id': company_id,
        'check_status': 1
    }
    post_form_data = parse.urlencode(data)
    post_form_headers = {'content-type': 'application/x-www-form-urlencoded'}
    post_req = request.Request(url, data=post_form_data.encode(), method='POST')
    request.urlopen(post_req)