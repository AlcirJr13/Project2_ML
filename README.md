# CHURN FORECAST OF TELECOMMUNICATIONS CUSTOMERS WITH NEURAL NETWORK

## Projeto da disciplina de Aprendizagem de Máquina
## Pós Graduação em Engenharia Elétrica e de Computação (PPgEEC/UFRN)


 Podemos denominar como Churn a taxa de cancelamento de clientes em um determinado período, seja esse período mensal, trimestal ou anual por exemplo. Estes cancelamentos são um problema que cada vez mais as empresas procuram mitigar, uma vez que o cancelamento de um cliente, representa a diminuição de receita de uma empresa, comprometendo o faturamento do período analisado, bem como o faturamento a médio-longo prazo.

 Como proposta para desenvolvimento do 2º projeto da disciplina de Aprendizagem de Máquina, do curso de Pós Graduação em Engenharia Elétrica e de Computação (PPgEEC/CT) da UFRN, nós, Antonio Alcir e Tayná Arruda realizamos a continuação do estudo do [1º projeto](https://github.com/AlcirJr13/Project1_ML), implementando agora uma rede neural. Assim como o primeiro, utilizamos a base de dados disponibilizada por Bharti Prasad na paltaforma do [kaglle](https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction), objetivando realizar predições a partir do perfil de um cliente sobre sua tendência de churn, utilizando Python e o algoritmo de Machine Learning da Árvore de Decisão,conceitos básicos de MLOps, uma vez que o problema em questão é um problema de classificação que vai gerar uma árvore de decisão binária, retornando se o consumidor possui tendência a dar Churn ou não.

Os passos deste projeto, foram instruidos seguindo as orientações do repositório do prof. Dr. Ivanotich Silva[ para a disciplina de Aprendizagem de Máquina do PPgEEC/UFRN](https://github.com/ivanovitchm/ppgeecmachinelearning), incluindo a utilização do [Wandb](https://wandb.ai/), ferramenta para auxiliar o gerenciamento e versionamento do pipeline do modelo. Para fazer o deploy do nosso modelo, utilizamos FastAPI e criamos uma API de teste. Inicialmente fizemos todo o trabalho localmente e testamos para então, fazer o deploy no Heroku, que é uma plataforma (PaaS) que nos permite fazer o deploy da nossa aplicação Python. Ainda utilizamos o Anaconda para auxiliar nos nossos testes locais. O projeto está implementado no [slug](https://project2-ml-ppgeec.herokuapp.com).

#### Referencias

- :computer: Bharti Prasad. CUSTOMER CHURN PREDICTION. [[Link]](https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction)
- :octocat: Ivanotich Silva. EEC1509 Machine Learning. [[Link]](https://github.com/ivanovitchm/ppgeecmachinelearning)
- :page_facing_up: Douglas Silva. O que é churn rate, como calcular + 10 dicas para ajudar a reduzir essa taxa [[Link]](https://www.zendesk.com.br/blog/churn-rate/)
