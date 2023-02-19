Dashboard criada como trabalho da pós de Engenharia e Análise de Dados para a matéria de Visualização e Análise de Dados

Esse artigo visa ajudar a fazer o upload do seu Dashboard feito com o Streamlit online, para que assim divulgue com quem quiser seu trabalho.

1 - Pré-requisitos: 

Conta no Github (https://github.com/).
Conta no Share Streamlit (https://share.streamlit.io/)


2 - Arquivos necessários no github para que o Share Streamlit consiga ler e disponibilizar online sua Dash.

Esse é um exemplo da árvore de como deve estar o projeto no github.
![1676222503017](https://user-images.githubusercontent.com/5480615/219966494-ee71523b-5060-4f61-b9b6-8f1b9fced8d4.png)

Adicionar texto alternativo
Não foi fornecido texto alternativo para esta imagem
Meu git caso prefiram acompanhar por la e ver o conteúdo dos arquivos: https://github.com/IvanLopesGit/Streamlit_DATA_VIS
Explicando os arquivos:

pasta assets: aqui pode colocar suas imagens, .css, etc.
pasta data: aqui pode colocar seus DataSets
.gitignore: aqui onde você deve adicionar as pastas não relacionadas ao conteúdo que você criou (libs do streamlit e outros devem entrar na config desse arquivo).
readme.md: caso queira escrever sobre seu projeto
app.py: esse é seu arquivo principal, podendo ter outros arquivos .py.
requirements.txt: esse é outro arquivo importante junto do app.py, aqui você vai falar pro share streamlit o que deve ser instalado das libs que seu projeto está utilizando. Para criar esse arquivo basta você ir no console e digitar: pip freeze > requirements.txt
Importante: após criar o requirements, abra ele e remova a biblioteca py32win.py, ela não existe no servidor do streamlit. É um arquivo que permite a criação de componentes python no windows.



3 - Criando o aplicativo no streamlit online

Depois de criar sua conta no https://share.streamlit.io/, será possível ver um botão azul escrito "New App".







Adicionar texto alternativo
Não foi fornecido texto alternativo para esta imagem
Após clicar no botão, abrirá uma janela para que você faça o login no github onde deve estar seu projeto do streamlit.

Na próxima janela você pode selecionar o repositório.







Adicionar texto alternativo
Não foi fornecido texto alternativo para esta imagem
No "Main file path", você deve seleciona o arquivo com nome "app.py", este sendo o arquivo principal da sua aplicação.

Depois de tudo configurado, só clicar em deploy, então aguardar seu aplicativo ser disponibilizado online. 

Após ser concluído a etapa de upload, no site terá a lista dos aplicativos que você subiu.

Agora é só compartilhar seu projeto com quem quiser!
