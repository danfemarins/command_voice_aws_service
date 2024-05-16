# Comando de Voz para Serviço AWS

Este é um projeto de exemplo que demonstra como usar comandos de voz para interagir com serviços da AWS (Amazon Web Services), especialmente com o serviço ECS (Amazon Elastic Container Service).

## Funcionalidades

1. **Obtenção do Número de Tarefas:**
   - Você pode perguntar sobre o número de tarefas dentro de um serviço ECS específico.

2. **Verificação do Status do Servidor ECS:**
   - Pode-se verificar o status do servidor ECS para garantir que esteja funcionando corretamente.

3. **Visualização de Métricas de CPU:**
   - É possível obter informações sobre a utilização média da CPU nos últimos 15 minutos.

## Requisitos

Para executar este projeto, é necessário ter os seguintes pré-requisitos instalados:

- Python 3
- Bibliotecas Python:
  - boto3
  - speech_recognition
  - gtts

## Como Usar

1. **Configuração de Credenciais AWS:**
   - Certifique-se de que suas credenciais da AWS estão configuradas corretamente. Isso pode ser feito configurando variáveis de ambiente ou usando perfis de credenciais.

2. **Instalação de Dependências:**
   - Execute o seguinte comando para instalar as dependências Python necessárias:
     ```
     pip install boto3 speech_recognition gtts
     ```

3. **Execução do Código:**
   - Execute o script Python fornecido para iniciar o bot de comando de voz. Ele fornecerá instruções de voz sobre como interagir com o servidor ECS.

## Observações

- Este é um projeto de exemplo e pode ser estendido ou personalizado conforme necessário.
- Certifique-se de ter permissões adequadas para acessar os serviços da AWS mencionados no código.

Para qualquer dúvida ou problema, sinta-se à vontade para entrar em contato.

