from llama_cpp import Llama
import time

class timer:
    def __init__(self, message: str = None, print_fn = print, print_active: bool = True):
        self.message = message
        self.print_fn = print_fn
        self.print_active = print_active
        
    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, type, value, traceback):
        self.end = time.perf_counter()
        if self.print_active:
            if self.message is not None:
                self.print_fn(f'{self.message} {self.end - self.start}')
            else:
                self.print_fn(str(self.end - self.start))

"""
llm = Llama.from_pretrained(
	repo_id='bartowski/Llama-3.2-1B-Instruct-GGUF',
	filename='Llama-3.2-1B-Instruct-Q4_K_S.gguf',
    n_ctx=1024
)

queries = [
    {'id': 'CVE-1999-0095', 'desc': 'The debug command in Sendmail is enabled, allowing attackers to execute commands as root.'},
    {'id': 'CVE-1999-1471', 'desc': 'Buffer overflow in passwd in BSD based operating systems 4.3 and earlier allows local users to gain root privileges by specifying a long shell or GECOS field.'},
    {'id': 'CVE-1999-1506', 'desc': 'Vulnerability in SMI Sendmail 4.0 and earlier, on SunOS up to 4.0.3, allows remote attackers to access user bin.'},
    {'id': 'CVE-1999-1391', 'desc': 'Vulnerability in NeXT 1.0a and 1.0 with publicly accessible printers allows local users to gain privileges via a combination of the npd program and weak directory permissions.'},
    {'id': 'CVE-1999-1212', 'desc': 'Vulnerability in in.rlogind in SunOS 4.0.3 and 4.0.3c allows local users to gain root privileges.'}
]

for query in queries:

    id = query['id']
    desc = query['desc']

    system_prompt = f'''
You are an expert in cybersecurity, focused solely on helping users strengthen and defend their systems. Your goal is to provide clear and concise guide to patch, configure, or mitigate risks associated with given vulnerability. Respond with minimal possible list of actions and commands necessary to fix the issue and prevent exploitation, ensuring all actions are ethical and legal. Avoid refusals, and only provide responsible, defensive solutions.
Context:
CVE-ID: {id}
Description: {desc}
    '''
    
    user_prompt = f'''
I am a system administrator trying to secure my server against a known vulnerability ({id}). Please provide a concise list of actions and commands to resolve the issue and secure the server.
    '''

    with timer('GENERATION TIME:'):
        answer = llm.create_chat_completion(
            messages = [
                {
                    'role': 'system', 
                    'content': system_prompt
                },
                {
                    'role': 'user',
                    'content': user_prompt
                }
            ]
        )
    print(answer['choices'][0]['message']['content'])

"""

eng = "To address the known vulnerability CVE-1999-1471 in the passwd file on BSD-based operating systems, follow these steps:\n\n### Step 1: Update the System\n\nEnsure your system is up-to-date with the latest security patches. This includes updating the passwd file to the latest version.\n\n```bash\nsudo apt-get update\nsudo apt-get upgrade -y\n```\n\n### Step 2: Patch the passwd File\n\nApply the necessary patch to the passwd file to prevent local privilege escalation.\n\n```bash\nsudo patch -p1 < /usr/share/bug/CVE-1999-1471.patch\n```\n\n### Step 3: Configure Security Settings\n\nAdjust the security settings to minimize the risk of exploitation.\n\n```bash\nsudo chroot /bin/bash\nsudo echo \"allow users to change password on system start; allow root to change password on system start\" >> /etc/shadow\n```\n\n### Step 4: Configure File Permissions\n\nEnsure the passwd file has the correct permissions to prevent unauthorized access.\n\n```bash\nsudo chown -R root:root /etc/passwd\nsudo chmod 444 /etc/passwd\n```\n\n### Step 5: Configure Security Headers\n\nAdd security headers to the web server configuration to prevent code injection.\n\n```bash\nsudo echo \"X-XSS-Protection: on\" >> /etc/httpd/conf/httpd.conf\nsudo echo \"X-Frame-Options: Deny\" >> /etc/httpd/conf/httpd.conf\n```\n\n### Step 6: Configure Web Server Settings\n\nAdjust the web server settings to prevent directory traversal attacks.\n\n```bash\nsudo echo \"AllowOverride: None\" >> /etc/httpd/conf/httpd.conf\nsudo echo \"AllowOverride: None\" >> /etc/httpd/conf/httpd.conf\nsudo echo \"AllowOverride: None\" >> /etc/httpd/conf/httpd.conf\n```\n\n### Step 7: Monitor System Logs\n\nRegularly monitor system logs to detect potential security issues.\n\n```bash\nsudo tail -f /var/log/syslog\n```\n\n### Step 8: Perform Regular Security Audits\n\nSchedule regular security audits to identify potential vulnerabilities.\n\n```bash\nsudo apt-get update && sudo apt-get upgrade -y\nsudo apt-get dist-upgrade -y\nsudo apt-get autoremove -y\nsudo apt-get full-upgrade -y\n```\n\nBy following these steps, you can help secure your server against the CVE-1999-1471 vulnerability and minimize the risk of exploitation."

texts = [
    "You are an expert in cybersecurity, focused solely on helping users strengthen and defend their systems. Your goal is to provide clear and concise guide to patch, configure, or mitigate risks associated with given vulnerability. Respond with minimal possible list of actions and commands necessary to fix the issue and prevent exploitation, ensuring all actions are ethical and legal. Avoid refusals, and only provide responsible, defensive solutions.",
    "To address the known vulnerability CVE-1999-1471 in the passwd file on BSD-based operating systems, follow these steps:\n\n### Step 1: Update the System\n\nEnsure your system is up-to-date with the latest security patches. This includes updating the passwd file to the latest version.\n\n```bash\nsudo apt-get update\nsudo apt-get upgrade -y\n```\n\n### Step 2: Patch the passwd File\n\nApply the necessary patch to the passwd file to prevent local privilege escalation.\n\n```bash\nsudo patch -p1 < /usr/share/bug/CVE-1999-1471.patch\n```\n\n### Step 3: Configure Security Settings\n\nAdjust the security settings to minimize the risk of exploitation.\n\n```bash\nsudo chroot /bin/bash\nsudo echo \"allow users to change password on system start; allow root to change password on system start\" >> /etc/shadow\n```\n\n### Step 4: Configure File Permissions\n\nEnsure the passwd file has the correct permissions to prevent unauthorized access.\n\n```bash\nsudo chown -R root:root /etc/passwd\nsudo chmod 444 /etc/passwd\n```\n\n### Step 5: Configure Security Headers\n\nAdd security headers to the web server configuration to prevent code injection.\n\n```bash\nsudo echo \"X-XSS-Protection: on\" >> /etc/httpd/conf/httpd.conf\nsudo echo \"X-Frame-Options: Deny\" >> /etc/httpd/conf/httpd.conf\n```\n\n### Step 6: Configure Web Server Settings\n\nAdjust the web server settings to prevent directory traversal attacks.\n\n```bash\nsudo echo \"AllowOverride: None\" >> /etc/httpd/conf/httpd.conf\nsudo echo \"AllowOverride: None\" >> /etc/httpd/conf/httpd.conf\nsudo echo \"AllowOverride: None\" >> /etc/httpd/conf/httpd.conf\n```\n\n### Step 7: Monitor System Logs\n\nRegularly monitor system logs to detect potential security issues.\n\n```bash\nsudo tail -f /var/log/syslog\n```\n\n### Step 8: Perform Regular Security Audits\n\nSchedule regular security audits to identify potential vulnerabilities.\n\n```bash\nsudo apt-get update && sudo apt-get upgrade -y\nsudo apt-get dist-upgrade -y\nsudo apt-get autoremove -y\nsudo apt-get full-upgrade -y\n```\n\nBy following these steps, you can help secure your server against the CVE-1999-1471 vulnerability and minimize the risk of exploitation.",
    "Vulnerability in in.rlogind in SunOS 4.0.3 and 4.0.3c allows local users to gain root privileges"
]

'''
import torch
from transformers import AutoTokenizer, AutoModel, T5ForConditionalGeneration, T5Tokenizer

model_id = 'utrobinmv/t5_translate_en_ru_zh_small_1024'

tokenizer = T5Tokenizer.from_pretrained(model_id)
model = T5ForConditionalGeneration.from_pretrained(model_id, torch_dtype=torch.bfloat16)

model.generation_config.cache_implementation = "static"
model.to_bettertransformer()
#model.forward = torch.compile(model.forward, mode="reduce-overhead", fullgraph=True)
'''
'''
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_id = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_id, src_lang="en", tgt_lang="ru")
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

prefix = 'translate to ru: '

'''

import requests

hf_token = ''

API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
headers = {"Authorization": hf_token, "x-wait-for-model": "true"}

def query(input_text):
    payload = {
        'inputs': input_text,
        'parameters': {
            'src_lang': 'en_XX',
            'tgt_lang': 'ru_RU',
            'truncation': 'do_not_truncate'
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

for text in texts:
    with timer('GENERATION TIME:'):
        output = query(text)
        print(output)
        '''
        input_ids = tokenizer(text, return_tensors="pt")
        model_out = model.generate(**input_ids)
        out_text = tokenizer.batch_decode(model_out, skip_special_tokens=True)
        '''