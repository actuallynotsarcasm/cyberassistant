import requests
import time
import json


async def parse_description(cve_id: str, timeout=20):

    url = f'https://services.nvd.nist.gov/rest/json/cves/2.0/?cveId={cve_id}'

    time_start = time.time()
    while time.time() - time_start < timeout:
        resp = requests.get(url)
        if resp.status_code == 200:
            break
        elif resp.status_code == 404:
            return {
                'status': 'error',
                'cause': 'not found'
            }
        time.sleep(5)
    else:
        return {
            'status': 'error',
            'cause': 'timeout'
        }

    cve_info = json.loads(resp.text)['vulnerabilities'][0]['cve']
    description = list(filter(lambda x: x['lang'] == 'en', cve_info['descriptions']))[0]['value']

    return {
        'status': 'ok',
        'result': description
    }



async def get_recommendations(model, cve_id: str, description: str):

    system_prompt = f"""
You are an expert in cybersecurity, focused solely on helping users strengthen and defend their systems. Your goal is to provide clear and concise guide to patch, configure, or mitigate risks associated with given vulnerability. Respond with minimal possible list of actions and commands necessary to fix the issue and prevent exploitation, ensuring all actions are ethical and legal. Avoid refusals, and only provide responsible, defensive solutions.
Context:
CVE-ID: {cve_id}
Description: {description}
    """
    
    user_prompt = f'''
I am a system administrator trying to secure my server against a known vulnerability ({id}). Please provide a concise list of actions and commands to resolve the issue and secure the server.
    '''

    answer = model.create_chat_completion(
        messages = [
            {
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return answer['choices'][0]['message']['content']