import boto3
import speech_recognition as sr
import os
from gtts import gTTS
from datetime import datetime, timedelta

def get_ecs_status():
    session = boto3.Session(region_name='sa-east-1')
    ecs = session.client('ecs') 
    response = ecs.describe_clusters(clusters=['Prod_api'])  
    status = response['clusters'][0]['status']
    return status

def get_task_count():
    session = boto3.Session(region_name='sa-east-1')
    ecs = session.client('ecs')
    response = ecs.list_tasks(cluster='Prod_api')  
    task_count = len(response['taskArns'])
    return task_count

def get_cpu_utilization():
    cloudwatch = boto3.client('cloudwatch', region_name='sa-east-1')
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/ECS',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'ClusterName',
                'Value': 'Prod_api'
            },
            {
                'Name': 'ServiceName',
                'Value': 'my-service'
            }
        ],
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=[
            'Average'
        ]
    )
    datapoints = response['Datapoints']
    if datapoints:
        return datapoints[-1]['Average']  # Último valor de utilização de CPU
    return "N/A"

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Reconhecendo comando...")
        command = recognizer.recognize_google(audio, language='pt-BR').lower()
        print("Comando reconhecido:", command)
        return command
    except sr.UnknownValueError:
        print("Desculpe, não entendi o comando.")
        return ""
    except sr.RequestError as e:
        print("Erro ao reconhecer comando; {0}".format(e))
        return ""

def speak(text):
    tts = gTTS(text=text, lang='pt-br')
    tts.save("response.mp3")
    os.system("start response.mp3")

def process_command(command):
    if "tarefas" in command:
        task_count = get_task_count()
        speak("O número de tarefas dentro do serviço é: {}".format(task_count))
    elif "status" in command:
        status = get_ecs_status()
        speak("O status do servidor ECS é: {}".format(status))
    elif "métricas" in command:
        cpu_utilization = get_cpu_utilization()
        speak("A utilização média de CPU nos últimos 15 minutos é de {}%".format(cpu_utilization))
    else:
        speak("Comando não reconhecido.")

def main():
    intro_text = "Olá! Meu nome é JIRA, sou o seu chat virtual por voz. Estou aqui para ajudá-lo com informações sobre o servidor ECS. Você pode me fazer uma pergunta sobre o número de tarefas, o status do servidor ECS ou as métricas de CPU. Por favor, fale 'tarefas' para obter o número de tarefas, 'status' para verificar o status do servidor ou 'métricas' para obter as métricas de CPU."
    print(intro_text)
    speak(intro_text)  # Introdução falada
    while True:
        command = listen_command()
        if command:
            process_command(command)

if __name__ == "__main__":
    print("Iniciando o bot...")
    main()
