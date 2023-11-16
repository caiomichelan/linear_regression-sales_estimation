# Regressão Linear - Estimativa de Vendas

## Data Science Project - Estimativa de Vendas

<div align='center'>

![pharmacy](https://github.com/caiomichelan/linear_regression-sales_estimation/assets/104601836/ecaa8d34-1964-484a-87e1-cec58870568e)

</div>

# 1. Problema do Negócio
<p align='justify'>Uma rede de farmácias precisa iniciar uma série de reformas em suas lojas a fim de melhorar o atendimento aos seus clientes. A base de recursos financeiros para orçamento a ser disponibilizado a cada loja provém hoje das projeções de vendas realizadas pelos seus gerentes.</p>
<p align='justify'>Ultimamente foram encontradas inconsistências nas projeções de uma série de lojas, desta forma houve a necessidade de contratação de uma equipe de Cientistas de Dados para prosseguir com a criação de um modelo estatístico de projeção de vendas para todas as lojas da rede.</p>
<p align='justify'>Com base nos resultados do modelo, o objetivo principal é direcionar de maneira mais assertiva os recursos financeiros para reforma de cada loja, baseado em sua projeção de vendas das próximas seis semanas.</p>

# 2. Premissas do Negócio
<p align='justify'>Foram desconsiderados fatores externos como economia e segmento do negócio.</p>
<p align='justify'>Foram consideradas apenas lojas abertas e que possuam alguma venda.</p>
<p align='justify'>Na Análise Exploratória foram desconsideradas datas em que as lojas estiveram fechadas.</p>
<p align='justify'>Considerando as lojas que não possuem lojas competidoras próximas, foi considerada uma distância muito maior à máxima distância observada na análise dos dados.</p>

# 3. Estratégia da Solução
<p align='justify'>Foi utilizada a metodologia CRISP-DM no desenvolvimento do projeto, através das seguintes etapas:</p>
<p align='justify'>- Data Description: Adquirir conhecimento sobre os dados com análise de colunas e sua nomenclatura, dimensão, tipos, verificação de dados nulos bem como seu tratamento, análise estatística descritiva a fim de encontrar padrões em suas métricas básicas, análise de distribuição das vendas e análise das variáveis categóricas.</p>
<p align='justify'>- Feature Engineering: Elaboração de Mapa Mental para análise do negócio, suas variáveis e atributos que as impactam diretamente. Nesta etapa também foram elaboradas as hipóteses a serem validadas na etapa de Análise Exploratória dos Dados (Exploratory Data Analysis).</p>
<p align='justify'>- Data Filtering: Filtro nos dados a fim de considerar os dados mais relevantes para a análise e modelagem estatística. Conforme indicado nas premissas, nesta etapa foram selecionadas apenas as lojas abertas e com ao menos uma venda registrada. Também foram removidas algumas colunas que não tiveram relevância na elaboração do modelo.</p>
<p align='justify'>- Exploratory Data Analysis: Realização de análise exploratória para identificação de padrões e melhor entendimento das variáveis e sua relevância ao aprendizado do modelo estatístico. Nesta etapa foram realizadas análises univariadas, bivariadas e multivariadas, com dados númericos e categóricos em conjunto. Através das análises bivariadas foram validadas as hipóteses definidas anteriormente.</p>
<p align='justify'>- Data Preparation: Preparação dos dados para aplicação dos modelos de Machine Learning, onde foram utilizadas técnicas de Rescaling e Transformation.</p>
<p align='justify'>- Feature Selection: Seleção das melhores variáveis a serem consideradas para treinamento do modelo de Machine Learning. A princípio foi utilizado o Boruta para apoio na seleção, mas após análise das variáveis consideradas foi avaliado que outras variáveis excluídas neste processo também tinham relevância  ao treinamento do modelo. Desta forma foram consideradas todas as variáveis selecionadas pelo Boruta e adicionadas outras variáveis manualmente. Também foram removidas as variáveis que não possuem nenhuma relevância ao treinamento do modelo.</p>
<p align='justify'>- Machine Learning Modelling: Realizado o treinamento de alguns modelos de Machine Learning com base nos dados propostos com a comparação de suas performances e avaliação do modelo ideal a ser utilizado efetivamente no projeto. Também foi implementada a técnica de Cross Validation a fim de garantir a performance dos modelos. Nesta etapa foram avaliados os modelos Average Model, Linear Regression Model, Linear Regression Regularized Model (Lasso), Random Forest Regressor e XGBoost Regressor.</p>
<p align='justify'>- Hyperparameter Fine Tunning: Após escolha no modelo XGBoost Regressor, foi aplicado o método de Random Search para escolha dos melhores parâmetros a este modelo, trazendo uma melhoria significativa em sua performance.</p>
<p align='justify'>- Error Interpretation: Demonstração do resultado obtido no projeto com avaliação da performance do modelo considerado, traduzindo seu resultado ao negócio e identificando o resultado financeiro esperado após sua implementação.</p>
<p align='justify'>- Deploy Model: Etapa com os passos para implementação do modelo em produção com a possibilidade de publicação em ambiente em nuvem, garantindo seu uso aos principais interessados, auxiliando nas Tomadas de Decisão.</p>

# 4. Insights de Dados
<p align='justify'>Algumas hipóteses validadas através da Análise Exploratória dos Dados:</p>
<p align='justify'>Hipóteses de Vendas no escopo das Lojas:</p>
<p align='justify'>- Lojas com maior variedade de produtos deveriam vender mais (Hipótese Rejeitada);</p>
<p align='justify'>- Lojas com competidores mais próximos deveriam vender menos (Hipótese Rejeitada);</p>
<p align='justify'>- Lojas com mais promoções consecutivas deveriam vender mais (Hipótese Rejeitada).</p>
<p align='justify'>Hipóteses de Vendas no escopo do Tempo:</p>
<p align='justify'>- Lojas abertas durante o feriado de Natal deveriam vender mais (Hipótese Rejeitada);</p>
<p align='justify'>- Lojas deveriam vender mais ao longo dos anos (Hipótese Rejeitada);</p>
<p align='justify'>- Lojas deveriam vender menos aos finais de semana (Hipótese Aceita);</p>
<p align='justify'>- Lojas deveriam vender menos durante feriados escolares (Hipótese Aceita - Exceto para o mês de Agosto);</p>

# 5. Produto Final
<p align='justify'>Com base nos dados das lojas e suas características, foi desenvolvido um modelo de previsão das vendas de cada loja, visando auxiliar efetivamente na definição do orçamento a ser disponibilizado a cada loja para realização de sua reforma, garantindo a melhor distribuição dos recursos financeiros para o objetivo em questão.</p>

# 6. Conclusão
<p align='justify'>O objetivo do projeto foi desenvolver um modelo de previsão das vendas de cada loja da rede de farmácias, garantindo a melhor distribuição dos recursos financeiros para realização das reformas propostas, tendo como base o faturamento das lojas de maneira individual.</p>
<p align='justify'>Com a implementação do modelo foi possível prever o faturamento das lojas de maneira geral com uma margem média de erro (MAPE) de aproximadamente 11%.</p>
<p align='justify'>Com base na projeção apresentada para as próximas seis semanas, a Diretoria Financeira poderá alocar os recursos de maneira mais eficiente em cada loja, tendo inclusive os cenários neutro, pessimista e otimista para auxílio no balizamento da Tomada de Decisão.</p>

# 7. Próximos Passos
<p align='justify'>Como próximos passos serão definidos estudos voltados às características geográficas das lojas, de modo a avaliar as vendas e refinar suas projeções com base na localização geográfica juntamente ao históricos de vendas.</p>
<p align='justify'>Também serão realizados estudos para otimização do modelo em produção com base nas necessidades da diretoria.</p>
