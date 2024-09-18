
import openai
from dotenv import load_dotenv, find_dotenv

# função para requests na api
def get_gpt(client, messages,model='gpt-4o-mini-2024-07-18', max_tokens = 1000, temperature=0):
    result = client.chat.completions.create(messages=messages,
                                         model=model,
                                         max_tokens=max_tokens, 
                                         temperature=temperature,
                                         stream = True)
    # armazenandoe imprimindo a mensagem
    resp = ''
    print("Nath's assistant: ", end='')
    for stream in result:
        txt = stream.choices[0].delta.content
        if txt:    
            print(txt, end='')
            resp += txt
    print('')

    # adicionando a resposta ao contexto
    messages.append({'role':'assistant','content':resp})
    return messages

def get_user(messages):
    txt = input('User: ')

    if txt == 'sair':
        return txt

    messages.append({'role':'user','content':txt})
    return messages

if __name__ == '__main__':
    # importa variáveis do .env
    _ = load_dotenv(find_dotenv()) 

    # criando client
    client = openai.Client()

    # interface
    print("Nath's assistant: Olá, bem-vinda(o) ao NathGPT! :D \n  Pergunte o que quiser. Digite 'sair' quando quiser encerrar.")
    messages = list()
    while True:
        messages = get_user(messages)

        try:
            messages = get_gpt(client,messages)
        except:
            print("Nath's assistant: você encerrou o programa. Volte sempre!")
            break

    

